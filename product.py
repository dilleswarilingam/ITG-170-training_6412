from fastapi import APIRouter
router=APIRouter()

@router.get("/products")
async def get_product():
    return{"message":"Get products "}

@router.post("/products")
async def create_product():
    return {"message": "Product created"}


@router.put("/products/{id}")
async def update_product(id: int):
    return {"message": f"Product {id} updated"}