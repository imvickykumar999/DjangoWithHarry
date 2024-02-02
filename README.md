># `Deployed` : [`DjangoWithHarry`](https://djangowithharry.pythonanywhere.com/)
>
>![image](https://github.com/imvickykumar999/DjangoWithHarry/assets/50515418/da4a0116-f50d-4315-af3c-14d298d383fa)
>![image](https://github.com/imvickykumar999/DjangoWithHarry/assets/50515418/b8913c19-7778-493a-84d4-a9dc2240e6b7)

<br>

# `Steps to run django project`

```bash
django-admin startproject mysite
# Note: `mysite` is user-defined name
cd mysite

# https://stackoverflow.com/ai/search/34258
python manage.py makemigrations
python manage.py migrate

# python manage.py createsuperuser
python manage.py createsuperuser --username imvickykumar999 --email imvickykumar999@gmail.com
# Note: `imvickykumar999` and `imvickykumar999@gmail.com` are user-defined names

python manage.py startapp home
# Note: `home` is user-defined name
python manage.py runserver
```

- `>>>` Starting development server at http://127.0.0.1:8000/

- Copy `urls.py` from `mysite` folder and paste this file in `home` folder.

<br><br>

># `Folder Structure`
>
>![image](https://github.com/imvickykumar999/DjangoWithHarry/assets/50515418/89b4b2eb-4078-45e2-b676-fcd846ca0003)
>![image](https://github.com/imvickykumar999/DjangoWithHarry/assets/50515418/123e454d-987b-4f22-b547-070fa5fe3811)
