# Usa l'immagine di base python 3.10
FROM python:3.9

# Crea la directory di lavoro dell'applicazione
WORKDIR /app

# Copia il codice dell'applicazione e il modello all'interno della directory di lavoro
COPY initializer.py ./

# Copia il file requirements.txt all'interno della directory di lavoro
COPY requirements.txt ./

# Copia il file requirements.txt all'interno della directory di lavoro
COPY init.sql ./

# Installa le dipendenze dell'applicazione
RUN pip install --no-cache-dir -r requirements.txt

# Avvia l'applicazione
CMD ["python", "initializer.py"]