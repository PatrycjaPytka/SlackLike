# Communicator Application

Django web application for chatting. It requires user to create an account and have access to groups. Only user with staff permissions can create, edit or delete group and add users to it. 
Users can chat with each other and create private conversations.

## Running

1. Install virtual environment:
* `pip3 install virtualenv`
* `python3 -m venv "venv"`
* `git clone <repo_url_from_git>`
* `venv\Scripts\activate`
> Note: There is no obligation to create a virtual environment. If we don't, remember to always use the formula 'python3' instead of 'python'.
2. Remember to make migrations and migrate:
* `python manage.py makemigrations`
* `python manage.py migrate`

3. Install Channels:
* python -m pip install -U channels 
* docker run -p 6379:6379 -d redis:5
> Application is using Docker which uses Redis as its backing store. It is needed to install channel_redis by running command: `python -m pip install channels_redis`

## Structure

Main app:
chat_main -> Channels handling (Message sending/Creation, deletion, edition channels/Searching for channels)

chat_main/templates/chat_main -> HTML files templates

User app:
chat_login -> User login app (Login/Sign up/Log out)
chat_login/templates/chat_login -> HTML files templates
chat_login/static/chat_login -> static files (css)
