from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import SessionLocal
from .config import settings

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/books", response_model=list[schemas.BookOut])
def read_books(api_key: str = Header(None), db: Session = Depends(get_db)):
    print(f"API Key received: {api_key}")
    print(f"Expected API Key: {settings.get('API_KEY') or settings.get('api_key')}")
    if api_key != (settings.get("API_KEY") or settings.get("api_key")):
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return crud.get_books(db)

@router.post("/books", response_model=schemas.BookOut)
def create_book(book: schemas.BookCreate, api_key: str = Header(None), db: Session = Depends(get_db)):
    print(f"API Key received: {api_key}")
    expected = settings.get("API_KEY") or settings.get("api_key")
    print(f"Expected API Key: {expected}")
    if api_key != expected:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return crud.create_book(db, book)

@router.put("/books/{book_id}", response_model=schemas.BookOut)
def update_book(book_id: int, book: schemas.BookUpdate, api_key: str = Header(None), db: Session = Depends(get_db)):
    if api_key != (settings.get("API_KEY") or settings.get("api_key")):
        raise HTTPException(status_code=401, detail="Invalid API Key")
    updated_book = crud.update_book(db, book_id, book)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

@router.delete("/books/{book_id}")
def delete_book(book_id: int, api_key: str = Header(None), db: Session = Depends(get_db)):
    if api_key != (settings.get("API_KEY") or settings.get("api_key") ):
        raise HTTPException(status_code=401, detail="Invalid API Key")
    deleted = crud.delete_book(db, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted"}
