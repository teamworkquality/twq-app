<template>
  <div class="columns">
    <div class="column is-half">
      <div>
        <p class="is-size-2 has-text-weight-semibold">Bem-vindo!</p>
      </div>
      <div class="has-vmargin-50">
        <p class="has-text-grey">Realize login para usufruir do sistema.</p>
      </div>
      <div>
        <form v-on:submit.prevent="onSubmit()" class="columns">
          <div class="column">
            <div class="field">
              <div class="control">
                <input class="input" type="email" placeholder="E-mail" v-model="email">
              </div>
            </div>
          </div>
          <div class="column">
            <div class="field">
              <div class="control">
                <input class="input" type="password" placeholder="Senha" v-model="password">
              </div>
            </div>
          </div>
          <div class="column">
            <div class="control">
              <button class="button is-dark is-fullwidth">Entrar</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'login',
  data: () => ({
    email: '',
    password: ''
  }),
  methods: {
    onSubmit() {
      console.log(this.email)
      console.log(this.password)
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
