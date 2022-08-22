# Групповой проект Yamdb

## Описание 
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». 

Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

Произведению может быть присвоен жанр. Новые жанры может создавать только администратор. Читатели оставляют к произведениям текстовые отзывы и выставляют произведению рейтинг (оценку в диапазоне от одного до десяти). Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

## Установка
Клонируем репозиторий на локальную машину:

git clone https://github.com/oladushkin/api_yamdb.git

Создаем виртуальное окружение:

`python -m venv venv`

Устанавливаем зависимости:

`pip install -r requirements.txt`

Применяем миграции:

`python manage.py migrate`

Запуск:

`python manage.py runserver`

### Над проектом работали:

- Денис Кудаков | [Github]([https://github.com/oladushkin](https://github.com/DK0894)) | Разработчик, разработка части, касающейся управления пользователями (Auth и Users): система регистрации и аутентификации, права доступа, работа с токеном, система подтверждения через e-mail
- Галиева Ляйсан | [Github](https://github.com/killyourasta) | Разработчик, написание части с категориями (Categories), жанрами (Genres) и произведениями (Titles): моделями, представлениями и эндпойнтами для них.
- Шелепин Дмитрий | [Github](https://github.com/oladushkin) | Тимлид, написание части с отзывами (Review) и комментариями (Comments): описание модели, представления, настройка эндпойнтов, определение прав доступа для запросов. Рейтинги произведений.
