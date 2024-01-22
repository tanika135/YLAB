from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base


class Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)

    submenus = relationship("Submenu", back_populates="menu")


class Submenu(Base):
    __tablename__ = "submenu"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    menu_id = Column(Integer, ForeignKey("menu.id"))

    menu = relationship("Menu", back_populates="submenus")


class Dish(Base):
    __tablename__ = "dish"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    price = Column(Float)
    submenu_id = Column(Integer, ForeignKey("submenu.id"))

    submenu = relationship("Submenu", back_populates="dishes")

