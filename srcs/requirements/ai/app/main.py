from fastapi import FastAPI, File, UploadFile
from io import BytesIO
import torch
from PIL import Image
import numpy as np

# # YOLO 모델 로드 클래스 정의
# class YOLOModel:
#     def __init__(self, vehicle_model_path: str, plate_model_path: str):
#         # 차량 탐지 모델 (yolov8n.pt)
#         self.vehicle_model = torch.hub.load('ultralytics/yolov5', 'custom', path=vehicle_model_path)
#         # 번호판 탐지 모델 (best.pt)
#         self.plate_model = torch.hub.load('ultralytics/yolov5', 'custom', path=plate_model_path)

#     def predict_vehicle(self, img: np.array):
#         # 차량 탐지
#         results = self.vehicle_model(img)
#         predictions = results.pandas().xywh[0].to_dict(orient="records")
#         return predictions

#     def predict_plate(self, img: np.array):
#         # 번호판 탐지
#         results = self.plate_model(img)
#         predictions = results.pandas().xywh[0].to_dict(orient="records")
#         return predictions

# FastAPI 앱 생성
app = FastAPI()

# 모델 경로 설정 (yolov8n.pt는 차량, best.pt는 번호판 탐지)
vehicle_model_path = "weights/yolov8n.pt"
plate_model_path = "weights/best.pt"
# yolo_model = YOLOModel(vehicle_model_path, plate_model_path)

@app.get("/test")
def read_root():
    return {"message": "Hello World"}

# # 이미지 처리 및 예측 엔드포인트
# @app.post("/predict/")
# async def predict(file: UploadFile = File(...)):
#     # 이미지 파일 읽기
#     image_data = await file.read()
#     image = Image.open(BytesIO(image_data))

#     # 이미지 배열로 변환
#     img = np.array(image)

#     # 차량 탐지
#     vehicle_predictions = yolo_model.predict_vehicle(img)

#     # 번호판 탐지
#     plate_predictions = yolo_model.predict_plate(img)

#     # 결과 반환
#     return {
#         "vehicle_predictions": vehicle_predictions,
#         "plate_predictions": plate_predictions
#     }
