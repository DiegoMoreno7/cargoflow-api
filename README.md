# CargoFlow API

Microservicio interno de logística para gestionar envíos.

## Stack

- Python 3.11+
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite en desarrollo / PostgreSQL en producción

## Onboarding local

1. Crear y activar el entorno virtual:

   ```powershell
   py -3.11 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Instalar dependencias:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. Configurar variables de entorno:

   ```powershell
   Copy-Item .env.example .env
   ```

4. Inicializar la base de datos con Flask-Migrate:

   ```powershell
   flask db init
   flask db migrate -m "create shipments table"
   flask db upgrade
   ```

5. Levantar el servidor:

   ```powershell
   flask run
   ```

6. Verificar el endpoint base:

   ```powershell
   curl http://127.0.0.1:5000/api/v1/shipments
   ```

## Git Flow

1. Inicializar el repositorio:

   ```powershell
   git init -b main
   ```

2. Crear el commit base en `main`:

   ```powershell
   git add .
   git commit -m "chore: bootstrap cargoflow api"
   ```

3. Crear la rama de desarrollo:

   ```powershell
   git switch -c develop
   ```

4. Publicar `main` y `develop` en GitHub:

   ```powershell
   git remote add origin https://github.com/TU_USUARIO/cargoflow-api.git
   git push -u origin main
   git push -u origin develop
   ```

