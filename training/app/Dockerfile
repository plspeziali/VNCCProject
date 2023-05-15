FROM python:3.9

WORKDIR /app

COPY training.py  ./

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3002

CMD ["python", "training.py"]