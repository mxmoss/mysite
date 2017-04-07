# mysite
simple django site using mysql

This is an example of a database-driven Python website.
It allows you to enter people into a contact list.
Roughly based on the [Django Girls tutorial](https://tutorial.djangogirls.org/en/)

It uses the following:
* MySQL
* Python
* Django framework
* The required python libraries are listed in requirements.txt

# Setting up local development
Clone, configure your virtual environment and install requirements:
```
git clone https://github.com/mxmoss/mysite.git
cd mysite
python -m venv mysite
mysite\Scripts\activate
pip install -r requirements.txt
```

If you are configured to use a local database for development you will need to run the migrate scripts. You only need to run this when the models have changed:

python manage.py makemigrations
python manage.py migrate

Run the app server:
python manage.py runserver

