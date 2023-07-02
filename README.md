<p align="center">
    <img src="https://github.com/alaltitov/docs_riviera/raw/main/Logo.svg" width="150">
</p>

<p align="center">
    https://riviera.alaltitov.ru/
</p>

<p align="center">
    <img alt="Static Badge" src="https://img.shields.io/badge/made%20by-alaltitov-blue">
    <img alt="Static Badge" src="https://img.shields.io/badge/version-v1.0%20Alpha-green">
    <img alt="Static Badge" src="https://img.shields.io/badge/python-v3.9.0-yellow">
    <img alt="Static Badge" src="https://img.shields.io/badge/license-MIT-orange">
</p>

## О проекте

Пример реализации сайта коттеджного поселка с регистрацией, авторизацией, личным кабинетом пользователя, передачей 
показаний счетчиков и оплатой коммунальных платежей через Ю-Кассу с простой аналитикой, историей показаний и баланса.<br>

<p align="center">
  <img src="https://github.com/alaltitov/docs_riviera/raw/main/card.png" height="300">
  <img src="https://github.com/alaltitov/docs_riviera/raw/main/chart.png" height="300">
</p>
<p align="center">
  <img src="https://github.com/alaltitov/docs_riviera/raw/main/utility_history.png" height="250">
</p>

## Как пользоваться?

Для регистрации нового пользователя необходимо ввести данные и PIN: **123456**<br>

В базу данных добавлен пользователь с тестовыми данными:<br>

login: **first**<br>
password: **123**<br>

Чтобы воспользоваться оплатой, необходимо ввести данные тестовой
банковской карты Ю-касса:<br>

**5555 5555 5555 4444**<br>

Срок действия любой, год больше текущего, CVV любой<br>

<div>
  <img src="https://github.com/alaltitov/docs_riviera/raw/main/pay4.png" height="300">
  <img src="https://github.com/alaltitov/docs_riviera/raw/main/pay5.png" height="300">
</div>

## Документация

Возможно потребуется установить urllib3 версии 1.26.6: **pip install urllib3==1.26.6**<br>
С ней не возникает ошибок при использовании OpenSSL ниже версии 1.1.1+.<br>

В обработчике платежей заменить страницу возврата с http://127.0.0.1/owner на https://<ваш домен>/owner

## Ближайшие планы по доработке:

- внедрение reCAPTCHA от Google
- восстановление пароля

## Стек технологий
<p align="center">
    <img src="https://github.com/devicons/devicon/blob/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/python/python-original.svg" width="40">
    <img src="https://github.com/devicons/devicon/blob/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/flask/flask-original.svg" width="40">
    <img src="https://github.com/devicons/devicon/blob/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/html5/html5-original.svg" width="40">
    <img src="https://github.com/devicons/devicon/blob/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/css3/css3-original.svg" width="40">
    <img src="https://github.com/devicons/devicon/blob/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/mysql/mysql-original-wordmark.svg" width="40">
    <img src="https://github.com/devicons/devicon/blob/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/illustrator/illustrator-line.svg" width="40">
    <img src="https://github.com/devicons/devicon/blob/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/bootstrap/bootstrap-original.svg" width="40">
</p>
