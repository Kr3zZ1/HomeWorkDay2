import uvicorn
import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Terran(BaseModel):
    name: str
    birthday: datetime.date
    deathday: Optional[datetime.date] = None
    yearold: int
    weapon: str

terrans = []

@app.get("/terrans", response_model=List[Terran])
def get_terrans():
    return terrans

@app.post("/terran", response_model=Terran)
def create_terran(terran: Terran):
    terrans.append(terran)
    return terran

@app.put("/terran/{index}", response_model=Terran)
def update_terran(index: int, terran: Terran):
    if index < 0 or index >= len(terrans):
        raise HTTPException(status_code=404, detail="Terran not found")
    terrans[index] = terran
    return terran

@app.delete("/terran/{index}", response_model=Terran)
def delete_terran(index: int):
    if index < 0 or index >= len(terrans):
        raise HTTPException(status_code=404, detail="Terran not found")
    return terrans.pop(index)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)