# compose-edu
Edu for docker compose and working with container status

## Обзор
Модель клиент-сервер. Сервер помещён в контейнер. Клиент отправляет на сервер тестовую строку, тот делает uppercase и возвращает его обратно клиенту.  
Клиент выводит логи контейнера, а затем останавливает и удаляет его.

## Обзор изменений для dev-listdir
На этой ветке я протестировал схему подключения папки для обмена данными с докер-контейнером, при которой изменения в папке на хосте мгновенно отражаются на содержимом связанной папки. в контейнере.  
Принципиальным моментом является то, что сначала запускается контейнер, а затем изменяется содержимое папки на хосте.  
Желаемый эффект: изменение контента в хост-папке отображалось в папке контейнера вне зависимости от последовательности действий.
Это необходимо было проверить в связи с ошибкой, описанной здесь:  
https://github.com/docker/for-win/issues/5530  
А также протестировать флаг <code>-v</code> вместо </code>--mount</code>. Видимо последний является устарвшим и не позволяет изменять контент связанной папки после запуска контейнера.

## Как собрать образ
Находясь в папке с Dockerfile:  
<code>docker build -t exp/server-1 .</code>
## Запуск
<code>python cl.py</code>