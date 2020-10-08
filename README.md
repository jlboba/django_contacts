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
