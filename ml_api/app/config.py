import os

from pydantic import BaseSettings


class Settings(BaseSettings):
	API_V1_STR: str = "/api/v1"
	PROJECT_NAME = "Animal Activity Prediction API"


settings = Settings()

