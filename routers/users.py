from fastapi import APIRouter

router = APIRouter()

@router.get("/users/test", tags=["users"])
async def read_user_me():
    return {"this": "test"}