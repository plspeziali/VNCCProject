FROM python:3.9

WORKDIR /app

COPY predictor.py ./

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "predictor.py"]