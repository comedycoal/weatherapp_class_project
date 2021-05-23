'''
Console-based module for weather app client side functionality
'''
import threading
import logging
import socket
import queue
import time
import os
from pathlib import Path
from enum import Enum

D_HOST = '127.0.0.1'
D_PORT = 7878
FORMAT = 'utf-8'

HEADER_LENGTH = 64
ID_LENGTH = 16

LOG_PATH = os.path.join(Path(__file__).parent.absolute(),"client.log")

#-------------------- Set-up for logger --------------------#
log = logging.getLogger(__name__)

f_formatter = logging.Formatter(fmt="%(asctime)s [%(levelname)s at %(funcName)s in %(filename)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
c_formatter = logging.Formatter(fmt="[%(levelname)s] %(message)s", datefmt="")

f_handler = logging.FileHandler(filename=LOG_PATH, mode='w+')
f_handler.setLevel(logging.DEBUG)
f_handler.setFormatter(f_formatter)

c_handler = logging.StreamHandler()
c_handler.setLevel(logging.WARNING)
c_handler.setFormatter(c_formatter)

log.setLevel(logging.DEBUG)
log.addHandler(f_handler)
log.addHandler(c_handler)

#-------------------- Threaded decorator --------------------#
def threaded(func):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper

def threaded_daemon(func):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs, daemon=True)
        thread.start()
        return thread
    return wrapper

class ClientProgram:
    '''
    Class for the client program that represents and encapsulates traffic and commands to and from a server for weather data

    Attributes:
        sock (socket.socket):
            The communication socket with the server
        connected (bool):
            indicates the status of the communication channel
        requestID (int):
            current requestID for this connection session
        dataQueue (queue.Queue):
            Queue for replies from the server
        
    '''
    class State(Enum):
        '''
        Provides an enumeration for standard communicative status between client and servers.
        All request wrapper should return a State status

        - SUCCEEDED: the request is sent perfectly and there might be extra data attached from the server
        - FAILED: the request is sent perfectly but the server did not process successfully
        - BADCONNECTION: the request is not sent
        '''
        SUCCEEDED = 1,
        FAILED = 2,
        BADCONNECTION = 3

    def __init__(self):
        '''
        Constructs a client program object
        '''
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False
        self.requestID = 0
        self.dataQueue = queue.Queue()
        self.loggedIn = False

        self.disconnectEvent = threading.Event()
        log.info("Client program initiated")
        pass

    def Connect(self, host=D_HOST, port=D_PORT):
        try:
            if not self.sock:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, port))
            self.requestID = 0
            self.connected = True
            log.info(f"Connected to server at ({host}, {port})")
            return True
        except Exception as e:
            log.exception("Exception occured")
            log.info("No connection established")
            return False

    def Disconnect(self):
        if not self.sock:
            return
        self.sock.close()
        self.connected = False
        self.sock = None
        log.info("Socket closed. Connection to server has terminated")

    def Run(self):
        listenThread = self.ListenForMessages()

        while True:
            if self.disconnectEvent.is_set():
                break

            req = input("Request: ")
            self.SendMessage(req.encode(FORMAT))
            if req == 'DISCONNECT':
                self.disconnectEvent.set()

            data = None
            
            while True:
                if self.disconnectEvent.is_set():
                    break
                if not self.dataQueue.empty():
                    data = self.dataQueue.get()
                    break

            print(data)
            
        self.Disconnect()
        listenThread.join()
        print("Client program ended")

    def Login(self, username:str, password:str):
        '''
        Wrapper function to request to the server command 'LOGIN'

        Parameters:
            username (str): self-explanatory
            password (str): self-explanatory

        Returns:
            state (ClientProgram.State):
                dictates the status of the request
            extraData (bytes):
                an attached error message from server, indicates the problem with the requested login
        '''
        pass

    def Register(self, username:str, password:str):
        '''
        Wrapper function to request to the server command 'REGISTER'

        Parameters:
            username (str): self-explanatory
            password (str): self-explanatory

        Returns:
            state (ClientProgram.State):
                dictates the status of the request
            extraData (bytes):
                an attached error message from server, indicates the problem with the requested registration
        '''
        pass

    def RequestWeatherDataAll(self):
        '''
        Wrapper function to request to the server command 'LISTALL'

        Parameters:

        Returns:
            state (ClientProgram.State):
                dictates the status of the request
            extraData (bytes):
                an attached error message from server, indicates the problem with the requested weather data
        '''
        pass

    def RequestWeatherDate7DaysOf(self, city_id):
        '''
        Wrapper function to request to the server command 'LIST'

        Parameters:

        Returns:
            state (ClientProgram.State):
                dictates the status of the request
            extraData (bytes):
                an attached error message from server, indicates the problem with the requested weather data
        '''
        pass

    def SendMessage(self, message:bytes):
        '''
        Send a message to the server
        
        Parameters:
            message (bytes):
                Message to send, in bytes

        Returns:
            state (bool):
                if True, the message is sent successfully
                if False, an error has occured and the message is either not sent or sent errorneously
        '''
        bytes_sent = 0
        try:
            length = len(message)
            header = str(length).encode(FORMAT)
            header += b' ' * (HEADER_LENGTH - len(header))

            # Add id to the message?
            
            bytes_sent = self.sock.send(header)
            assert bytes_sent == HEADER_LENGTH, "Length of message sent does not match that of the actual message"
                
            bytes_sent = self.sock.send(message)
            assert bytes_sent == length, "Length of message sent does not match that of the actual message"

            log.info(f"Sent message of length {length} to server.")
            return True
        except AssertionError as e:
            log.info(f"Couldn't send full message of length {length} to server. Only {bytes_sent}")
        except Exception as e:
            log.exception(f"Counld not send message of length {length} to server.")

        return False
    
    @threaded
    def ListenForMessages(self):
        '''
        Threaded - Enable message listening mechanism

        The method actively listens for requests
        The method terminates if:
            - The connection is lost
            - The server wants to disconnect, this will only happens once the client confirms with a specific message
            - the client wants to disconnect (via a message), this will happens once a specific message is received, regardless of unsent replies

        Parameters:
            requestQueue (queue.Queue):
                The queue for requests to be put in for processing
                Default is None.
                If None, this object will use the class level UniversalRequestQueue to put in requests
        '''
        while True:
            message = None
            try:
                # Listens for HEADER message
                hasMessage = self.sock.recv(HEADER_LENGTH, socket.MSG_PEEK).decode(FORMAT)
                if hasMessage:
                    message_length = self.sock.recv(HEADER_LENGTH).decode(FORMAT)
                    if message_length:
                        length = int(message_length)
                        # If HEADER is caught, listens for the actual message
                        bytesReceived = 0
                        chunks = []
                        while bytesReceived < length:
                            message = self.sock.recv(length - bytesReceived)
                            bytesReceived += len(message)
                            chunks.append(message)
                        message = b''.join(chunks)
                        log.info(f"Client has received message of length {message_length}")
            except ConnectionResetError as e:
                self.disconnectEvent.set()
                log.exception(f"Abrupt disconnection occured while listening for messages. The connection will effectively close")
                break
            except Exception as e:
                # Please handle errors, maybe?
                self.disconnectEvent.set()
                log.exception(f"Exception occured on listening thread.")
                break

            # Now that we have a message
            # If the message is "DISCONNECT"
            #   It means the server wants to disconnect
            #   -> Send confirm disconnection and break
            if message == b'DISCONNECT':
                log.info(f"Server has requested disconnection.")
                self.disconnectEvent.set()
                self.SendMessage(b'CONFIRM DISCONNECTION')
                break

            # Any other messages:
            self.dataQueue.put(message)

            # Go back to listening

        log.info(f"Listener thread has terminated")


if __name__ == '__main__':
    a = ClientProgram()
    a.Connect()
    a.Run()
