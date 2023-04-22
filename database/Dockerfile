FROM postgres

# Copia il file di script SQL nella nuova immagine
COPY init.sql /docker-entrypoint-initdb.d/

# Esegui il comando per inizializzare il database con lo script SQL
CMD ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"]