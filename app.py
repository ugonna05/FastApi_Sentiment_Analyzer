from imp import reload
from socketserver import BaseRequestHandler
import libs
from mimetypes import init
import uvicorn
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional, List
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = FastAPI()

class SentimentalText(BaseModel):
    text: Optional[str] = 'text'

@app.get("/analyzer")
async def analyzer(message: SentimentalText):

    sentiment_analyzer = SentimentIntensityAnalyzer()
    sentiment_dict = sentiment_analyzer.polarity_scores(message.text)
    

    label = None
    score = None

    if sentiment_dict['compound'] >= 0.5 :
        label = "Positive"
        score = round(sentiment_dict["compound"], 2)
 
    elif sentiment_dict['compound'] <= - 0.05 :
        label = "Negative"
        score = round(sentiment_dict["all"], 2)
 
    else :
       label = "Neutral"
       score = round(sentiment_dict["all"], 2)
    
    return f"The sentiment of the text is {label} with a Score of: {score}"

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
