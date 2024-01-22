from pydantic import BaseModel


class DishBase(BaseModel):
    title: str
    description: str | None = None
    price: float


class DishCreate(DishBase):
    pass


class Dish(DishBase):
    id: int
    submenu_id: int

    class Config:
        orm_mode = True


class SubmenuBase(BaseModel):
    title: str
    description: str | None = None


class SubmenuCreate(SubmenuBase):
    pass


class Submenu(SubmenuBase):
    id: int
    dishes: list[Dish] = []

    class Config:
        orm_mode = True


class MenuBase(BaseModel):
    title: str
    description: str | None = None


class MenuCreate(MenuBase):
    pass


class Menu(MenuBase):
    id: int
    submenus: list[Submenu] = []

    class Config:
        orm_mode = True

