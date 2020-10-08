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
| `/contacts/id/delete`  | Delete (action only, no view)  |

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

1. Go to `localhost:8000/`. You should see a very plain contacts index page, like so: 
![](https://imgur.com/V6SvjaX.png) 
1. Go to `localhost:8000/admin` and log in using the username/password you created when making the superuser 
1. You should now be able to add / delete / edit / read contacts directly from your browser!
    - <details><summary>See an example of how to use the admin panel</summary><p>
    
        ![](https://imgur.com/EROfINH.gif)
    
    </p></details>
    
---


