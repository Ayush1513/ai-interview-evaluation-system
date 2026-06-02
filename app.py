from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.scoring_routes import router

from database.connection import engine
from database.connection import Base


Base.metadata.create_all(bind=engine)


app = FastAPI()


app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)


app.include_router(router)


@app.get("/")
def home():

    return {

        "message":
        "AI Agent System Running"

    }