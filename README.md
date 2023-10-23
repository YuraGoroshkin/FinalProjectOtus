
**Финальный проект Otus на примере проекта Restful Booker Platform:**

  Платформа веб-сервисов, формирующая систему бронирования проживания и завтрака. Основная цель платформ — обучение других тому, как исследовать и тестировать платформы веб-сервисов, а также разрабатывать стратегии и внедрять автоматизацию в стратегиях тестирования.
  
  [общедоступный - пример проекта](https://automationintesting.online/)
  
  [проект - github](https://github.com/mwinteringham/restful-booker-platform)

**Зависимости:**
  * [Python] 3.10
  * [pytest] 7.3.2
  * [selenium] 4.10.0
  * [faker] 18.11.2
  * [allure-pytest] 2.13.2
  * [requests] 2.31.0
  * [urllib3] 2.0.6
  * [jsonschema] 4.19.1 

**Установка проекта:**

* pip 
```sh
pip install -r requirements.txt
```
* docker-compose
```sh
  docker-compose up -d
  ```

**Запуск тестов:**


Перед запуском тестов требуется узнать url проекта, если запуск был по умолчанию через docker-compose то контейнер rbp-proxy запустил проект на 127.0.0.1

*  --url по умолчанию
  ```sh
  http://127.0.0.1
  ```
А для api тестов можно проверить доступность переходом в swagger под проекта сервиса, кторый требуется проверить, например(по умолчанию для message): http://localhost:3006/message/swagger-ui/index.html

Подробнее смотри в [проекте - github](https://github.com/mwinteringham/restful-booker-platform) разделе API details


Есть возможность выбрать какие тесты запустить, через маркеры ui и api

*  
  ```sh
  pytest -m ui
  ```
*  
  ```sh
  pytest -m api
  ```

**Отчёты:**

Все отчёты сохроняются в корне проекта папки .allure-results и .allure-report

Allure server мониторит данные папки и создаёт отчёты, последние доступны по ссылке
```sh
  http://127.0.0.1:5050/allure-docker-service/projects/default/reports/latest/index.html
  ```
Подробнее о возможностях allure-server в [источнике](https://github.com/fescobar/allure-docker-service)

<img src="https://lh3.googleusercontent.com/u/0/drive-viewer/AK7aPaBFa27rE8O5sIOGyssfoj6WQrWg6dTDbraxI4lyqyN1JTzmvWsnQFZvKBreFxsYDvxvAMi6391LJxNv50GuIaOekG0sAQ=w1850-h944" alt="отчёт">
