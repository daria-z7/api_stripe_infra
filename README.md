##  Проект "API_stripe_payment"

### Описание проекта:

Сервер на Django и библиотеке Stripe с двумя эндпойнтами:
```
1)/item/{id} - для просмотра товара
2)/buy/{id} - для получения номера сессии и перенаправления на страницу оплаты
```

Для просмотра запущенного сервера воспользуйтесь данными ссылками:
```
http://158.160.1.54/item/1/
http://158.160.1.54/item/2/
http://158.160.1.54/item/3/
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
Создайте файл .env в папке infra и пропишите в нем переменные окружения следующим образом:

```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME= # имя базы данных
POSTGRES_USER= # логин для подключения к базе данных
POSTGRES_PASSWORD= # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
URL_PATH = хост, на котором вы будете запускать сервер
STRIPE_SK= secret key (необходим аккаунт на сайте https://dashboard.stripe.com/)
STRIPE_PK= public key (необходим аккаунт на сайте https://dashboard.stripe.com/

```
Из папки, в которой находится файл docker-compose.yaml выполните сборку контейнеров с помощью команды:

```
sudo docker-compose up -d --build 
```

Выполните миграции:

```
sudo docker-compose exec web python manage.py migrate 
```

Создайте суперпользователя:

```
sudo docker-compose exec web python manage.py createsuperuser
```

Соберите статику:

```
sudo docker-compose exec web python manage.py collectstatic --no-input  
```

Войдите в админку:

```
http://localhost/admin/
```
