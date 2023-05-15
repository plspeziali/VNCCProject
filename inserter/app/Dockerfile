FROM python:3.9

WORKDIR /app

COPY inserter.py ./

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3001

CMD ["python", "inserter.py"]