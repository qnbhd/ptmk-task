# PTMK-test-task

<p style="background-color: #1c1f39;">
  <img src="https://i.postimg.cc/d08d18kL/vacancy-test-task.png">
</p>

# Отчёт по работе

Запуск: ```python main.py (WorkId) {Args}```

```WorkId``` совпадает с операциями в тестовом задании. (6 - вывод первых ```records``` записей из бд)

В файле ```requirements.txt``` находятся необходимые пакеты для установки (```pip -r requirements.txt```)
Задание 6 не выполнено (действия с базой данных)

Используется база данных ```SQLite```. Для работы с ней используется ORM (SQLAlchemy)

# Описание файлов

- ```main.py``` - главный файл для запуска скрипта
- ```ptmkworker.py``` - файл с классом для работы с необходимым функционалом, некоторыми настройками для отладки
- ```user.py``` - файл с моделью для базы данных
- ```benchmark.py``` - файл с декоратором для замера времени выполнения функции
