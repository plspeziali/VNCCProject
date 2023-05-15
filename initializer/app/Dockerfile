FROM python:3.9

WORKDIR /app

COPY initializer.py ./

COPY requirements.txt ./

COPY init.sql ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "initializer.py"]