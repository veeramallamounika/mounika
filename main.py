from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Food Delivery API is running"}


foods = [
    {"id": 1, "name": "Chicken Biryani", "price": 250},
    {"id": 2, "name": "Veg Biryani", "price": 180},
    {"id": 3, "name": "Chicken Burger", "price": 150},
    {"id": 4, "name": "Pizza", "price": 300}
]


@app.get("/foods")
def get_foods():
    return foods