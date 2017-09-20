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

$backgroud-color: #e5e9f2;

$util-values: 10, 20, 30, 40, 50;

@each $i in $util-values {
  .has-vmargin-#{$i} {
    margin-top: #{$i}px;
    margin-bottom: #{$i}px;
  }
}

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
