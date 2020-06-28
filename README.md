<p align="center">
  <a href="https://github.com/thelastpolaris/anti-corona-crm/">
    <img src="web-app/app/main/static/assets/img/brand/blue.png" alt="Logo" width="400">
  </a>

  <h3 align="center">COVID-19 | Центр Контроля</h3>

  <p align="center">
    Web приложение, призванное помочь Министерству Здравоохранения Республики Казахстан контролировать распространение коронавируса
    <br />
  </p>
  
  ## Legal Disclaimer | Лицензия
  Данный проект бесплатен и доступен по open-source лицензии от MIT. Это значит, что вы можете использовать этот проект бесплатно, сделать fork и развивать его самостоятельно. Единственное условие использования - вы всегда должны указывать оригинальных авторов (см. Copyright в лицензии и ниже по тексту). Я прошу Вас указывать следующую информацию, если Вы собираетесь использовать проект, сделать fork или же если вы хотите рассказать о данном проекте в новостях или соц. сетях,.
  
  "Веб-Приложение Covid-19 было разработано Артемом Федоскиным, Alem School, при активном участии РГП на ПХВ "Национального Центра общественного здравоохранения" МЗ РК (в частности Асель Абакова и Ерубаев Жанибек). Проект тестируется и активно развивается благодаря эпидемиологам территориальных департаментов КККБТУ РК. Проект был начат в ходе хакатона Alem School, при поддержке Фонда Первого Президента - Елбасы"
  
  Отсутствие копирайта, указанного в файле LICENSE.md при использовании данного проекта будет рассматриваться как нарушение лицензии. Я оставляю за собой право применять легальные меры против нарушения лицензии на свое усмотрение. Используя данный проект, вы автоматически соглашаетесь с данным условием.

<a href="https://github.com/thelastpolaris/anti-corona-crm/blob/master/LICENSE">MIT License</a>

Copyright (c) 2020 Artem Fedoskin

  
  ## Список Возможностей

* Загрузка списка новых пациентов из .xls и .xlsx файлов. Извлечение и сохранение данных о пациентах в базу данных
* Добавление новых пациентов через удобную веб-форму
* Онлайн карта, отображающая всех пациентов
* Поиск пациентов по регионам, статусам "найден" и "госпитализирован"
* Разработано с помощью Python, веб фреймворка Flask, и <a href="https://github.com/app-generator/flask-boilerplate-dashboard-argon">данного шаблона</a>



  ## Локализация
* ``pybabel extract -F babel.cfg -k _l -o messages.pot .``
* ``pybabel init -i messages.pot -d app/translations -l '*your locale code (e.g. kk_KZ)*'``
* Используйте Poedit для перевода .po файла
* ``pybabel update -i messages.pot -d app/translations`` для обновления файла локализации

  ## Развертывание на сервере
Репозиторий содержит скрипт `setup.sh`. Данный скрипт устанавливает на сервере c ОС _Ubuntu 18.04_ зависимости этого проекта и запускает его.
1. Скрипт устанавливает на сервере: nginx, docker, docker-compose, postgresql.
2. Создает конфигурационный nginx файл.
3. Cоздает в postgresql UTF8 базу данных и пользователя.
4. Запускает проект.

Перед запуском следует указать следующие _env variables_:
```bash
$> export CRM_ENDPOINT="crm.yourwebsite.kz"
$> export DATABASE_USER="someuser"
$> export DATABASE_PASSWORD="somepassword"
$> export CERTIFICATE_PATH="path_to_certificate"
```

Далее
```bash
$> sh setup.sh
```

  ## Перезапуск проекта
```bash
$> cd path_to_project/web-app/
$> docker-compose down && docker-compose up -d
```

  ## Обновление проекта
```bash
$> cd path_to_project/web-app/
$> git pull
$> docker-compose down && docker-compose build && docker-compose up -d
```
