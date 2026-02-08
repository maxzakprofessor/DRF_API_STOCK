<template>
  <div className="about">
    <div className="container">
      <div className="row">
        <div className="col">
          <h3>          </h3>
          <div class="accordion" id="accordionExample">
  <div class="accordion-item">
        <h2 class="accordion-header" id="headingOne">
          <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            О проекте
          </button>
        </h2>
        <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
          <div class="accordion-body">
            Интеллектуальная экосистема складского учета (Sklad AI EcoSystem), который позволяет вести учет складов, ТМЦ, прихода и перемещения ТМЦ между складами.
          </div>
        </div>
  </div>
  <div class="accordion-item">
        <h2 class="accordion-header" id="headingTwo">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            ------------------------------------------------------
https://sklad-backend-docker.onrender.com
Бэкенд.Облака Render.
------------------------------------------------------
https://mzakiryanovgmailcom.pythonanywhere.com/
Фронтенд. Облако Vercel.
-------------------------------------------------------
Репозитории в GitHub
https://github.com/maxzakprofessor/DRF_API_STOCK.git
          </button>
        </h2>
        <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#accordionExample">
          <div class="accordion-body">
Ключевые достижения и задачи:

1)Архитектура и API: Спроектирована и реализована клиент-серверная архитектура (Separation of Concerns). Разработан гибкий REST API на Django Rest Framework, обеспечивающий бесшовную миграцию данных и сохранение целостности БД при рефакторинге сущностей.

2)Контейнеризация и DevOps (Docker):
Бэкенд упакован в Docker-контейнер, оптимизируя среду для стабильного деплоя.
Обеспечен переход с SQLite на промышленную БД PostgreSQL (Managed).

3)Настроены CI/CD процессы: автоматический деплой фронтенда на Vercel и контейнеризированного бэкенда на Render.

4)Интеграция Искусственного Интеллекта (LLM):
Внедрен Google Gemini API для реализации модуля интеллектуальной аналитики.
Разработана система поддержки принятия решений (DSS), которая анализирует остатки в реальном времени и выдает рекомендации по закупкам.

5)Безопасность и Сеть:
Интегрирована авторизация на базе JWT (SimpleJWT).
Настроено безопасное межсерверное взаимодействие через CORS-политики и управление секретами через Environment Variables.

6)Frontend Development: Создан реактивный интерфейс на Vue.js 3 (Vite) с использованием асинхронного взаимодействия (Async/Await) и глубокой обработки состояний API (лоадеры, кастомные уведомления о тарифах).
          </div>
        </div>
  </div>
  <div class="accordion-item">
    <h2 class="accordion-header" id="headingThree">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
        Технологический стек (Full-Stack)
1)Backend: Python 3.10+, Django, DRF, SimpleJWT.
2)Database: PostgreSQL, агрегация данных и сложные расчеты через Django ORM.
3)Frontend: Vue.js 3, Axios, Bootstrap 5.
4)Infrastructure: Docker, Dockerfile, Render (Web Services), Vercel.
5)AI: Google Gemini API (LLM Integration), Prompt Engineering.
      </button>
    </h2>
    <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree" data-bs-parent="#accordionExample">
      <div class="accordion-body">
          Soft Skills & Методология
  1)AI-Driven Development: Эффективное применение LLM-инструментов для ускорения разработки, глубокой отладки сетевых конфигураций Docker и написания технической документации.
  2)Problem Solving: Успешная реализация миграции проекта из монолитной структуры (PythonAnywhere) в масштабируемую облачную среду (Docker/Render), решение комплекса задач по настройке сетевых протоколов и оптимизации ресурсов.
  3)Итеративный подход: Работа по методологии Agile: от реализации базового CRUD до выпуска продукта с элементами машинного обучения.
      </div>
    </div>
  </div>
</div>
        </div>
      </div>
  </div>

  </div>
</template>

