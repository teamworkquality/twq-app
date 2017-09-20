<template>
  <nav class="navbar is-transparent" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <button class="button navbar-burger">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
    <div class="navbar-menu">
      <div class="navbar-end">
        <router-link :to="item.route" :key="item.route" class="navbar-item" v-for="item in navItems">
          {{ item.title }}
        </router-link>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'navbar',
  data: () => ({
    navItems: [
      { title: 'Início', route: '#' },
      { title: 'Permissões', route: '#' },
      { title: 'Formulários', route: '#' },
      { title: 'Equipes', route: '#' }
    ]
  })
}
</script>

<style lang="scss" scoped>
.navbar {
  &.is-transparent {
    background: transparent;
  }
}
</style>
