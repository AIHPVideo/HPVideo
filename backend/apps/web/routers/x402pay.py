from typing import Any, Dict
from fastapi import APIRouter

# 
router = APIRouter()

@router.get("/creator")
async def get_param(model: str, messageid: str) -> Dict[str, Any]:
    return {
        "message": "pay success",
        "model": model,
        "messageid": messageid
    }