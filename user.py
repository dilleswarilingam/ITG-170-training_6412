from fastapi import APIRouter

router = APIRouter()


@router.get("/users")
async def get_users():
    return {"message": "Get users"}


@router.post("/users")
async def create_user():
    return {"message": "User created"}

@router.put("/users/{id}")
async def update_user(id: int):
    return {"message": f"User {id} updated"}

@router.delete("/users/{id}")
async def delete_user(id: int):
    return {"message": f"User {id} deleted"}