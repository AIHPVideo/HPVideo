from typing import Any, Dict
from fastapi import APIRouter, Request
from cdp.x402 import create_facilitator_config
from x402.fastapi.middleware import require_payment
from apps.web.models.pay import PayTableInstall
import os

router = APIRouter()

COINBASE_KEY = os.getenv("COINBASE_KEY")
COINBASE_SECRET = os.getenv("COINBASE_SECRET")
COINBASE_ADDRESS = os.getenv("COINBASE_ADDRESS")

facilitator_config = create_facilitator_config(
    api_key_id= COINBASE_KEY,
    api_key_secret= COINBASE_SECRET
)

# Define an outer middleware
async def payment_middleware(request: Request, call_next):
    # Only effective for the target path
    if request.url.path == "/creator/api/v1/x402/creator":
        # Calculate the price
        price = calTotal(request)
        
        # Call require_payment middleware
        inner_middleware = require_payment(
            path="/creator/api/v1/x402/creator",
            price=price,
            pay_to_address=COINBASE_ADDRESS,
            network="base",
            facilitator_config=facilitator_config
        )
        # Execute the inner middleware
        response = await inner_middleware(request, call_next)
        
        # add cache control headers to disable caching
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response
    
    # Non-target paths are directly allowed through
    return await call_next(request)

def calTotal(request: Request):
    query_params = request.query_params
    model = query_params.get("model")
    messageid = query_params.get("messageid")
    if model is not None and messageid is not None:
        pay = PayTableInstall.get_by_messageid(messageid)
        if pay is None:
            PayTableInstall.insert_pay("123123123", model, "12*12", 10, "$0.02", messageid) 
    return "$0.02"

@router.get("/creator")
async def get_param(model: str, messageid: str) -> Dict[str, Any]:
    pay = PayTableInstall.get_by_messageid(messageid)
    if pay is not None:
        PayTableInstall.update_status(pay.id, True)
    return {
        "model": model,
        "messageid": messageid
    }