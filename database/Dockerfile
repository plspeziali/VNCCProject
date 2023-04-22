FROM postgres

# Copia il file di script SQL nella nuova immagine
COPY init.sql /docker-entrypoint-initdb.d/

COPY bodyPerformance.csv ./

# Esegui il comando per inizializzare il database con lo script SQL
CMD ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"]