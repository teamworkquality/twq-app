<template>
<div class = "container">
		<div class="columns is-half">
			<p class="is-size-2 has-text-weight-semibold">Envio Relatório</p>
		</div>
		<div class="columns is-multiline is-mobile">
			<div class="field - column is-one-quarter">
			  <label class="label">Equipe</label>
			  <div class="control"s>
			    <div class="select">
			      <select  v-model ="permissoes">
			        <option>Visualizar</option>
			        <option>Vizualizar e responder</option>
			        <option>Editar</option>
			      </select>
			    </div>
			  </div>
			</div>
			<div class = "field - colum is-half">
			<div class="field-label column is-half" >
			    <label class="label">Valores Invertidos?</label>
			</div>
			 <div class="field-body column is-half">
			    <div class="field is-narrow">
			      <div class="control">
			        <input type="checkbox" v-model="valores_invertidos"> 
			      </div>
			    </div>
			  </div>
			 </div>
			<div class="field column is-one-quarter">
				  <div class="field-label is-normal column is-half">
				    <label class="label">Valor Mínimo:</label>
				  </div>
				  <div class="field-body">
				    <div class="field column is-half">
				      <div class="control">
				        <input class="input " type="text" placeholder="1" v-model ="valor_minimo">
				      </div>
				    </div>
				  </div>
		    </div>
		    <div class="field column is-one-quarter">
				  <div class="field-label is-normal column is-half">
				    <label class="label">Valor Máximo:</label>
				  </div>
				  <div class="field-body">
				    <div class="field column is-half">
				      <div class="control">
				        <input class="input " type="text" placeholder="10" v-model ="valor_maximo">
				      </div>
				    </div>
				  </div>
				</div>
	   </div>
	   <div class="container is-widescreen">
		  <div class="notification">
			    <div class="field - column is-half">
				  <label class="label" id = "perg">{{perg_texto}}</label>
				  <div class="control" >
		    		<input class="input " type="text" placeholder="Pergunta" v-model ="pergunta">
		          </div>
				</div>
				<div class="field is-horizontal">
			  
			</div>
				
						
	        <!--    <p>data: {{data}}</p> -->
         </div>
	  </div>
	  <div class="field column is-half is-pulled-right ">
		            <div class="control is-pulled-right column is-half">
		            <router-link :to="{name: 'ListarForms'}">
		              <button class="button is-dark is-fullwidth "v-on:click="finalizarForm()" >Finalizar Formulário</button>
		            </router-link>
		            </div>
	  </div>
	</div>
</template>

<script>
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
  	novoForm: []
     
  }),
  methods: {
    novaPergunta() {
       ++ this.count
       this.perguntas.push(this.pergunta) 
       this.perg_texto = 'Pergunta '+this.count

    },
    finalizarForm() {
    	this.novoForm.push({nome:this.nome_formulario,data:this.data_envio,permissao:this.permissoes,pergunta:this.perguntas,valores_inv:this.valores_invertidos,valor_max:this.valor_maximo,valor_min:this.valor_minimo,eq:this.equipe})
    	this.count = 0
    }
  }
}


</script>
<style scoped>
</style>