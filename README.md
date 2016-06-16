#Setup

* Clone project
* Create a virtual env

        mkvirtualenv exmaster
    
* Install requirements

        pip install -r requirements.txt

* Create a `exmaster/local_settings.py` file:

        DEBUG = True
        SECRET_KEY = "kjagfkafjhdgfgf"
    
* Create DB

        python manage.py migrate

* Create Superuser

        python manage.py createsuperuser

* Generate content

        python manage.py generate_blog_content

