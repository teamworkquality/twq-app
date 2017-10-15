<script>
import { Radar } from 'vue-chartjs'

export default {
  extends: Radar,
  name: 'v-radar-chart',
  props: ['data', 'options'],
  mounted() {
    this.renderChart(this.data, this.options)
  }
}
</script>
