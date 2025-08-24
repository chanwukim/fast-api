from passlib.context import CryptContext

class Crypto:
  def __init__(self):
    self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

  def encrypt(self, password: str):
    return self.pwd_context.hash(password)

  def verify(self, secret: str, hash: str):
    return self.pwd_context.verify(secret, hash)