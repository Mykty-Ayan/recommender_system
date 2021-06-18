from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: str
    image: str


class Product(ProductBase):
    id: int
    price: int
    brand_id: int
    category_id: int

    class Config:
        orm_mode = True


class BrandBase(BaseModel):
    name: str


class Brand(BrandBase):
    id: int


class CategoryBase(BaseModel):
    name: str


class Category(CategoryBase):
    id: int
