# JSON Token verification utilizing the PyJWT Library
import jwt
import datetime

# Token verification with correct information
def verify_token1(token):
    correct_payload = {'username': 'user', 'email': 'user@mail.com'}
    decoded_token = jwt.decode(token, 'secretkey', algorithms=['HS512'])

    if decoded_token == correct_payload:
        return True
    else:
        return False

# Token verification with incorrect secret
def verify_token2(token):
    correct_payload = {'username': 'user', 'email': 'user@mail.com'}
    decoded_token = jwt.decode(token, 'secret', algorithms=['HS512'])

    if decoded_token == correct_payload:
        return True
    else:
        return False

# Token verification with incorrect algorithm
def verify_token3(token):
    correct_payload = {'username': 'user', 'email': 'user@mail.com'}
    decoded_token = jwt.decode(token, 'secretkey', algorithms=['HS256'])

    if decoded_token == correct_payload:
        return True
    else:
        return False

# Token verification with incorrect payload
def verify_token4(token):
    correct_payload = {'username': 'user'}
    decoded_token = jwt.decode(token, 'secretkey', algorithms=['HS512'])

    if decoded_token == correct_payload:
        return True
    else:
        return False

# Token verification with expired time claim
def verify_token5(token):
    decoded_token = jwt.decode(token, 'secretkey', algorithms=['HS512'])

    if decoded_token['exp'] != datetime.datetime.utcnow():
        return True
    else:
        return False

#Token verification for server
def verify_token(token):
    correct_payload = {'firstname': 'John', 'lastname': 'Doe'}
    decoded_token = jwt.decode(token, 'symmetrickey', algorithms=['HS512'])

    if decoded_token == correct_payload:
        return True
    else:
        return False