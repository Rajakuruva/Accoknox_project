# Accuknox Project

## Installation Steps

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Rajakuruva/Accoknox_project.git
    cd Accoknox_project
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser for administration:**
    ```sh
    python manage.py createsuperuser
    ```
    Follow the prompts to set the username and password. When asked `Bypass password validation and create user anyway? [y/N]:`, you can type `y`.

6. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

## Dockerization

### Docker Setup

1. **Build and run the Docker containers:**
    ```sh
    docker-compose build
    docker-compose up
    ```

2. **Access the application:**
    - The application will be available at `http://localhost:8000`.
    - The admin interface can be accessed at `http://localhost:8000/admin`.

### Database Configuration

If you want to change the database, you can modify the `docker-compose.yml` and `settings.py` files.

**Example `docker-compose.yml` for PostgreSQL:**

```yaml
version: '3'

services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db

  db:
    image: postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: mydatabase
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword

volumes:
  postgres_data:

In settings.py file - "
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'db',
        'PORT': '5432',
    }
}
"
