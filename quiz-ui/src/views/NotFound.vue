<template>
  <div class="not-found">
    <img src="../assets/golden-snitch.png" class="snitch" />
    <h1 class="main-title">Not found</h1>
  </div>
</template>

<script>
export default {
  name: 'NotFound',
  created() {
    document.getElementById('navbar-container').remove()
  }
}
</script>

<style>
.not-found {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  overflow: hidden;
}

.snitch {
  position: absolute;
  top: 50%;
  left: -10%; /* start offscreen */
  transform: translateY(-50%);
  animation: snitch-fly 6s linear infinite;
}

@keyframes snitch-fly {
  0% {
    left: -10%; /* start offscreen */
    border-radius: 0;
  }
  25% {
    left: 20%; /* move right and down */
    top: 60%;
    border-radius: 50%;
  }
  50% {
    left: 50%; /* move right and down */
    top: 30%;
    border-radius: 50%;
  }
  75% {
    left: 80%; /* move right and down */
    top: 60%;
    border-radius: 50%;
  }
  100% {
    left: 110%; /* fly offscreen */
    border-radius: 0;
  }
  /* 0% {
    left: 10%; 
    top: 50%;
    border-radius: 0;
  }
  10% {
    left: 40%; 
    top: 50%;
    border-radius: 50%;
  }
  20% {
    left: 45%; 
    top: 30%;
    border-radius: 50%;
  }
  30% {
    left: 50%;
    top: 60%;
    border-radius: 50%;
  }
  40% {
    left: 55%;
    top: 30%;
    border-radius: 50%;
  }
  50% {
    left: 60%;
    top: 60%;
    border-radius: 0;
  }
  60% {
    left: 65%; 
    top: 50%;
    border-radius: 0;
  }
  70% {
    left: 80%;
    top: 50%;
    border-radius: 0;
  }
  80% {
    left: 55%;
    top: 60%;
    border-radius: 0;
  }
  90% {
    left: 35%;
    top: 40%;
    border-radius: 0;
  }
  100% {
    left: 20%;
    top: 35%;
    border-radius: 0;
  } */
}

h1 {
  font-size: 4rem;
  margin-bottom: 1rem;
}

p {
  font-size: 2rem;
  text-align: center;
}
</style>
