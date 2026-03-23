
# Programación Paralela y Concurrente - Tarea 6 
```bash
# 1. Levantar contenedor de PostgreSQL con terminal
    docker run --name sqltutorial -e POSTGRES_PASSWORD=supersecret -e POSTGRES_USER=postgres -p 5432:5432 -d postgres

# 2. Levantar contenedor de pgAdmin desde terminal
    docker run --name pgadmin-container -p 5050:80 -e PGADMIN_DEFAULT_EMAIL=user@domain.com -e PGADMIN_DEFAULT_PASSWORD=supersecret -d dpage/pgadmin4

# 3. Crear red de Docker y conectar contenedores desde terminal
    docker network create my-db-network
    docker network connect my-db-network sqltutorial
    docker network connect my-db-network pgadmin-container

## 4. Crear las bases de datos desde terminal
    docker exec -it sqltutorial psql -U postgres -c "CREATE DATABASE db_alternativa01;"

    docker exec -it sqltutorial psql -U postgres -c "CREATE DATABASE db_alternativa02;"

# 5. Tabla para Alternativa 01 desde terminal
docker exec -it sqltutorial psql -U postgres -d db_alternativa01 -c "
    CREATE TABLE IF NOT EXISTS inversiones (
        id SERIAL PRIMARY KEY,
        symbol VARCHAR(10),
        price VARCHAR(20),
        register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );"

# 6. Tabla para Alternativa 02
docker exec -it sqltutorial psql -U postgres -d db_alternativa02 -c "
    CREATE TABLE IF NOT EXISTS inversiones (
        id SERIAL PRIMARY KEY,
        symbol VARCHAR(10),
        price VARCHAR(20),
        register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );"

# 7. Ejecutar los códigos desde terminal 
    python3 "Alternativa01.py"

    python3 "Alternativa02.py"
