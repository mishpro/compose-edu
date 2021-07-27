# compose-edu
Edu for docker compose and working with container status

## Обзор
Модель клиент-сервер. Сервер помещён в контейнер. Клиент отправляет на сервер тестовую строку, тот делает uppercase и возвращает его обратно клиенту.  
Клиент выводит логи контейнера, а затем останавливает и удаляет его.
## Как собрать образ
Находясь в папке с Dockerfile:  
<code>docker build -t exp/server-1 .</code>
## Запуск
<code>python cl.py</code>
