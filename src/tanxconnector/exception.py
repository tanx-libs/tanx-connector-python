class AuthenticationError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.name = 'AuthenticationError'

class ConnectNotCalled(Exception):
    pass

class CoinNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.name = 'CoinNotFoundError'


class InvalidAmountError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.name = 'InvalidAmountError'


class AllowanceTooLowError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.name = 'AllowanceTooLowError'


class BalanceTooLowError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.name = 'BalanceTooLowError'


def is_authentication_error(err):
    return isinstance(err, AuthenticationError)


__all__ = [
    "AuthenticationError",
    "is_authentication_error",
    "CoinNotFoundError",
    "AllowanceTooLowError",
    "BalanceTooLowError",
    "InvalidAmountError",
]
