<template>
  <nav class="navbar navbar-expand-lg bg-light">
    <div class="container-fluid">
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav main-navbar">
          <li class="nav-item">
            <router-link class="nav-link" to="/"><i class="bi bi-house"></i></router-link>
          </li>
          <li class="nav-item">
            <button class="btn" @click="toggleTheme"><i class="bi bi-moon-stars"></i></button>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/login"><i class="bi bi-person"></i></router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
    name: "MainNavbar",
    methods:{
      toggleTheme(){

        if (document.documentElement.getAttribute('data-bs-theme') == 'dark') {
            document.documentElement.setAttribute('data-bs-theme','light');
            window.localStorage.setItem('theme', 'light');
        }
        else {
            document.documentElement.setAttribute('data-bs-theme','dark');
            window.localStorage.setItem('theme', 'dark');
        }
      }
    },
    mounted(){
      if( window.localStorage.getItem('theme') === undefined){
          window.localStorage.setItem('theme', 'light');
        }else{
          document.documentElement.setAttribute('data-bs-theme', window.localStorage.getItem('theme'));
        }
    }
    
};
</script>