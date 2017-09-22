<template>
	<div class="columns">
		<div class="column is-half">
			<div>
				<p class="is-size-2 has-text-weight-semibold">Formulários</p>
			</div>
			<table class="table has-vmargin-50 is-bordered is-stripe is-fullwidth">
				<thead>
					<tr>
						<th>Name</th>
						<th>Contact</th>
						<th>Country</th>
					</tr>
				</thead>

				<tbody>
					<tr>
						<td>Claudemira Florbela Anjos</td>
						<td>Nazaré Luciana Godinho</td>
						<td>Brasil</td>
					</tr>
					<tr>
						<td>Amadeu Marcelo Coimbra</td>
						<td>Floriano Almerinda Aragão</td>
						<td>Portugal</td>
					</tr>
					<tr>
						<td>Eva Viridiana Alencar</td>
						<td>Constantino Adérito Carromeu</td>
						<td>Angola</td>
					</tr>
					<tr class="is-selected">
						<td>Godofredo Ulrico Neves</td>
						<td>Clarindo Teodorico Paixão</td>
						<td>Alemanha</td>
					</tr>
					<tr>
						<td>Alfredo Lucrécia Amaro</td>
						<td>Gueda Sancha Fonseca</td>
						<td>Argentina</td>
					</tr>
					<tr>
						<td>Ema Collin Nazário</td>
						<td>Neuza Dirceu Veleda</td>
						<td>Uruguai</td>
					</tr>
				</tbody>
			</table>
        <div class="control">
				<div class="columns">
					<div class="column is-half">
							<button class="button is-dark is-medium">Novo</button>
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
	name: 'listarForms'
}
</script>
<style scoped></style>