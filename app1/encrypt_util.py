from cryptography.fernet import Fernet
import base64
import logging
import traceback
from django.conf import settings

def encrypt(password):
    try:
        password = str(password)
        cipher_password = Fernet(settings.ENCRYPT_KEY)
        encrypted_password = cipher_password.encrypt(password.encode('ascii'))
        encrypted_password = base64.urlsafe_b64decode(encrypted_password).decode('ascii')
        return encrypted_password
    except Exception as e:
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None
    # except UnicodeDecodeError:
    #     decrypted_password = base64.urlsafe_b64decode(encrypted_password).decode('utf-8',)

    
def decrypt(password):
    try:
        password = base64.urlsafe_b64decode(password)
        cipher_password = Fernet(settings.ENCRYPT_KEY)
        decode_password = cipher_password.decrypt(password).decode('ascii')
        return decode_password
    except Exception as e:
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None
