# Тестовое задание на позицию инженера по автоматизации

## Стартовые настройки

Далее приведена инструкция для локального запуска проекта.

1. Подготовка виртуального окружения

Зайдите в директорию `backend/` и создайте виртуальное окружение:

`python -m venv Venv`

Далее перейдите в директорию `backend/src` и установите все зависимости:

`pip install -r requirements.txt`

Теперь активируйте виртуальное окружение:

`cd ..`

`source Venv/bin/activate`

Виртуальное окружение готово

2. Найтройка `.env` файла и базы данных

В файле `.env.example` есть пример того, как должен выглядеть файл `.env`. Достаточно просто создать в директории `backend/src` файл `.env` и скопировать в него содержанимое файла `.env.example`, при этом ****раскоментировав его****. В этом случае все команды далее никак не изменятся.

Подготовка базы данных требует установленного PostgreSQL. Если сервис PostgreSQL установлен и запущен, то подключитесь к нему от имени пользователя postgres:

`sudo -i -u postgres psql`

Далее откроется интерфейс утилиты `psql`, в которой нужно будет создать пользователя, создать базу данных и отдать ее этому пользователю. Если вы не меняли `.env`, эти шаги будут выглядеть так:

`postgres=# create database database;`

`CREATE DATABASE`

`postgres=# create user admin with encrypted password 'admin';`

`CREATE ROLE`

`postgres=# grant all privileges on database database to admin;`

`GRANT`

`postgres=# alter database database owner to admin;`

`ALTER DATABASE`

Здесь создан пользователь `admin` с паролем `admin` и база данных `database`.

Теперь, когда база данных готова, нужно накатить необходимые таблицы. Сделаем это с помощью пакета для контроля миграций `alembic`. Нужно удалить все миграции из каталога `backend/src/alembic/versions` и выполнить в каталоге `backend/src` команды (создание миграции и ее применение):

`alembic revision --autogenerate`

`alembic upgrade +1`

Осталось только инициализировать базу начальными данными. Для этого нужно подключиться к базе данных от имени только что созданного пользователя:

`psql -h 127.0.0.1 -p 5432 -U admin -d database` (потребуется ввести пароль)

Далее нужно выполнить скрипт инциализации `init_db.sql`:

`database=> \i {путь до проекта}/backend/src/init_db.sql;`

Если в консоли только логи от `INSERT`, то все готово.

3. Старт приложения

Перейдите в директорию `backend/src/` и выполните команду:

`python -m app`.

После этого сервер должен запуститься.
