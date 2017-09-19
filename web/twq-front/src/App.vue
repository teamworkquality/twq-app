<template>
  <div id="app" class="is-flex">
    <navbar></navbar>
    <div class="container">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar'
export default {
  name: 'app',
  components: {
    'navbar': Navbar
  }
}
</script>

<style lang="scss">
@import '~bulma/bulma.sass';

html,
body {
  height: 100%;
}

#app {
  background: #e5e9f2;
  flex-flow: column;
  height: 100%;

  .container {
    margin: auto;
  }
}
</style>
