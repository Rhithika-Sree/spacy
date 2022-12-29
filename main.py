from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import uvicorn
import spacy 

from pydantic import BaseModel

app = FastAPI(
    title="Spacy API",
    description="Test",
    version="0.1.0",
    docs_url="/",
)

class Item(BaseModel):
    text: str

def get_response(text):
    nlp1 = spacy.load("model-best")
    docx = nlp1(text)
    # print(docx.ents)
    # return entity for each token
    entities = []
    for ent in docx.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)
        entities.append(ent.text)
    return entities
    


@app.post("/")
async def create_item(item: Item):
    response = dict()
    # prompt = f"Human : Person{item.text}AI  Gabby"
    response['text'] = get_response(item.text)
    print(response['text'])
    return response



if __name__ == "__main__":
    uvicorn.run(app, port=9000)

    
