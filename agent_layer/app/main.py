from google import genai
from decouple import config
import logging

PROJECT_ID = config("PROJECT_ID") 
REGION = config("REGION") 
MODEL_NAME = config("MODEL_NAME")


if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    client = genai.Client(vertexai=True, project=PROJECT_ID, location=REGION)
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents="Você é uma inteligência artificial?",
    )
    logging.info({"Você é uma inteligência artificial?": response.text})