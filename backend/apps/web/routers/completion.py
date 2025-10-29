from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import StreamingResponse
from utils.utils import get_current_user
from apps.web.models.aimodel import AiModelReq, AiResultReq
from apps.web.ai.wave import WaveApiInstance
import json
import time

router = APIRouter()

@router.post("/completion/video")
async def completion_video(param: AiModelReq, user=Depends(get_current_user)):
  def event_generator():
    result = WaveApiInstance.create(param)
    print("=================video-create======================", result)
    if result is not None and result.get('code') == 200:
      requestId = result['data']['id']
      timeout = 0
      while True:
        timeout += 1
        if timeout > 600:
          data = {
            "success": True,
            "message": "timeout",
            "status": "timeout",
            "value": "failed"
          }
          yield f"data: {json.dumps(data)}\n\n"
          break
        result = WaveApiInstance.get_prediction_result(requestId)
        if result.get('success'):
          outer_data = result.get('data', {})
          inner_data = outer_data.get('data', {})
          status = inner_data.get('status', 'unknown')
          if status == 'completed':
            data = {
              "success": True,
              "message": inner_data.get('message', 'success'),
              "status": status,
              "videos": inner_data.get('outputs', [])
            }
            yield f"data: {json.dumps(data)}\n\n"
            break
          else:
            data = {
              "success": True,
              "message": inner_data.get('message', 'success'),
              "status": status,
              "videos": "loading"
            }
            yield f"data: {json.dumps(data)}\n\n"
        # stop 1s
        time.sleep(0.2)
    else:
      data = {
        "success": False,
        "message": "create failed",
        "status": 'failed',
        "videos": ""
      }
      yield f"data: {json.dumps(data)}\n\n"

    yield f"data: [DONE]\n\n"

  return StreamingResponse(event_generator(), media_type="text/event-stream")

@router.post("/video/result")
async def completion_video(param: AiResultReq, user=Depends(get_current_user)):
  result = WaveApiInstance.get_prediction_result(param.requestId)
  return result
