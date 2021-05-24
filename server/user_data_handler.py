import enum

class UserDataHandler:
    class LoginState(enum.Enum):
        NO_USERNAME = 0,
        WRONG_PASSWORD = 1,
        VALID = 2

    class RegisterState(enum.Enum):
        DUPLICATE = 0,
        VALID = 1,
        WEAK_PASSWORD = 2
    
    def __init__(self, jsonPath):
        pass

    def __del__(self):
        pass

    def Verify(self, username, password):
        return UserDataHandler.LoginState.VALID
        pass

    def Register(self, username, password):
        pass

    def Delete(self, username):
        pass