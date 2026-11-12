from sqlalchemy.orm import Session
import models, schemas

def create_dataset(db: Session, dataset: schemas.DatasetCreate):
    obj = models.Dataset(**dataset.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_datasets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Dataset).offset(skip).limit(limit).all()

def get_dataset(db: Session, dataset_id: int):
    return db.query(models.Dataset).filter(models.Dataset.id == dataset_id).first()

def update_dataset(db: Session, dataset_id: int, dataset: schemas.DatasetUpdate):
    obj = get_dataset(db, dataset_id)
    if obj is None:
        return None
    for key, value in dataset.model_dump().items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_dataset(db: Session, dataset_id: int):
    obj = get_dataset(db, dataset_id)
    if obj is None:
        return None
    db.delete(obj)
    db.commit()
    return obj
