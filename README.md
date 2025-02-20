# Исправление оценок в электронном дневнике

Пошаговая инструкция изменений в электронном дневнике 

## Основные возможности

- Изменения базы данных эл. дневника
- Афиширование изменений на сайте

## Шаги запуска программы :
Откройте терминаль
! Важно находиться в папке проекта (e-diary) !

1) Клонируйте проект
```bash
git clone https://github.com/devmanorg/e-diary.git
```
2) Для сохранения всех необходимых библиотек откройте терминаль в папке скачанного проекта и введите команду:
```bash
pip install -r requirements.txt
```
3) Создайте БД командой 
```bash
pip python manage.py migrate
````
4) Запустите сервер
```bash
pip python manage.py runserver
````
5) Запустите shell
```bash
pip python manage.py shell
````
6) Откройте файл script.py

## Изменение оценок

Чтобы изменить свои оценки, выполните следующие шаги в Django Shell:

1. Найдите ученика по полному имени:
    ```bash
    Ivan = Schoolkid.objects.filter(full_name='Фролов Иван Григорьевич').first()
    ```

2. Измените оценки на 5 (если у ученика есть оценки 2 или 3):
    ```bash
    if Ivan:
        fix_marks(Ivan)
        print("Оценки успешно исправлены!")
    else:
        print("Ошибка: ученик не найден!")
    ```

## Добавление комментария

Чтобы добавить комментарий, выполните следующие шаги:

1. Найдите ученика по полному имени:
    ```bash
    Ivan = Schoolkid.objects.filter(full_name='Фролов Иван Григорьевич').first()
    ```

2. Укажите предмет и добавьте похвалу:
    ```bash
    if Ivan:
        create_commendation(Ivan, 'Математика')
        print("Комментарий успешно добавлен!")
    else:
        print("Ошибка: ученик не найден!")
    ```

## Обработка ошибок

При поиске ученика могут возникнуть ошибки. Убедитесь, что указано корректное имя:

1. Если указано популярное имя, может быть найдено несколько учеников:
    ```bash
    from django.core.exceptions import MultipleObjectsReturned

    try:
        Ivan = Schoolkid.objects.get(full_name='Степан')
    except MultipleObjectsReturned:
        print("Ошибка: найдено несколько учеников с таким именем! Уточните запрос.")
    ```

2. Если указано несуществующее имя, будет выведено сообщение об ошибке.
