##  Проект "API_stripe_payment"

### Описание проекта:

Сервер на Django и библиотеке Stripe с двумя эндпойнтами:
```
1)/item/{id} - для просмотра товара
2)/buy/{id} - для получения номера сессии и перенаправления на страницу оплаты
```

```
http://
```

### Технологии:

При реализации бекэнда проекта были использованы следующие основные технологии, фреймворки и библиотеки:
- Python 3
- Django 3.2
- Django Rest FrameWork 3.12.4
- Stripe 4.1.0

### Как запустить проект:
Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone 'ссылка на репозиторий'
```

```
cd API_stripe_payment
```

Cоздайте и активируйте виртуальное окружение:

```
python -m venv venv
```

```
source venv/bin/activate
```
```
python -m pip install --upgrade pip
```

Установите зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполните миграции:

```
python manage.py migrate
```

Создайте .env файл в директории проекта и заполните значения переменных (необходим аккаунт на сайте https://dashboard.stripe.com/):

```
STRIPE_SK=
STRIPE_PK=
```

Запустите проект:

```
python manage.py runserver
```
