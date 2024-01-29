from sqlalchemy.orm import Session

from . import models, schemas


def get_menus(db: Session):
    return db.query(models.Menu).all()


def create_menu(db: Session, menu: schemas.MenuCreate):
    db_menu = models.Menu(**menu.model_dump())
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu


def get_menu(db: Session, menu_id: str):
    return db.query(models.Menu).filter(models.Menu.id == menu_id).first()


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
    return db.query(models.Submenu).filter(models.Submenu.id == submenu_id).first()


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

