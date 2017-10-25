<template>
  <div class="columns">
    <div class="column is-half">
      <div>
        <p class="is-size-2 has-text-weight-semibold">Visualização de Gráfico</p>
      </div>
      <div class="has-vmargin-50">
        <div class="select">
          <select>
            <option>Selecione uma equipe</option>
            <option v-for="team in teams"
                    :key="team">{{team}}</option>
          </select>
        </div>
      </div>

    </div>
    <div class="column is-half">
      <div class="box">
        <v-radar-chart :data="data"></v-radar-chart>
      </div>
    </div>
  </div>
</template>

<script>
import RadarChart from './charts/RadarChart'

function generateRandomColor() {
  return "#" + ((1 << 24) * Math.random() | 0).toString(16);
}

function generateRandomData(length, max) {
  return [... new Array(length)].map(() => (Math.random() * max));
}

function generateConstructoArray(length) {
  return [... new Array(length)].map((item, index) => `Constructo ${index + 1}`);
}

function generateMembersArray(length, constructos, max) {
  return [... new Array(length)].map((item, index) => ({
    label: `Member ${index + 1}`,
    backgroundColor: 'transparent',
    borderColor: generateRandomColor(),
    data: generateRandomData(constructos, max)
  }));
}

export default {
  components: {
    'v-radar-chart': RadarChart,
  },
  data() {
    const max = 1;
    const constructos = 12;
    const members = 6;
    return {
      teams: ['Equipe 1', 'Equipe 2', 'Equipe 3'],
      data: {
        labels: generateConstructoArray(constructos),
        datasets: generateMembersArray(members, constructos, max),
      }
    };
  },
}
</script>

<style lang="scss" scoped>
#app .container {
  margin: 0 auto;
}
</style>
