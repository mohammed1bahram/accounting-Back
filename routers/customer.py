from fastapi import APIRouter

router = APIRouter()

@router.get("/customers")
def read_customers():
    return {"message": "List of customers"}
