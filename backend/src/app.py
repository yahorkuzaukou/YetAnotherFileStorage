from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


app = FastAPI()


origins = ["*"]
cors_middleware = CORSMiddleware(
    app=app,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)