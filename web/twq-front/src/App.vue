<template>
  <div id="app">
    <div>Navbar aqui</div>
    <div class="container">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
@import '~bulma/css/bulma.css';
</style>
