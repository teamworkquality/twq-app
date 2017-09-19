<template>
  <div class="columns">
    <div class="column is-half">
      <div>Bem-vindo!</div>
      <div>
        <form v-on:submit.prevent="onSubmit()" class="columns">
          <div class="column">
            <div class="field">
              <div class="control">
                <input class="input" type="text" placeholder="E-mail" v-model="email">
              </div>
            </div>
          </div>
          <div class="column">
            <div class="field">
              <div class="control">
                <input class="input" type="text" placeholder="Senha" v-model="password">
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
  name: 'hello',
  data: () => ({
    email: '',
    password: ''
  }),
  methods: {
    onSubmit() {
      console.log(this.email);
      console.log(this.password);
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
