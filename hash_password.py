# uuid is used to generate a random number
# import uuid
import hashlib


def hash_password(password):
    # salt is a random sequence added to the password string before
    # using the hash function. The salt is used in order to prevent
    # dictionary attacks and rainbow tables attacks
    # salt = uuid.uuid4().hex
    return hashlib.md5()
