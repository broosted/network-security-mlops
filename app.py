import os, sys
import certifi
from pymongo import MongoClient
ca = certifi.where()

from dotenv import load_dotenv
load_dotenv()

from networksecurity.pipelines.training_pipeline import TrainingPipeline
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.components.model_trainer import NetworkModel

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import RedirectResponse
import pandas as pd

from networksecurity.utils.main_utils.utils import load_object
from networksecurity.constants.training_pipeline import *

MONGO_DB_PW = os.getenv("MONGODB_PW")
MONGO_DB_USER = os.getenv("MONGODB_USER")

mongoDB_url = f"mongodb+srv://{MONGO_DB_USER}:{MONGO_DB_PW}@cluster0.ld7yesa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(mongoDB_url, tlsCAFile=ca)

database = client[DATA_INGESTION_DATABASE_NAME]
collection_name = database[DATA_INGESTION_COLLECTION_NAME]

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="./templates")

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()
        return Response("Training successful !!")
    except Exception as e:
        raise NetworkSecurityException(e, sys)

@app.post("/predict")
async def predict_route(request: Request, file: UploadFile = File(...)):
    try:
        df = pd.read_csv(file.file)
        preprocessor = load_object(file_path="final_models/preprocessor.pkl")
        model = load_object(file_path="final_models/model.pkl")
        network_model = NetworkModel(preprocessor=preprocessor, model=model)
        print(df.iloc[0])
        y_pred = network_model.predict(df)
        print(y_pred)
        df['predicted_column'] = y_pred
        print(df['predicted_column'])

        df.to_csv("prediction_output/output.csv")
        table_html = df.to_html(classes="table table-striped")

        return templates.TemplateResponse("table.html", {"request": request, "table": table_html})
    except Exception as e:
        raise NetworkSecurityException(e, sys)


if __name__ == "__main__":
    app_run(app, host="localhost", port=8000)
    logging.info("Starting server at http://localhost:8000")