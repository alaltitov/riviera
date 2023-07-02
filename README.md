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
    <a href="https://git-scm.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/git-colored.svg" width="36" height="36" alt="Git" /></a>
    <a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" width="36" height="36" alt="Python" /></a>
    <a href="https://developer.mozilla.org/en-US/docs/Glossary/HTML5" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/html5-colored.svg" width="36" height="36" alt="HTML5" /></a>
    <a href="https://www.w3.org/TR/CSS/#css" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/css3-colored.svg" width="36" height="36" alt="CSS3" /></a>
    <a href="https://getbootstrap.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/bootstrap-colored.svg" width="36" height="36" alt="Bootstrap" /></a>
    <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/mysql-colored.svg" width="36" height="36" alt="MySQL" /></a>
    <a href="https://flask.palletsprojects.com/en/2.0.x/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/flask-colored.svg" width="36" height="36" alt="Flask" /></a>
    <a href="https://www.adobe.com/uk/products/photoshop.html" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/photoshop-colored.svg" width="36" height="36" alt="Photoshop" /></a>
    <a href="adobe.com/uk/products/illustrator.html" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/illustrator-colored.svg" width="36" height="36" alt="Illustrator" /></a>
</p>
