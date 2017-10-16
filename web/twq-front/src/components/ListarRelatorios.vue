<template>
	<div class="columns is-multiline is-mobile">
		<div class="column is half">
			<div>
				<p class="is-size-2 has-text-weight-semibold">Relatórios</p>
			</div>
			<table class="table has-vmargin-50 is-bordered is-stripe is-fullwidth">
				<thead>
					<tr>
						<th>Nome</th>
						<th>Equipe</th>
					</tr>
				</thead>

				<tbody v-for = "item in relatorios">
					<tr>
						<td>{{item.nome}}</td>
						<td>{{item.equipe}}</td>
					</tr>
					
				</tbody>
			</table>
      </div>  

	  <div class="field column is-half">
	                <div class="column is-one-quarter"></div>
	                <div class="column is-one-quarter"></div>
	                <div class="column is-one-quarter"></div>
		            <div class="column is-one-quarter">
		              <button class="button is-outlined is-fullwidth " v-on:click="novaPergunta()">Novo</button>
		            </div>
		            <div class="column is-one-quarter">
		            <!-- <router-link > -->
		              <button class="button is-dark is-fullwidth "v-on:click="finalizarForm()" >Enviar</button>
		            <!-- </router-link> -->
		            </div>
		            <div class="column is-one-quarter">
		            <!-- <router-link> -->
		              <button class="button is-outlined is-fullwidth "v-on:click="finalizarForm()" >Comparar</button>
		            <!-- </router-link> -->
		            </div>
	  </div>
	
	</div>
</template>

<script>
import HttpService from '@/service';
export default {
	name: 'listarRelatorios',
	data: () =>({
		relatorios:[{nome:'Relatorio 1',equipe:'Equipe 1'},{nome:'Relatorio 2',equipe:'Equipe 2'}]
	})

}
</script>
<style scoped></style>