from fastapi import FastAPI, File, UploadFile
from io import BytesIO
import torch
from PIL import Image
import numpy as np
from pathlib import Path
from ultralytics import YOLO

# FastAPI 앱 생성
app = FastAPI()

# 모델 경로 설정 (yolov8n.pt는 차량, best.pt는 번호판 탐지)
vehicle_model_path = "weights/yolov8n.pt"
plate_model_path = "weights/best.pt"

# YOLO 모델을 로드하는 함수 (Torch 모델)

def load_model(model_path: str):
    model = YOLO(model_path)  # YOLOv8 모델 로드
    return model

# 모델을 메모리에 로드 (차량 모델과 번호판 모델)
vehicle_model = load_model(vehicle_model_path)
plate_model = load_model(plate_model_path)

@app.get("/test")
def read_root():
    return {"message": "Hello World"}
