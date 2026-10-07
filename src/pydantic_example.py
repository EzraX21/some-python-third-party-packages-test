from pydantic import BaseModel, EmailStr

class Order(BaseModel):
    id: int
    email: EmailStr
    total: float

order = Order(id="1042", email="alex@example.com", total="89.99")
print(order.total, type(order.total))  # auto-coerced to float

Order(id=2, email="not-an-email", total=5)  # raises a clear validation error