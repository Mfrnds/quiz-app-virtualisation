<template>
  <nav class="navbar navbar-expand-lg bg-light">
    <div class="container-fluid">
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav main-navbar">
          <li class="nav-item">
            <router-link class="nav-link" v-if="!isAdmin" to="/"
              ><i class="bi bi-house"></i
            ></router-link>
            <router-link class="nav-link" v-else to="/admin/view-questions"
              ><i class="bi bi-table"></i
            ></router-link>
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
            <router-link class="nav-link" v-else to="/logout"
              ><i class="bi bi-box-arrow-right"></i
            ></router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
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
