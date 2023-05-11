<template>
  <nav class="navbar navbar-expand-lg bg-light">
    <div class="container-fluid">
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav main-navbar">
          <li class="nav-item">
            <router-link class="nav-link" to="/"><i class="bi bi-house"></i></router-link>
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
    name: "Navbar",
    
};
</script>