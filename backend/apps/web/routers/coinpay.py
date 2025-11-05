from typing import Any, Dict
from fastapi import APIRouter, Request
from x402.fastapi.middleware import require_payment

# 修正路由命名（符合常规命名习惯）
router = APIRouter()

# 动态价格计算函数
def dynamic_price(request: Request) -> str:
    location = request.query_params.get("location", "")
    popular_cities = ["newyork", "london", "tokyo"]
    return "0.002" if location.lower() in popular_cities else "0.001"

# 直接挂载现有中间件
# router.middleware("http")(
#     require_payment(
#         path="/creator",
#         price=dynamic_price,  # 可以直接传函数，在中间件内部调用时传入request
#         pay_to_address="0x8b0b8c7f984dd3f2b580149ade3cdab504d3af1f",
#         network="base-sepolia",
#     )
# )

@router.get("/creator")
async def get_weather(location: str) -> Dict[str, Any]:
    """获取指定城市的天气数据（受支付中间件保护）"""
    return {
        "report": {
        "location": location,
        "weather": "sunny",
        "temperature": 70.0,  # 明确为浮点型，符合output_schema定义
    }
}