# Django Full CRUD App 

## Description 

This is a single model full CRUD full app for contacts using Python and Django, including Django's built in templating for the views. 

### Contacts Properties: 

|Property  | Type  | Default  |
|---|---|---|
| id | integer | assigned by db |
| name | string | n/a |
| age | integer | n/a |

### Contacts URLS: 

|Endpoint  | View/Action  |
|---|---|
| `/`  | Index |
| `/contacts/:id`  | Show  |
| `/contacts/new`  | Create  |
| `/contacts/:id/edit`  | Edit  |
| `/contacts/:id/delete`  | Delete (action only, no view)  |

## System Requirements 

- Python 3 
- pipenv 

### Installation

If you don't have either of the above, please install them. 

<details><summary>Python3 Installation</summary><p>
    
#### Python Installation

1. Check what python version you have on your computer by running: `python -V`
1. If you're not on a version of Python that is 3 or greater, install python 3 with homebrew:
    - `brew install python3` 
    - Note: in order to use this installed python3, you will have to use `python3` whenever running a python command 
    
</p></details>

<details><summary>pipenv Installation</summary><p>
    
#### pipenv Installation

To build your app, we're going to be building a virtual environment. In order to manage our dependencies and our virtual environment, we're going to use [pipenv](https://pipenv.pypa.io/en/latest/).

1. Check if you have pipenv by running: `pipenv --version` 
1. If you do not have it, install it with homebrew:
    - `brew install pipenv` 
    
</p></details>

---

## Get Set Up Locally 

### On your Browser 

1. Fork this repository to your account 

### In your Terminal 

1. Clone **your fork** of the repo onto your computer anywhere that is not a git repo
1. `cd` into the repo 
1. Touch a `.env` into the root of your project and add a SECRET_KEY value. See the .env.sample file for an example
1. Install all the required packages by running: `pipenv install` 
1. Activate the virtual environment by running: `pipenv shell`
    - NOTE: To exit the shell gracefully whenever you're done working, use `exit`
1. Create the `contacts` psql database and user by running the following while in the pipenv shell: `psql -U postgres -f settings.sql` 
    - You can find the database name and username/password inside the settings.sql file
1. Apply the migrations by running the following while in the pipenv shell: `python3 manage.py migrate`
1. Make a superuser for your app, this will allow you to work directly with your database on the browser without having to use Postman 
    - In the pipenv shell, run `python3 manage.py createsuperuser` and follow the instructions
1. Start the Django server by running the following inside the pipenv shell: `python3 manage.py runserver`  

### On your Browser 

1. Go to `localhost:8000/`. You should see a very plain contacts index page
    - <details><summary>See how it should look</summary><p>
      
        ![](https://imgur.com/Xn0vzRp.png) 
        
      <p></details>
1. You should be able to add data by using the already set up form
    - EXTRA: You can also use the built in django admin panel:
        1. Go to `localhost:8000/admin` and log in using the username/password you created when making the superuser 
        1. You should now be able to add / delete / edit / read contacts directly from your browser!
            - <details><summary>See an example of how to use the admin panel</summary><p>
    
                ![](https://imgur.com/EROfINH.gif)
    
            </p></details>
    
---

## Making Changes 

### Updating / Creating Models 

1. If you make any changes to the `contacts/models.py` file, you will need to make and run a migration to apply the changes. You can do so by using the following commands while _inside the pipenv shell_
    1. Make the migration: `python3 manage.py makemigrations` 
    1. Apply the migration: `python3 manage.py migrate` 
    
---

## Set Up for Heroku Deployment 

### In Terminal
1. Create a heroku app from the root of your project folder, run: `heroku create` 
    - The above command will randomly generate a name for you, if you want to name your app something specific run: `heroku create urlNameYouWantHere`

### In your Code Editor 

1. Copy the heroku url that was created (without the `https://`), go to your `django_contacts/settings.py` and add it into the `ALLOWED_HOSTS`
    - e.g. 
    ![](https://imgur.com/AVlB8kK.png)
    
### On the Browser 

1. Go to your heroku dashboard for the heroku project you just created
1. Click on Configure Add-Ons
1. Search for Heroku Postgres and add it 
1. Go to the Settings, Reveal Config Vars, add a config var for SECRET_KEY and anything else you have in your .env file 

### In Terminal

1. `pipenv lock` to ensure your pipfile.lock is up to date
1. `git add -A`
1. `git commit -m "heroku deployment"`
1. `git push heroku master` 
1. Once it builds successfully, run `heroku run bash` 
1. While in heroku bash,  apply the migrations to the heroku project by running: `python manage.py migrate` 
1. Still in heroku bash, create a superuser for the heroku project by running `python manage.py createsuperuser` and follow the prompts
    - To exit heroku bash, run `exit`

### In Browser 

1. After the migrations finish, you should now be able to open the heroku app in your browser!
1. Remember that your heroku database is separate from your local database, so there should not be any data on the first load. 
    - You can add data by just using the create route / form already there
    - Additionally, you can also log in to `/admin` with the heroku superuser you created
    
---

## Resources 

Django is a fairly opinionated frameworks meaning there are right ways to do things. If you plan on making many changes to this template, I would recommend looking at their documentation: 

- [Django Documentation](https://docs.djangoproject.com/en/3.1/)
    - Particular pages you may want to look at: 
        - [Making Queries (Django's built in ORM)](https://docs.djangoproject.com/en/3.1/topics/db/queries/#)
        - [Models](https://docs.djangoproject.com/en/3.1/topics/db/models/)
        - [Migrations](https://docs.djangoproject.com/en/3.1/topics/migrations/)
        - [URLs Config](https://docs.djangoproject.com/en/3.1/topics/http/urls/)
        - [Templates](https://docs.djangoproject.com/en/3.1/topics/templates/)
        - [The Django Templating Language](https://docs.djangoproject.com/en/3.1/ref/templates/language/)
        - [Writing Views](https://docs.djangoproject.com/en/3.1/topics/http/views/)
        - [Class Based Views](https://docs.djangoproject.com/en/3.1/topics/class-based-views/)
        
