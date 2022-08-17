import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv

from app.routers import blog_routers, user_routers, token_routers, like_routers

load_dotenv()

app = FastAPI()

app.include_router(blog_routers.router)
app.include_router(token_routers.router)
app.include_router(user_routers.router)
app.include_router(like_routers.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)