# Blog
A simple django-based blog website

Database used: sqlite3

Requirements:
- Python 3.6
- Django 2.1.1
- CrsipyForms (`pip install django-crispy-forms`)
- Coverage (`pip install coverage==3.6 `)

## Procedure to Setup

1. Clone the repository using:  `git clone https://github.com/sarthak-srivastava/Blog.git`
2. Change to the cloned directory
3. Make migrations using `python manage.py makemigrations`
4. Migrate using `python manage.py migrate`
5. Run the server locally on your machine using `python manage.py runserver`
6. To run test script, run `coverage run manage.py test blogapp -v 2`

