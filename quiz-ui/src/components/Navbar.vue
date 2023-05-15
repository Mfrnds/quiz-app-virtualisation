<template>
  <nav class="navbar navbar-expand-lg bg-light">
    <div class="container-fluid">
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#mainNavBar"
        aria-controls="mainNavBar"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="mainNavBar">
        <ul class="navbar-nav main-navbar">
          <li class="nav-item">
            <router-link class="nav-link" v-if="!isAdmin" to="/"
              ><i class="bi bi-house"></i
            ></router-link>
            <router-link class="nav-link" v-else to="/admin"
              ><i class="bi bi-table"></i
            ></router-link>
          </li>
          <li class="nav-item">
            <button class="btn p-0" @click="toggleTheme">
              <i v-if="theme === 'light'" class="bi bi-moon-stars"></i
              ><i v-else class="bi bi-sun"></i>
            </button>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" v-if="!isAdmin" to="/login"
              ><i class="bi bi-person"></i
            ></router-link>
            <span class="nav-link" v-else @click="handleLogout"
              ><i class="bi bi-box-arrow-right"></i
            ></span>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <!-- <nav class="navbar navbar-expand-lg bg-light">
    <div class="container-fluid">
      <ul class="navbar-nav main-navbar">
        <li class="nav-item">
          <router-link class="nav-link" v-if="!isAdmin" to="/"
            ><i class="bi bi-house"></i
          ></router-link>
          <router-link class="nav-link" v-else to="/admin"><i class="bi bi-table"></i></router-link>
        </li>
        <li class="nav-item">
          <button class="btn" @click="toggleTheme">
            <i v-if="theme === 'light'" class="bi bi-moon-stars"></i
            ><i v-else class="bi bi-sun"></i>
          </button>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" v-if="!isAdmin" to="/login"
            ><i class="bi bi-person"></i
          ></router-link>
          <span class="nav-link" v-else @click="handleLogout"
            ><i class="bi bi-box-arrow-right"></i
          ></span>
        </li>
      </ul>
    </div>
  </nav> -->
</template>

<script>
import AdminService from '../services/AdminService'

export default {
  name: 'MainNavbar',
  data() {
    return {
      theme: '',
      isAdmin: false
    }
  },
  methods: {
    toggleTheme() {
      if (document.documentElement.getAttribute('data-bs-theme') == 'dark') {
        document.documentElement.setAttribute('data-bs-theme', 'light')
        window.localStorage.setItem('theme', 'light')
      } else {
        document.documentElement.setAttribute('data-bs-theme', 'dark')
        window.localStorage.setItem('theme', 'dark')
      }
      this.theme = window.localStorage.getItem('theme')
    },
    handleLogout() {
      AdminService.clear()
      window.location = '/'
    }
  },
  mounted() {
    if (window.localStorage.getItem('theme') === undefined) {
      window.localStorage.setItem('theme', 'light')
    } else {
      document.documentElement.setAttribute('data-bs-theme', window.localStorage.getItem('theme'))
    }
  },
  created() {
    this.theme = window.localStorage.getItem('theme')
    this.isAdmin = window.location.href.includes('admin')
  }
}
</script>
