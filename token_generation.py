# JSON Token generation utilizing the PyJWT Library
import jwt
import datetime

# Default token generation
def generate_token1():
    return jwt.encode({'username': 'user', 'email': 'user@mail.com'}, 'secretkey', algorithm='HS512')

# Token generation with expired time claim
def generate_token5():
    return jwt.encode({'username': 'user', 'email': 'user@mail.com', 'exp': datetime.datetime.utcnow()}, 'secretkey', algorithm='HS512')

# Token generation with correct time claim
def generate_token6():
    return jwt.encode({'username': 'user', 'email': 'user@mail.com', 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=10)
    }, 'secretkey', algorithm='HS512')

# Token generatoin for server
def generate_token(username, password):
    return jwt.encode({'username': username, 'password': password}, 'symmetrickey', algorithm='HS512')