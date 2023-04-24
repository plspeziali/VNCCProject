# Usa l'immagine di base python 3.10
FROM python:3.9

# Crea la directory di lavoro dell'applicazione
WORKDIR /app

# Copia il codice dell'applicazione e il modello all'interno della directory di lavoro
COPY inserter.py ./

# Copia il file requirements.txt all'interno della directory di lavoro
COPY requirements.txt ./

# Installa le dipendenze dell'applicazione
RUN pip install --no-cache-dir -r requirements.txt

# Esponi la porta 5000 per la comunicazione dell'applicazione
EXPOSE 3001

# Avvia l'applicazione
CMD ["python", "inserter.py"]