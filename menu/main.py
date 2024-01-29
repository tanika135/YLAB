from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/v1/menus", response_model=list[schemas.Menu])
async def get_menus(db: Session = Depends(get_db)):
    menus = crud.get_menus(db)
    return menus


@app.post("/api/v1/menus", response_model=schemas.Menu, status_code=201)
async def create_menu(menu: schemas.MenuCreate, db: Session = Depends(get_db)):
    db_menu = crud.create_menu(db, menu)
    return db_menu


@app.get("/api/v1/menus/{menu_id}", response_model=schemas.Menu)
async def get_menu(menu_id: str, db: Session = Depends(get_db)):
    db_menu = crud.get_menu(db, menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    return db_menu


@app.patch("/api/v1/menus/{menu_id}", response_model=schemas.Menu)
async def update_menu(menu_id: str, menu: schemas.MenuCreate, db: Session = Depends(get_db)):
    db_menu = crud.update_menu(db, menu_id, menu)
    if db_menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    return db_menu


@app.delete("/api/v1/menus/{menu_id}", response_model=schemas.Menu)
async def delete_menu(menu_id: str, db: Session = Depends(get_db)):
    db_menu = crud.delete_menu(db, menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    return db_menu


@app.get("/api/v1/menus/{menu_id}/submenus", response_model=list[schemas.Menu])
async def get_submenus(menu_id: str, db: Session = Depends(get_db)):
    db_menu = crud.get_submenus(db, menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    return db_menu


@app.post("/api/v1/menus/{menu_id}/submenus", response_model=schemas.Menu, status_code=201)
async def create_submenu(menu_id: str, submenu: schemas.SubmenuCreate, db: Session = Depends(get_db)):
    db_submenu = crud.create_submenu(db, menu_id, submenu)
    return db_submenu


@app.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}", response_model=schemas.Submenu)
async def get_submenu(submenu_id: str, db: Session = Depends(get_db)):
    db_submenu = crud.get_submenu(db, submenu_id)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail="submenu not found")
    return db_submenu


@app.patch("/api/v1/menus/{menu_id}/submenus/{submenu_id}", response_model=schemas.Submenu)
async def update_submenu(submenu_id: str, submenu: schemas.SubmenuCreate, db: Session = Depends(get_db)):
    db_submenu = crud.update_submenu(db, submenu_id, submenu)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail="submenu not found")
    return db_submenu


@app.delete("/api/v1/menus/{menu_id}/submenus/{submenu_id}", response_model=schemas.Submenu)
async def delete_submenu(submenu_id: str, db: Session = Depends(get_db)):
    db_submenu = crud.delete_submenu(db, submenu_id)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail="submenu not found")
    return db_submenu


