from pydantic import BaseModel, UUID4
from decimal import Decimal


class DishBase(BaseModel):
    title: str
    description: str | None = None
    price: Decimal


class DishCreate(DishBase):
    pass


class Dish(DishBase):
    id: UUID4
    submenu_id: UUID4

    class Config:
        orm_mode = True


class SubmenuBase(BaseModel):
    title: str
    description: str | None = None


class SubmenuCreate(SubmenuBase):
    pass


class Submenu(SubmenuBase):
    id: UUID4
    dishes: list[Dish] = []

    class Config:
        orm_mode = True


class MenuBase(BaseModel):
    title: str
    description: str | None = None


class MenuCreate(MenuBase):
    pass


class Menu(MenuBase):
    id: UUID4
    submenus: list[Submenu] = []

    class Config:
        orm_mode = True

