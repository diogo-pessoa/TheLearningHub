
### Heroku Deployment

#### [Python Django app in Heroku](https://devcenter.heroku.com/articles/deploying-python)
   
This Project main repo in GitHub is linked to heroku and automatic deploys is enabled. Hence, when a commit reaches master. It will automatically release a new version to the Staging environment 

### Before you create the App:
  Heroku requires some basic files and dependencies to be available in order to run the app, those are:

  - **requirements.txt**
    - gunicorn (Webserver)
    - dj_database_url  (Support for django and Postgres as backend)
    - psycopg2-binary (Support for django and Postgres as backend)
  - [Procfile](Procfile)
  - Update Settings.py
    - `import dj_database_url` Add database config to load DATABASE_URL from HEROKU config_vars


#### Steps to create and setup App:
- `Login` to heroku [login](https://id.heroku.com/login)
- On `Dashboard`  click on create a new pipeline [image](readme_resources/heroku_images_deploy/create_pipeline.png)
  - On this page you set the GitHub repo as a source for this pipeline
- Once pipeline is ready `Add an App in Staging` Add information related to your app [image](readme_resources/heroku_images_deploy/staging_prod_apps_in_pipeline.png)
- On tab `Deploy` Enable automatic Deploy from main branch [image](readme_resources/heroku_images_deploy/automatic_deploy.png)
- Until project  is ready for launch, in `app the-learning-hub-prod -> settings` and set it to maintenance mode(offline) [image](readme_resources/heroku_images_deploy/set-production-app-to-maintenance.png)
- On tab `Settings` Setup Config Vars with environment variables [image](readme_resources/heroku_images_deploy/config_vars.png) 
  - Add a **SECRET_KEY** (django key)
  - **MAIL_USER** (smtp config) to allow app to send emails
  - **MAIL_PASSWORD** (smtp config)
  - _note:_ the postgres url will already be set on the app as **DATABASE_URL**
- Check Logs through the UI [image](https://github.com/diogo-pessoa/the-bookshelf/blob/master/readme-content/heroku-deploy/check_log_UI.png)
    - or CLI: `#heroku logs --tail --app the-learning-hub-staging`
      
#### Setup database connection:

[dj-database-url](https://pypi.org/project/dj-database-url/)

    DATABASES = {
        'default': dj_database_url.parse(os.environ['DATABASE_URL']),
    }
    

### Run Migration on Staging database and initial app setup: 
  Running a migration on Staging environment

- temporarily load the environment variable `DATABASE_URL` with your staging environment database url. 
  
  - `python3 manage.py showmigrations` to make sure manage.py is able to reach the DB.
  - `python3 manage.py migrate`
  
- Create superuser
  - `python3 manage.py createsuperuser`


### STATIC_ROOT Setup in production (DEBUG disabled)

    From browser console
        GEThttps://the-learning-hub-staging.herokuapp.com/static/js/materialize.min.js
    [HTTP/1.1 404 Not Found 23ms]
    The resource from “https://the-learning-hub-staging.herokuapp.com/static/js/materialize.min.js” was blocked due to MIME type (“text/html”) mismatch (X-Content-Type-Options: nosniff).

- STATIC_CONTENT in Heroku 
- Using [whitenoise](https://warehouse.python.org/project/whitenoise/) 

### Stripe Setup

    - Export stripe keys: STRIPE_SECRET_KEY & STRIPE_PUBLISHABLE_KEY
    - If if it's the first time you setup the application (run migrate), then you'll be required to add the subscription and product information to the Product Model.