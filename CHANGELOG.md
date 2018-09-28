# Dependencies
```txt
dj-database-url==0.3.0 => 0.5.0
    - helps configure the DB connection
django==1.8.3 => 2.1.1
    - Web framework!
    -REQUIRES PYTHON3.4 +
django-bootstrap3==6.1.0 => 11.0.0
    - CSS Bootstrap for Django
django-grappelli==2.7.1 =>
    - Only release that supports django2.0+
    - Replacement for the built-in Admin console
django-localflavor==1.1 => 2.1
    - Location and currency data standards
django-registration-redux==1.2 => 2.4
    - Registration process - no support for Django2.1 (TBD)
djangorestframework==3.2.0 =>  3.8.0
    - API Framework for building restful endpoints in Django
factory-boy==2.5.2 => 2.11.1
    - Does not support Python3.7 or Django2.1
    - Provides fake data for testing!
fake-factory==0.5.2 => DEPRECATED!
    - Is now Faker (Faker is installed with Factory-Boy)
Pillow==2.9.0 => 5.2.0
    - Imaging Library for supporting image file management in Python
psycopg2==2.6.1 => 2.7.5
    - Postgres adapter for python
    - We need psycopg1-binary with this
requests==2.7.0 => 2.19.1
    - Send HTTP requests from within our code
selenium==2.47.1 => 3.14.1
    - Headless browser drivers for scripted e2e testing
splinter==0.7.3 => 0.9.0
    - Testing tool for findingelements, events, etc
wheel==0.24.0 => 0.31.1
    - Package distribution and installation
```
