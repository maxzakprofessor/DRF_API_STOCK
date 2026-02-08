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
            Этот проект - это складской учет, который позволяет вести учет складов, ТМЦ, прихода и перемещения ТМЦ между складами.
          </div>
        </div>
  </div>
  <div class="accordion-item">
        <h2 class="accordion-header" id="headingTwo">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            О стеке разработки
          </button>
        </h2>
        <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#accordionExample">
          <div class="accordion-body">
              Этот фронтенд разработан с помощью <strong>Vue JS, Bootstrap 5, Axios, pdfmake. </strong>.
          </div>
        </div>
  </div>
  <div class="accordion-item">
    <h2 class="accordion-header" id="headingThree">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
        О бэкенде и базе данных
      </button>
    </h2>
    <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree" data-bs-parent="#accordionExample">
      <div class="accordion-body">
          Этот бэкенд разработан с помощью <strong>Django Rest Framework, PostgreSQL. </strong>.
      </div>
    </div>
  </div>
</div>
        </div>
      </div>
  </div>

  </div>
</template>

