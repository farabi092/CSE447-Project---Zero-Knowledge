import jwt
import datetime
import random
import secrets
from django.conf import settings

def generate_jwt_token(user):
   
    payload = {
        'user_id': user.id,
        'username': user.username,
        'role': user.role, 
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1), #expiry in 1 day
        'iat': datetime.datetime.utcnow(),
    }
    
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token

def generate_otp():
   
    return str(random.randint(100000, 999999))


def generate_password_salt():
    
    return secrets.token_hex(16)


def combine_password_and_salt(raw_password, salt):
  
    return f"{raw_password}{salt}"