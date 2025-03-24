# 기본 NVIDIA CUDA와 PyTorch 이미지 사용
FROM pytorch/pytorch:2.1.2-cuda11.8-cudnn8-runtime

# 시스템 의존성 설치 (OpenCV 관련 라이브러리는 필요 없음)
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 작업 디렉토리 설정
WORKDIR /app

# requirements.txt 복사 및 의존성 설치
COPY conf/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY app/ /app/

# 모델 파일 복사
COPY weights/ /app/weights/

# FastAPI 실행 포트 노출
EXPOSE 8000

# 애플리케이션 실행 명령어
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
