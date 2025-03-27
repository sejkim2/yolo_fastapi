from fastapi import FastAPI, File, UploadFile
from io import BytesIO
import torch
from PIL import Image
import numpy as np
from pathlib import Path
import sys

# 로컬 YOLO 모델이 있는 디렉토리를 파이썬 경로에 추가
sys.path.append(str(Path(__file__).resolve().parent / 'YOLO8' / 'ultralytics'))

# YOLO 클래스는 수정하지 않았으므로 그대로 가져오기
from ultralytics import YOLO

# FastAPI 앱 생성
app = FastAPI()

# 모델 경로 설정 (yolov8n.pt는 차량, best.pt는 번호판 탐지)
vehicle_model_path = "weights/yolov8n.pt"
plate_model_path = "weights/best.pt"

# YOLO 모델 로드 함수
def load_model(model_path: str):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = YOLO(model_path).to(device)  # GPU가 있으면 GPU로, 없으면 CPU로
    return model

# 모델을 메모리에 로드 (차량 모델과 번호판 모델)
vehicle_model = load_model(vehicle_model_path)
plate_model = load_model(plate_model_path)

@app.get("/test")
def read_root():
    return {"message": "Hello World!"}

