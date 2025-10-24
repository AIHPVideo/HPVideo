import os
import requests
import cv2
import numpy as np
from apps.web.models.aimodel import AiModelReq


wave_url = os.getenv("WAVESPEED_URL")
wave_key = os.getenv("WAVESPEED_KEY")


class WaveApi:
    
	def check_model(self, model: str):
		models = ["wan-2.5"]
		return model in models

	# Create Video ID      
	def create(self, param: AiModelReq):
		headers = {
			"Authorization": f'Bearer {wave_key}',
			"Content-Type": "application/json"
		}
		last_message = param.messages[-1]
		data = {
			"duration": param.duration,
			"prompt": last_message.get("content"),
			"size": param.size
		}
		if param.image is not None and param.image.strip() != "":
			data["image"] = param.image

		try:
			url = f'{wave_url}/{param.source}/{param.model}'
			response = requests.post(url, json=data, headers=headers)
			response.raise_for_status()
			return response.json()
		except Exception as e:
			print(f"Request Err: {e}")
			return None

	# Get Video By Video ID	
	def get_prediction_result(self, requestId: str):
		url = f"{wave_url}/predictions/{requestId}/result"
		headers = {
			"Authorization": f"Bearer {wave_key}"
		}
		try:
			response = requests.get(url, headers=headers)
			response.raise_for_status()
			return {
				"success": True,
				"data": response.json()
			}	
		except requests.exceptions.HTTPError as e:
			return {
				"success": False,
				"error": f"HTTP Err: {str(e)}",
				"status_code": response.status_code,
				"response_text": response.text
			}
		except requests.exceptions.RequestException as e:
			return {
				"success": False,
				"error": f"Err: {str(e)}"
      }

WaveApiInstance = WaveApi()
