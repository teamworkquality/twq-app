<template>
	<div class="columns">
	<div class="column"></div>
		<div class="column is-three-quarters">
			<p class="is-size-2 has-text-weight-semibold has-text-centered">Formulário 1</p>
			
			<p class="is-size-4">Há comunicação frequente dentro da equipe?</p>
			  <div class="control">
				  <label class="radio">
				    <input type="radio" name="answer1">
				    Sim
				  </label>
				  <br>
				  <label class="radio">
				    <input type="radio" name="answer1">
				    Não
				  </label>
				</div>
			  <p class="is-size-4">Você está satisfeito com sua equipe?</p>
				<div class="control">
				  <label class="radio">
				    <input type="radio" name="answer2">
				    Sim
				  </label>
				  <br>
				  <label class="radio">
				    <input type="radio" name="answer2">
				    Não
				  </label>
				</div>
			<div class="column">
						<button class="button is-danger is-medium is-pulled-left">Cancelar</button>
						<button class="button is-primary is-medium is-pulled-right">Enviar</button>
			</div>

		</div>
		<div class="column"></div>
	</div>
</template>

<script>
export default {
	name: 'Responder',
	data: () =>({
		formularios:[{nome:'Formulário 1',data:'10/10/2017'},{nome:'Formulário 2',data:'20/10/2017'}]
	})

}
</script>
<style scoped></style>