import uvicorn

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from user.interface.controller.user_controller import router as user_routers

# localhost:8000/docs에 문서화 된 페이지 생성됨
app = FastAPI() 
app.include_router(user_routers)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
    ):
    return JSONResponse(
        status_code=400,
        content=exc.errors()
    )

@app.get("/")
async def root():
    return {"message": "Hello World"}


    
if __name__ == "__main__":
	uvicorn.run("main:app", host="127.0.0.1", reload=True)