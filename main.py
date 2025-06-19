from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

class InputText(BaseModel):
    text: str

class MeaningNode(BaseModel):
    node_id: str
    content: str
    transformation: str

class MeaningRoute(BaseModel):
    route: List[MeaningNode]
    resolved_meaning: str

@app.post("/navigate-meaning", response_model=MeaningRoute)
def navigate_meaning(input_text: InputText):
    # TODO: Реализовать смысловой разбор
    nodes = []
    # Пример: для запроса "Сколько будет дважды два?"
    # nodes.append(MeaningNode(node_id="math", content="дважды два", transformation="умножение"))
    # nodes.append(MeaningNode(node_id="result", content="4", transformation="ответ"))
    # return MeaningRoute(route=nodes, resolved_meaning="4")
    return MeaningRoute(route=[], resolved_meaning="Not implemented yet")
