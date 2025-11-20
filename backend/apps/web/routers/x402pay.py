from typing import Any, Dict
from fastapi import APIRouter, Request
from cdp.x402 import create_facilitator_config
from x402.fastapi.middleware import require_payment
from apps.web.models.pay import PayTableInstall
from apps.web.ai.wave import WaveApiInstance
import uuid
import os

router = APIRouter()

COINBASE_KEY = os.getenv("COINBASE_KEY")
COINBASE_SECRET = os.getenv("COINBASE_SECRET")
COINBASE_ADDRESS = os.getenv("COINBASE_ADDRESS")
BASE_URL = os.getenv("BASE_URL")

facilitator_config = create_facilitator_config(
    api_key_id= COINBASE_KEY,
    api_key_secret= COINBASE_SECRET
)

amounts = {
  "wan-2.5": {
    "480": {"5": 0.375, "10": 0.75},
    "720": {"5": 0.75, "10": 1.5}, 
    "1080": {"5": 1.125, "10": 2.25}
  },
  "sora-2": {
    "720": {"4": 0.45, "8": 1.35, "12": 2.7}
  },
  "ovi": {
    "540": {"10": 0.45, "30": 1.35, "60": 2.7}
  },
  "veo3.1": {
    "*": {"4": 2.4, "6": 3.6, "8": 4.8}
  },
  "ltx-2-pro": {
    "*": {"6": 0.54, "8": 0.72, "10": 0.9}
  },
  "hailuo-02": {
    "*": {"6": 0.345, "10": 0.84}
  },
  "seedance": {
    "*": {"6": 0.27, "9": 0.405, "12": 0.54}
  },
  "kling": {
    "*": {"5": 1.95, "10": 3.9}
  },
  "pixverse": {
    "*": {"5": 0.525, "8": 1.05}
  }
}

# Define an outer middleware
async def payment_middleware(request: Request, call_next):
    # Only effective for the target path
    if request.url.path == "/creator/api/v1/x402/creator/wan2.5_480_5":
        # Calculate the price
        price = calTotal("wan2.5", "480", "5")
        
        # Call require_payment middleware
        inner_middleware = require_payment(
            path="/creator/api/v1/x402/creator/wan2.5_480_5",
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
    
    if request.url.path == "/creator/api/v1/x402/creator/wan2.5_480_10":
        # Calculate the price
        price = calTotal("wan2.5", "720", "10")
        
        # Call require_payment middleware
        inner_middleware = require_payment(
            path="/creator/api/v1/x402/creator/wan2.5_480_10",
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
    
    # Only effective for the target path
    if request.url.path == "/creator/api/v1/x402/creator/wan2.5_720_5":
        # Calculate the price
        price = calTotal("wan2.5", "720", "5")
        
        # Call require_payment middleware
        inner_middleware = require_payment(
            path="/creator/api/v1/x402/creator/wan2.5_720_5",
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
    
    if request.url.path == "/creator/api/v1/x402/creator/wan2.5_720_10":
        # Calculate the price
        price = calTotal("wan2.5", "720", "5")
        
        # Call require_payment middleware
        inner_middleware = require_payment(
            path="/creator/api/v1/x402/creator/wan2.5_720_10",
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
    
    # Only effective for the target path
    if request.url.path == "/creator/api/v1/x402/creator/wan2.5_1080_5":
        # Calculate the price
        price = calTotal("wan2.5", "1080", "5")
        
        # Call require_payment middleware
        inner_middleware = require_payment(
            path="/creator/api/v1/x402/creator/wan2.5_1080_5",
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
    
    if request.url.path == "/creator/api/v1/x402/creator/wan2.5_1080_10":
        # Calculate the price
        price = calTotal("wan2.5", "1080", "5")
        
        # Call require_payment middleware
        inner_middleware = require_payment(
            path="/creator/api/v1/x402/creator/wan2.5_1080_10",
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
    
    # Only effective for the target path
    if request.url.path == "/creator/api/v1/x402/creator/sora-2_720_4":
        # Calculate the price
        price = calTotal("sora-2", "720", "4")
        
        # Call require_payment middleware
        inner_middleware = require_payment(
            path="/creator/api/v1/x402/creator/sora-2_720_4",
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
    if request.url.path == "/creator/api/v1/x402/creator/sora-2_720_8":
        # Calculate the price
        price = calTotal("sora-2", "720", "8")
        
        # Call require_payment middleware
        inner_middleware = require_payment(
            path="/creator/api/v1/x402/creator/sora-2_720_8",
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
    if request.url.path == "/creator/api/v1/x402/creator/sora-2_720_12":
        # Calculate the price
        price = calTotal("sora-2", "720", "12")
        
        # Call require_payment middleware
        inner_middleware = require_payment(
            path="/creator/api/v1/x402/creator/sora-2_720_12",
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

def calTotal(model: str, key: str, duration, size: str):
    address = "wallet_x402pay"
    messageid = str(uuid.uuid4())
    amount_dict = amounts.get(model)
    amount = "$0.02"
    if model is not None and messageid is not None:
        for key in amount_dict:
          if size.find(key) != -1:
              amount = f"${amount_dict.get(key).get(str(duration))}"
        pay = PayTableInstall.get_by_messageid(messageid)
        if pay is None:
            PayTableInstall.insert_pay(address, model, size, duration, amount, messageid) 
    return amount

@router.get("/test/creator/wan2.5_480_5")
async def get_param(model: str, messageid: str) -> Dict[str, Any]:
    pay = PayTableInstall.get_by_messageid(messageid)
    if pay is not None:
        PayTableInstall.update_status(pay.id, True)
    result = WaveApiInstance.x402create("alibaba", "wan-2.5/text-to-video", "美食分享", 5, "832*480")
    if result is not None and result.get('code') == 200:
        requestId = result['data']['id']

    return {
        "success": True,
        "model": model,
        "path": f"{BASE_URL}?createid={requestId}"
    }

@router.get("/creator/wan2.5_480_10")
async def get_param(model: str, messageid: str) -> Dict[str, Any]:
    pay = PayTableInstall.get_by_messageid(messageid)
    if pay is not None:
        PayTableInstall.update_status(pay.id, True)
    return {
        "model": model,
        "messageid": messageid
    }

@router.get("/creator/wan2.5_720_5")
async def get_param(model: str, messageid: str) -> Dict[str, Any]:
    pay = PayTableInstall.get_by_messageid(messageid)
    if pay is not None:
        PayTableInstall.update_status(pay.id, True)
    return {
        "model": model,
        "messageid": messageid
    }

@router.get("/creator/wan2.5_720_10")
async def get_param(model: str, messageid: str) -> Dict[str, Any]:
    pay = PayTableInstall.get_by_messageid(messageid)
    if pay is not None:
        PayTableInstall.update_status(pay.id, True)
    return {
        "model": model,
        "messageid": messageid
    }

@router.get("/creator/wan2.5_1080_5")
async def get_param(model: str, messageid: str) -> Dict[str, Any]:
    pay = PayTableInstall.get_by_messageid(messageid)
    if pay is not None:
        PayTableInstall.update_status(pay.id, True)
    return {
        "model": model,
        "messageid": messageid
    }

@router.get("/creator/wan2.5_1080_10")
async def get_param(model: str, messageid: str) -> Dict[str, Any]:
    pay = PayTableInstall.get_by_messageid(messageid)
    if pay is not None:
        PayTableInstall.update_status(pay.id, True)
    return {
        "model": model,
        "messageid": messageid
    }

@router.get("/creator/sora-2_720_4")
async def get_param(model: str, messageid: str) -> Dict[str, Any]:
    pay = PayTableInstall.get_by_messageid(messageid)
    if pay is not None:
        PayTableInstall.update_status(pay.id, True)
    return {
        "model": model,
        "messageid": messageid
    }
@router.get("/creator/sora-2_720_8")
async def get_param(model: str, messageid: str) -> Dict[str, Any]:
    pay = PayTableInstall.get_by_messageid(messageid)
    if pay is not None:
        PayTableInstall.update_status(pay.id, True)
    return {
        "model": model,
        "messageid": messageid
    }
@router.get("/creator/sora-2_720_12")
async def get_param(model: str, messageid: str) -> Dict[str, Any]:
    pay = PayTableInstall.get_by_messageid(messageid)
    if pay is not None:
        PayTableInstall.update_status(pay.id, True)
    return {
        "model": model,
        "messageid": messageid
    }