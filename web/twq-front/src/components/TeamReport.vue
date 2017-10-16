<template>
  <div class="columns">
    <div class="column">
      <div>
        <p class="is-size-2 has-text-weight-semibold">Visualização de Relatório</p>
      </div>
      <div class="field is-grouped">
        <div class="control">
          <div class="select">
            <select>
              <option>Data de Início</option>
            </select>
          </div>
        </div>
        <div class="control">
          <div class="select">
            <select>
              <option>Data de Finalização</option>
            </select>
          </div>
        </div>
        <div class="control">
          <div class="select">
            <select>
              <option>Equipe</option>
            </select>
          </div>
        </div>
        <label>ICC:</label>
      </div>
      <table class="table has-vmargin-50 is-bordered is-stripe is-fullwidth">
        <thead>
          <tr>
            <th>Variables</th>
            <th v-for="(item, index) in report.size"
                :key="index">{{index+1}}</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="item in report.data"
              :key="item.label">
            <td>{{item.label}}</td>
            <td v-for="value in item.data"
                :key="item.label+value"
                :class="highlight(value)">{{value}}</td>
          </tr>

        </tbody>
      </table>
      <div class="control align-right">
        <button class="button  is-dark is-medium">Exportar PDF</button>
        <button class="button  is-dark is-medium">Exportar CSV</button>
        <router-link :to="{name: 'Graphic'}">
          <button class="button  is-dark is-medium">Gerar Gráfico</button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'listarForms',
  data() {
    return {
      report: {
        size: 14,
        data: [
          {
            label: 'Communication',
            data: ['', -0.23, -0.16, '', '', '', '', 0.14, '', '', '', '', 0.13, -0.16]
          },
          {
            label: 'Coordination',
            data: [0.35, '', -0.27, 0.16, '', '', '', -0.12, '', 0.15, '', '', -.16, '']
          },
          {
            label: 'Balance of m.con.',
            data: [0.57, .27, '', '', '', '', '', 0.14, '', '', '', '', 0.13, -0.16]
          },
          {
            label: 'Mutual support',
            data: [.76, -0.23, -0.16, '', '', '', '', 0.14, '', '', '', '', 0.13, -0.16]
          },
          {
            label: 'Effort',
            data: ['', -0.23, -0.16, '', '', '', '', 0.14, '', '', '', '', 0.13, -0.16]
          },
          {
            label: 'Cohesion',
            data: ['', -0.23, -0.16, '', '', '', '', 0.14, '', '', '', '', 0.13, -0.16]
          },
          {
            label: 'Work Satisfaction',
            data: ['', -0.23, -0.16, '', '', '', '', 0.14, '', '', '', '', 0.13, -0.16]
          },
          {
            label: 'Learning',
            data: ['', -0.23, -0.16, '', '', '', '', 0.14, '', '', '', '', 0.13, -0.16]
          },
          {
            label: 'Effectiveness_TM',
            data: ['', -0.23, -0.16, '', '', '', '', 0.14, '', '', '', '', 0.13, -0.16]
          },
          {
            label: 'Efficiency_TM',
            data: ['', -0.23, -0.16, '', '', '', '', 0.14, '', '', '', '', 0.13, -0.16]
          },
          {
            label: 'Effectiveness_TL',
            data: ['', -0.23, -0.16, '', '', '', '', 0.14, '', '', '', '', 0.13, -0.16]
          },
          {
            label: 'Efficiency_TL',
            data: ['', -0.23, -0.16, '', '', '', '', 0.14, '', '', '', '', 0.13, -0.16]
          },
          {
            label: 'Effectiveness_PO',
            data: ['', -0.23, -0.16, '', '', '', '', 0.14, '', '', '', '', 0.13, -0.16]
          },
          {
            label: 'Efficiency_PO',
            data: ['', -0.23, -0.16, '', '', '', '', 0.14, '', '', '', '', 0.13, -0.16]
          },
        ]
      }
    }
  },
  methods: {
    highlight(value) {
      return {
        'has-text-info': value > 0.7,
        'has-text-danger': value < 0,
      };
    },
  }
}
</script>
<style scoped>
.align-right {
  text-align: right;
}
</style>