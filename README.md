# Accuknox

## Installation Steps

1. Clone the repository:
    git clone https://github.com/Rajakuruva/Accoknox_project.git
    cd your-repo-name
    
2. Create a virtual environment and activate it:
    python -m venv venv
    source venv/bin/activate
    
    # On Windows use `venv\Scripts\activate`

3. Install the dependencies:
    pip install -r requirements.txt

4. Apply migrations:
   python manage.py migrate
   python manage.py makemigrations
   python manage.py migrate

5. Create super user for administration
   python manage.py createsuperuser
   #Give username and password after that it will ask "Bypass password validation and create user anyway? [y/N]:" You can give "y"

7. Run the development server:
    python manage.py runserver
