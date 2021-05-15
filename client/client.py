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
    def __init__(self):
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
        listenThread = self.ListenForReplies()

        while True:
            if self.disconnectEvent.is_set():
                break

            if not self.loggedIn:
                print("Login:")
                username = input("Username: ")
                password = input("Password: ")
                logReq = " ".join(["LOGIN", username, password])
                self.SendMessage(logReq.encode(FORMAT))
            else:
                req = input("Request: ")
                self.SendMessage(req.encode(FORMAT))

            data = None
            while True:
                if self.disconnectEvent.is_set():
                    break
                if not self.dataQueue.empty():
                    data = self.dataQueue.get()
                    break

            print(data)
            
        listenThread.join()

    def Login(self):
        pass

    def Register(self):
        pass

    def RequestWeatherData(self, command):
        pass

    def SendMessage(self, message:bytes):
        '''
        Send a message to the server
        
        Parameters:

        Returns:

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
    def ListenForReplies(self):
        '''
        '''
        while True:
            message = None
            try:
                # Listens for HEADER message
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
            except Exception as e:
                # Please handle errors
                # Remember to catch "no connection" exception first (what is it called again?)
                return

            # Now that we have a message
            # If the message is "DISCONNECT"
            #   It means the server wants to disconnect
            #   -> Send confirm disconnection and break
            if message == b'DISCONNECT':
                log.info(f"Server has requested disconnection.")
                self.disconnectEvent.set()
                break

            # Any other messages:
            self.dataQueue.put(message)

            # Go back to listening

        log.info(f"Listener thread has terminated")


if __name__ == '__main__':
    a = ClientProgram()
    a.Connect()
    a.Run()
