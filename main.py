from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Dataset Management API", version="1.1.0")

@app.get("/")
def home():
    return {"message": "Welcome to the Dataset Management API"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/datasets/", response_model=schemas.DatasetResponse, status_code=status.HTTP_201_CREATED)
def create_dataset(dataset: schemas.DatasetCreate, db: Session = Depends(get_db)):
    return crud.create_dataset(db, dataset)

@app.get("/datasets/", response_model=list[schemas.DatasetResponse])
def read_datasets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_datasets(db, skip, limit)

@app.get("/datasets/{dataset_id}", response_model=schemas.DatasetResponse)
def read_dataset(dataset_id: int, db: Session = Depends(get_db)):
    item = crud.get_dataset(db, dataset_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Dataset not found")
    return item

@app.put("/datasets/{dataset_id}", response_model=schemas.DatasetResponse)
def update_dataset(dataset_id: int, dataset: schemas.DatasetUpdate, db: Session = Depends(get_db)):
    item = crud.update_dataset(db, dataset_id, dataset)
    if item is None:
        raise HTTPException(status_code=404, detail="Dataset not found")
    return item

@app.delete("/datasets/{dataset_id}")
def delete_dataset(dataset_id: int, db: Session = Depends(get_db)):
    item = crud.delete_dataset(db, dataset_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Dataset not found")
    return {"message": "Dataset deleted successfully", "dataset_id": dataset_id}
