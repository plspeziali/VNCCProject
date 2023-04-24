FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install jupyter

COPY Classifier.ipynb /app/

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"] 

EXPOSE 8888/tcp

# docker build -t myproject .
# docker run -p 8888:8888 myproject