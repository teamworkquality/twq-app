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
import router from './router'

export default {
  name: 'app',
  components: {
    'navbar': Navbar
  },
  /*beforeUpdate: function() {
    // TODO: check if user is logged in or not.
    // If not, redirect to login page.
    router.replace({ name: 'Login' });
  }*/
}
</script>

<style lang="scss">
@import 'assets/custom.scss';
@import '~bulma/bulma.sass';

html,
body {
  height: 100%;
}

#app {
  background: $backgroud-color;
  flex-flow: column;
  height: 100%;

  .container {
    margin: auto;
  }
}
</style>
