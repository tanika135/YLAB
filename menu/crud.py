from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from .models import Menu, Submenu, Dish
from . import models, schemas
from .database import SessionLocal


def get_menus(db: Session):
    return db.query(models.Menu).all()


def create_menu(db: Session, menu: schemas.MenuCreate):
    db_menu = models.Menu(**menu.model_dump())
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu



def get_menu(db: Session, menu_id: str):
    # return db.query(models.Menu).filter(models.Menu.id == menu_id).first()
    with SessionLocal() as session:
        menu = session.query(Menu).filter(Menu.id == menu_id).first()
        if menu is None:
            raise HTTPException(status_code=404, detail="menu not found")
        submenus = session.query(Submenu).filter(Submenu.menu_id == menu_id).all()
        submenus_count = len(submenus)
        dishes_count = sum(
            session.query(func.count(Dish.id)).filter(Dish.submenu_id == submenu.id).scalar() for submenu in submenus)
        menu_dict = {
            "id": menu.id,
            "title": menu.title,
            "description": menu.description,
            "submenus_count": submenus_count,
            "dishes_count": dishes_count,
        }
        return menu_dict

def update_menu(db: Session, menu_id: str, menu: schemas.MenuCreate):
    db_menu = db.query(models.Menu).filter(models.Menu.id == menu_id).first()
    db_menu.title = menu.title
    db_menu.description = menu.description
    db.commit()
    db.refresh(db_menu)
    return db_menu


def delete_menu(db: Session, menu_id: str):
    db_menu = db.query(models.Menu).filter(models.Menu.id == menu_id).first()
    db.delete(db_menu)
    db.commit()
    return db_menu


def get_submenus(db: Session, menu_id: str):
    return db.query(models.Submenu).filter(models.Submenu.menu_id == menu_id).all()


def create_submenu(db: Session, menu_id: str, submenu: schemas):
    db_submenu = models.Submenu(**submenu.model_dump())
    db_submenu.menu_id = menu_id
    db.add(db_submenu)
    db.commit()
    db.refresh(db_submenu)
    return db_submenu


def get_submenu(db: Session, submenu_id: str):
    # return db.query(models.Submenu).filter(models.Submenu.id == submenu_id).first()
    with SessionLocal() as session:
        submenu = session.query(Submenu).filter(Submenu.id == submenu_id).first()
        if submenu is None:
            raise HTTPException(status_code=404, detail="submenu not found")
        dishes = session.query(Dish).filter(Dish.submenu_id == submenu_id).all()
        dishes_count = len(dishes)
        submenu_dict = {
            "id": submenu.id,
            "title": submenu.title,
            "description": submenu.description,
            "menu_id": submenu.menu_id,
            "dishes_count": dishes_count,
        }
        return submenu_dict


def update_submenu(db: Session, submenu_id: str, submenu: schemas.SubmenuCreate):
    db_submenu = db.query(models.Submenu).filter(models.Submenu.id == submenu_id).first()
    db_submenu.title = submenu.title
    db_submenu.description = submenu.description
    db.commit()
    db.refresh(db_submenu)
    return db_submenu


def delete_submenu(db: Session, submenu_id: str):
    db_submenu = db.query(models.Submenu).filter(models.Submenu.id == submenu_id).first()
    db.delete(db_submenu)
    db.commit()
    return db_submenu


def get_dishes(db: Session, submenu_id: str):
    return db.query(models.Dish).filter(models.Dish.submenu_id == submenu_id).all()


def create_dish(db: Session, submenu_id: str, dish: schemas.DishCreate):
    db_dish = models.Dish(**dish.model_dump())
    db_dish.submenu_id = submenu_id
    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)
    return db_dish


def get_dish(db: Session, dish_id: str):
    return db.query(models.Dish).filter(models.Dish.id == dish_id).first()


def update_dish(db: Session, dish_id: str, dish: schemas.DishCreate):
    db_dish = db.query(models.Dish).filter(models.Dish.id == dish_id).first()
    db_dish.title = dish.title
    db_dish.description = dish.description
    db_dish.price = dish.price
    db.commit()
    db.refresh(db_dish)
    return db_dish


def delete_dish(db: Session, dish_id: str):
    db_dish = db.query(models.Dish).filter(models.Dish.id == dish_id).first()
    db.delete(db_dish)
    db.commit()
    return db_dish

