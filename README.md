### Репозиторий студентов Третьякова Дмитрия и Бабинова Данила для лабораторной работы № 2 по дисциплине "Инструментальные средства информационных систем".

Цель: написать простое приложение с использованием контейнеризации

### How To Run
```
git clone https://github.com/DmitryTretiakov/Docker_lb2.git
```
```
Собрать Docker образ
Откройте терминал в корневой директории вашего приложения и выполните следующую команду:
docker build -t myapp .
```
```
Запустить приложение
Выполните следующую команду, чтобы запустить Docker контейнер на основе созданного образа:

docker run -p 5000:5000 myapp
```
Перейти по ссылке
```
http://localhost:5000/
```
