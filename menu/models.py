import uuid

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, UUID
from sqlalchemy.orm import relationship

from .database import Base


class Menu(Base):
    __tablename__ = "menu"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
    description = Column(String)

    submenus = relationship("Submenu", back_populates="menu", cascade='save-update, merge, delete, delete-orphan')


class Submenu(Base):
    __tablename__ = "submenu"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
    description = Column(String)
    menu_id = Column(UUID, ForeignKey("menu.id"))

    menu = relationship("Menu", back_populates="submenus")
    dishes = relationship("Dish", back_populates="submenu", cascade='save-update, merge, delete, delete-orphan')


class Dish(Base):
    __tablename__ = "dish"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
    description = Column(String)
    price = Column(Float)
    submenu_id = Column(UUID, ForeignKey("submenu.id"))

    submenu = relationship("Submenu", back_populates="dishes")

