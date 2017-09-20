<template>
	<div class = "container">
		<div class="columns is-multiline is-mobile">
			<div class="field - column is-one-quarter">
			  <label class="label">Nome</label>
			  <div class="control">
	    		<input class="input " type="text" placeholder="Nome do formulário">
	          </div>
			</div>
			<div class="field - column is-one-quarter">
			  <label class="label">Data de Envio</label>
			  <div class="control">
	    		<input class="input " type="text" placeholder="DD/MM/AAAA">
	          </div>
			</div>
			<div class= "field columns is-multiline is-mobile is-narrow">
			  <div class="control">
			    <label class="radio is-one-quarter">
			      <input type="radio" name="question" checked="true">
			      Escolha Única
			    </label>
			    <label class="radio is-one-quarter">
			      <input type="radio" name="question">
			      Númerico
			    </label>
			    <label class="radio is-one-quarter">
			      <input type="radio" name="question" checked="true">
			      Múltipla escolha
			    </label>
			    <label class="radio is-one-quarter">
			      <input type="radio" name="question" checked="true">
			      Texto Aberto
			    </label>
			  </div>
			</div>
			<div class="field - column is-one-quarter">
			  <label class="label">Equipe</label>
			  <div class="control">
			    <div class="select">
			      <select>
			        <option>Escolha a equipe</option>
			        <option>With options</option>
			      </select>
			    </div>
			  </div>
			</div>
			<div class="field - column is-one-quarter">
			  <label class="label">Permissões</label>
			  <div class="control">
			    <div class="select">
			      <select>
			        <option>Visualizar</option>
			        <option>Vizualizar e responder</option>
			      </select>
			    </div>
			  </div>
			</div>
	   </div>
	   <div class="container is-widescreen">
		  <div class="notification">
			    <div class="field - column is-half">
				  <label class="label">Pergunta</label>
				  <div class="control">
		    		<input class="input " type="text" placeholder="Pergunta">
		          </div>
				</div>
				<div class="field column is-half is-horizontal">
				  <div class="field-label is-normal">
				    <label class="label">Opção:</label>
				  </div>
				  <div class="field-body">
				    <div class="field">
				      <div class="control">
				        <input class="input " type="text" placeholder="e.g. Partnership opportunity">
				      </div>
				    </div>
				  </div>
				</div>
				
				<div class="field column is-one-quarter is-pulled-right ">
		            <div class="control is-pulled-right">
		              <button class="button is-dark is-fullwidth ">Nova Opção</button>
		            </div>
	           </div>
         </div>
	  </div>
	  <div class="field column is-half is-pulled-right ">
		            <div class="control is-pulled-right column is-half">
		              <button class="button is-outlined is-fullwidth ">Nova Pergunta</button>
		            </div>
		            <div class="control is-pulled-right column is-half">
		              <button class="button is-dark is-fullwidth ">Finalizar Pergunta</button>
		            </div>
	  </div>
	</div>
</template>

<script>
export default {
  name: 'criarForm'
}
</script>
<style scoped></style>