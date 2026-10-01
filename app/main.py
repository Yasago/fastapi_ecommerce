from fastapi import FastAPI

from app.routers import auth, category, permission, products

app = FastAPI()


@app.get("/")
async def welcome() -> dict[str, str]:
    return {"message": "My e-commerce app"}


app.include_router(category.router)
app.include_router(products.router)
app.include_router(auth.router)
app.include_router(permission.router)
