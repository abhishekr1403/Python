from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
import json

app = FastAPI()
load_dotenv()
client = genai.Client()


@app.get("/")
def read_root():
    return {"message": "My Test API is working.."}


@app.get('/margin')
def margin(revenue: float, expenses: float):
    profit = revenue - expenses
    margin_percent = (profit / revenue) * 100
    return {"profit": profit, "margin_percent": margin_percent}


class Review(BaseModel):
    text: str


class Sentiment(BaseModel):
    label: str
    score: int


@app.post('/sentiment')
def analyze_sentiment(review: Review):
    try:
        interaction = client.interactions.create(
            model='gemini-3.5-flash-lite',
            input="Find the sentiment of this customer review. "
                  "label must be 'positive', 'negative', or 'neutral'. "
                  "score must be a number from 1 (very bad) to 5 (very good). "
                    f'Review: {review.text}',
            response_format={
                "type": "text",
                "mime_type": "application/json",
                "schema": Sentiment.model_json_schema()
            },
        )
        return json.loads(interaction.output_text)

    except Exception as e:
        return f'Something went wrong, {e}'