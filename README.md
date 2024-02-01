># `Django With Harry`
>
>![image](https://github.com/imvickykumar999/DjangoWithHarry/assets/50515418/d286b6fe-2230-46c9-b1e3-7f7240a4befa)

<br>

# `Steps to run django project`

```bash
django-admin startproject mysite
# Note: `mysite` is user-defined name
cd mysite

python manage.py migrate
python manage.py createsuperuser --username imvickykumar999 --email imvickykumar999@gmail.com
# Note: `imvickykumar999` and `imvickykumar999@gmail.com` are user-defined names

python manage.py startapp home
# Note: `home` is user-defined name
python manage.py runserver
```

<br>

- `>>>` Starting development server at http://127.0.0.1:8000/

- Copy `urls.py` from `mysite` folder and paste this file in `home` folder.

<br>

>![image](https://github.com/imvickykumar999/DjangoWithHarry/assets/50515418/89b4b2eb-4078-45e2-b676-fcd846ca0003)
