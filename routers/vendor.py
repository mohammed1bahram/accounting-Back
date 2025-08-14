from fastapi import APIRouter

router = APIRouter()

@router.get("/vendors")
def read_vendors():
    return {"message": "List of vendors"}
