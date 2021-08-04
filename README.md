# compose-edu
Edu for docker compose and working with container status

## Обзор
Модель клиент-сервер. Сервер помещён в контейнер. Клиент отправляет на сервер тестовую строку, тот делает uppercase и возвращает его обратно клиенту.  
Клиент выводит логи контейнера, а затем останавливает и удаляет его.

## Обзор изменений для dev-listdir
На этой ветке я протестировал схему подключения папки для обмена данными с докер-контейнером, при которой изменения в папке на хосте мгновенно отражаются на содержимом связанной папки в контейнере. Сервер, помимо строки, возвращает клиенту список содержимого папки в контейнере.  
Принципиальным моментом является то, что сначала запускается контейнер, а затем изменяется содержимое папки на хосте.  
Желаемый эффект: изменение контента в хост-папке отображалось в папке контейнера вне зависимости от последовательности действий.
Это необходимо было проверить в связи с ошибкой, описанной здесь:  
https://github.com/docker/for-win/issues/5530  
А также протестировать флаг <code>-v</code> вместо <code>--mount</code>. Видимо последний является устарвшим и не позволяет изменять контент связанной папки после запуска контейнера.  
Подробнее про <code>-v</code> можно прочитать здесь:  
https://www.digitalocean.com/community/tutorials/how-to-share-data-between-the-docker-container-and-the-host

## Как собрать образ (есть изменения)
Находясь в папке с Dockerfile:  
<code>docker build -t exp/server-2 .</code>
## Запуск
<code>python cl.py</code>

## Обзор изменений для dev-compose
Эта ветка - форк **dev-listdir**. Результат работы тот же: используется общее содержимое в папке, его список возвращается сервером клиенту.  
Захотелось потестировать docker-compose, т.к. видится, что только через него можно определить порты для соединения с контейнером под Windows в Docker Desktop.

## Как собрать образ
Его не нужно собирать. При использовании docker-compose необходимо иметь Dockerfile. Как и в случае использования нативного docker, на его основе собирается образ. Однако часть функционала с Dockerfile и команды <code>docker run ...</code> можно переложить на docker-compose.yml. Например, прописать в нём исполняемую при запуске контейнера команду, определить порты, тома или привязать папку.  
По сути использование docker-compose объединяет в себе этапы работы с docker, а именно сборку образа (build) и запуск контейнера (run). Делается это в одной командой <code>docker-compose up</code> из папки проекта, где присутствует docker-compose.yml. 
Именно она добавлена в cl.py для запуска контейнера с сервером.  
Выполните для запуска проекта: <code>python cl.py</code>

## Обзор изменений для dev-docker-sdk
Форк **dev-compose**. На этой ветке я отказался от subprocess.run для работы с контейнерами. С помощью Docker SDK запускается контейнер с необходимыми портами и папкой. Проверяется статус перед установлением соединения. Определённые трудности в понимании были с параметром <code>ports</code> функции <code>client.containers.run()</code>:  
1. Порядок определения портов изменён: в левой части указывается порт в контейнере, а в правой порт на хосте. Более подробно описал в комментарии в <code>cl.py</code>
2. Изначально определил <code>ports = {'8787':'8787'}</code>. Однако после того, как я стал проверять статус перед отправкой, перестало устанавливаться соединение с контейнером. С чем это было конкретно связано, я так и не понял. Исправил ситуацию указанием конкретного IP хоста, а именно <code>ports={'8787/tcp':('127.0.0.1', 8787)}</code>. Возможно при обновлении атрибутов <code>containers.reload()</code> контейнера сбивались параметры сети и их нужно было указывать более явно, как я и сделал.  
  
Для порядка использовал конструкцию try-finally в s.py, чтобы соединение закрывалось при любом исходе работы сервера в контейнере, что также приводит к остановке контейнера.

## Как собрать образ
На этой ветке я отказался от docker-compose, т.к. порты можно указывать в функции <code>client.containers.run()</code>. Поэтому сборку проекта осуществлять с помощью Dockerfile:  
<code>docker build -t exp/server-mod .</code>
