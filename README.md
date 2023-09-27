# Wagtail template: Your first Wagtail site

A Wagtail project starter template – with the solution to Wagtail’s official [Your first Wagtail site](https://docs.wagtail.org/en/stable/getting_started/tutorial.html) tutorial.

## Starting a new project

```bash
wagtail start mysite --template=https://github.com/thibaudcolas/wagtail-tutorial-template/archive/main.zip
```

## Full starting instructions

For macOS / Linux:

```bash
python -m venv mysite/env
source mysite/env/bin/activate
pip install wagtail

wagtail start mysite --template=https://github.com/thibaudcolas/wagtail-tutorial-template/archive/main.zip

cd mysite
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
