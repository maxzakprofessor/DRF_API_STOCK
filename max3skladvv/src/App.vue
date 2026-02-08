<template>
  <div  className="container">
      <h3 className="d-flex justify-content-center">
        Складской учет. Бэкенд Django Rest Framework PostgreSQL. Фронтенд Vue JS.
      </h3>
      <nav className="navbar navbar-expand-sm bg-light navbar-dark">
          <ul className="navbar-nav">

        
            <li className="nav-item m-1">
                <router-link class="btn btn-light btn-outline-primary"
                to="/stocks">Склады</router-link>
            </li>

            <li className="nav-item m-1">
                <router-link class="btn btn-light btn-outline-primary"
                to="/goods">Товары</router-link>
            </li>

            <li className="nav-item m-1">
                <router-link class="btn btn-light btn-outline-primary"
                to="/goodincomes">Приход ТМЦ</router-link>
            </li>           

            <li className="nav-item m-1">
                <router-link class="btn btn-light btn-outline-primary"
                to="/goodmoves">Перемещение ТМЦ</router-link>
            </li>           

            <li className="nav-item m-1">
                <router-link class="btn btn-light btn-outline-primary"
                to="/goodrests">Остатки ТМЦ</router-link>
            </li>   

            <li className="nav-item m-1">
                <router-link class="btn btn-light btn-outline-primary"
                to="/">О проекте</router-link>
            </li>            

          </ul>
      </nav>
      <router-view></router-view>
  </div>
</template>