<template>
	<div class="columns">
		<div class="column is-half">
			<div>
				<p class="is-size-2 has-text-weight-semibold">Formulários</p>
			</div>
			<table class="table has-vmargin-50 is-bordered is-stripe is-fullwidth">
				<thead>
					<tr>
						<th>Nome</th>
						<th>Data</th>
						<th>Permissão</th>
					</tr>
				</thead>

				<tbody v-for = "item in formularios">
					<tr>
						<td>{{item.nome}}</td>
						<td>{{item.data}}</td>
						<td>Brasil</td>
					</tr>
					
				</tbody>
			</table>
        <div class="control">
				<div class="columns">
					<div class="column is-half">
					     <router-link :to="{name: 'CriarForm'}">
							<button class="button is-dark is-medium">Novo</button>
					     </router-link>
					</div>
					<div class="column">
						<button class="button is-light is-medium">Editar</button>
						<button class="button is-light is-medium">Enviar</button>
						<button class="button is-light is-medium">Permissões</button>
					</div>
				</div>
  			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'listarForms',
	data: () =>({
		formularios:[{nome:'Formulário 1',data:'10/10/2017'},{nome:'Formulário 2',data:'20/10/2017'}]
	})

}
</script>
<style scoped></style>