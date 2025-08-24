from datetime import datetime
from fastapi import HTTPException
from ulid import Ulid
from user.domain.repository.user_repo import IUserRepository
from user.domain.user import User
from user.infra.repository.user_repo import UserRepository
from utils.crypto import Crypto

class UserService:
  def __init__(self):
    self.user_repo: IUserRepository = UserRepository()
    self.ulid = Ulid()
    self.crypto = Crypto()

  def create_user(self, name: str, email: str, password: str):
    found_user = None

    try:
      found_user = self.user_repo.find_by_email(email)
    except HTTPException as e:
      if e.status_code != 422:
        raise e

    if found_user:
      raise HTTPException(status_code=422, detail="User already exists")

    now = datetime.now()
    user: User = User(
      id=self.ulid.generate(),
      name=name,
      email=email,
      password=self.crypto.encrypt(password),
      created_at=now,
      updated_at=now
    )
    self.user_repo.save(user)
    return user
