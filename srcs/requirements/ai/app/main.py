from fastapi import FastAPI, File, UploadFile
from io import BytesIO
import torch
from PIL import Image
import numpy as np
from pathlib import Path

# FastAPI 앱 생성
app = FastAPI()

# 모델 경로 설정 (yolov8n.pt는 차량, best.pt는 번호판 탐지)
vehicle_model_path = "weights/yolov8n.pt"
plate_model_path = "weights/best.pt"

# YOLO 모델을 로드하는 함수 (Torch 모델)
def load_model(model_path: str):
    # 모델을 Torch로 로드
    model = torch.hub.load('ultralytics/yolov5:v6.0', 'custom', path=model_path)
    return model

# 모델을 메모리에 로드 (차량 모델과 번호판 모델)
vehicle_model = load_model(vehicle_model_path)
plate_model = load_model(plate_model_path)

@app.get("/test")
def read_root():
    return {"message": "Hello World"}

# # 이미지 업로드 및 차량, 번호판 탐지 엔드포인트
# @app.post("/detect")
# async def detect_objects(file: UploadFile = File(...)):
#     # 이미지 파일을 BytesIO 객체로 읽기
#     image_bytes = await file.read()
#     image = Image.open(BytesIO(image_bytes))
    
#     # 이미지를 numpy 배열로 변환
#     img_array = np.array(image)
    
#     # 차량 탐지 (vehicle_model)
#     vehicle_results = vehicle_model(img_array)
#     vehicle_detected = vehicle_results.pandas().xywh[vehicle_results.pandas().columns[0] == 'car']
    
#     # 번호판 탐지 (plate_model)
#     plate_results = plate_model(img_array)
#     plate_detected = plate_results.pandas().xywh[plate_results.pandas().columns[0] == 'license plate']
    
#     # 결과를 JSON 형식으로 반환
#     return {
#         "vehicle_detected": vehicle_detected.to_dict(orient="records"),
#         "plate_detected": plate_detected.to_dict(orient="records")
#     }

