import uvicorn

from fastapi import FastAPI

app = FastAPI()
# localhost:8000/docs에 문서화 된 페이지 생성됨

@app.get("/")
async def root():
    return {"message": "Hello World"}
    
if __name__ == "__main__":
	uvicorn.run("main:app", host="127.0.0.1", reload=True)