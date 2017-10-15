<template>
<div class = "container">
		<div class="columns is-half">
			<p class="is-size-2 has-text-weight-semibold">Envio de Relatório</p>
		</div>
		<div class="columns is-multiline is-mobile">
			<div class="field - column is-one-quarter">
			  <label class="label">Equipe</label>
			  <div class="control"s>
			    <div class="select">
			      <select  v-model ="equipe">
			        <option v-for = "e in equipesN">
			        {{e.equip}}
			        </option>
			        
			      </select>
			    </div>
			  </div>
			</div>
	   </div>
	   <div class="container is-widescreen">
		  <div class="notification">
			   
			<div class="field">
			  <div class="control">
			    <label class="column is-half radio" v-for="n in nomes" >
			      <input type="radio" name="question">
			      {{n.nome}}
			    </label>
			  </div>
			</div>
				
         </div>
	  </div>
	  <div class="field column is-half is-pulled-right ">
		            <div class="control is-pulled-right column is-half">
		            <router-link :to="{name: 'ListarForms'}">
		              <button class="button is-dark is-fullwidth "v-on:click="envioRelatorio()" >Enviar Relatório</button>
		            </router-link>
		            </div>
	  </div>
	</div>
</template>

<script>

import HttpService from '@/service';

export default {
  name: 'envioRelatorio',
  data: () =>({
  	nome_formulario: '',
  	data_envio: '',
  	permissoes: '',
  	pergunta: '',
  	valores_invertidos: '',
  	valor_minimo: '',
  	valor_maximo: '',
  	equipe: '',
  	perg_texto: 'Pergunta',
  	count: 0,
  	perguntas:[],
  	novoForm: [],
  	selected: 'ABC',
  	nomes: [{nome: 'Renata'}, {nome: 'Bianca'}, {nome: 'Roberto'}],
  	equipesN: [{equip: 'ABC'}, {equip: 'DEF'}, {equip: 'GHI'}]
     
  }),
  methods: {
    envioRelatorio() {
    	this.novoForm.push({nome:this.nome_formulario,data:this.data_envio,permissao:this.permissoes,pergunta:this.perguntas,valores_inv:this.valores_invertidos,valor_max:this.valor_maximo,valor_min:this.valor_minimo,eq:this.equipe})
    	this.count = 0
    }
  }
}


</script>
<style scoped>
</style>