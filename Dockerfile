FROM python:3.10-slim 
#  python 3.10 이미지를 사용할 겁니다.

WORKDIR /app
#  app 폴더를 작업 디렉토리로 설정합니다.

COPY requirements.txt /app/
#  requirements.txt 파일을 복사합니다.
RUN pip install --no-cache-dir -r requirements.txt
#  requirements.txt 파일을 설치합니다.

COPY . /app
#  . 폴더를 복사합니다.

EXPOSE 8081
#  8081 포트를 열어줍니다.

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081", "--reload"]
#  uvicorn을 실행합니다.
