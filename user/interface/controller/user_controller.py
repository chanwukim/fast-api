from fastapi import APIRouter
from pydantic import BaseModel

from user.application.user_service import UserService

router = APIRouter(prefix="/users")

class CreateUserBody(BaseModel):
  name: str
  email: str
  password: str

@router.post("/", status_code=201)
def create_user(body: CreateUserBody):
  user_service = UserService()
  created_user = user_service.create_user(
    name =body.name,
    email=body.email,
    password=body.password
  )
  
  return created_user