<script>
export default{
  methods:{
    getSketchValue(src, dst, sport, dport) {
      fetch('http://127.0.0.1:8000/sketch', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          src: src,
          dst: dst,
          sport: sport,
          dport: dport,
        }),
      })
      .then(response => response.json())
      .then(data => {
        console.log('Query successful!');
        console.log('Sketch value:', data);
        this.sketchValues.push(data);  // 将返回的值添加到数组中
      })
      .catch(error => {
        console.error('Error getting sketch value:', error);
      });
    },
    getAllSketachValue(){
      this.sketchValues = [];//这里可以写循环，但是老懒狗了
      this.getSketchValue('10.0.0.1', '10.0.0.2', '1234', '1234')
      this.getSketchValue('10.0.0.1', '10.0.0.3', '1234', '1234')
      this.getSketchValue('10.0.0.1', '10.0.0.4', '1234', '1234')
      this.getSketchValue('10.0.0.1', '10.0.0.5', '1234', '1234')
      this.getSketchValue('10.0.0.1', '10.0.0.6', '1234', '1234')
      this.getSketchValue('10.0.0.1', '10.0.0.7', '1234', '1234')
      this.getSketchValue('10.0.0.1', '10.0.0.8', '1234', '1234')

      this.getSketchValue('10.0.0.2', '10.0.0.1', '1234', '1234')
      this.getSketchValue('10.0.0.2', '10.0.0.3', '1234', '1234')
      this.getSketchValue('10.0.0.2', '10.0.0.4', '1234', '1234')
      this.getSketchValue('10.0.0.2', '10.0.0.5', '1234', '1234')
      this.getSketchValue('10.0.0.2', '10.0.0.6', '1234', '1234')
      this.getSketchValue('10.0.0.2', '10.0.0.7', '1234', '1234')
      this.getSketchValue('10.0.0.1', '10.0.0.8', '1234', '1234')
      
      this.getSketchValue('10.0.0.3', '10.0.0.2', '1234', '1234')
      this.getSketchValue('10.0.0.3', '10.0.0.1', '1234', '1234')
      this.getSketchValue('10.0.0.3', '10.0.0.4', '1234', '1234')
      this.getSketchValue('10.0.0.3', '10.0.0.5', '1234', '1234')
      this.getSketchValue('10.0.0.3', '10.0.0.6', '1234', '1234')
      this.getSketchValue('10.0.0.3', '10.0.0.7', '1234', '1234')
      this.getSketchValue('10.0.0.3', '10.0.0.8', '1234', '1234')

      this.getSketchValue('10.0.0.4', '10.0.0.2', '1234', '1234')
      this.getSketchValue('10.0.0.4', '10.0.0.3', '1234', '1234')
      this.getSketchValue('10.0.0.4', '10.0.0.1', '1234', '1234')
      this.getSketchValue('10.0.0.4', '10.0.0.5', '1234', '1234')
      this.getSketchValue('10.0.0.4', '10.0.0.6', '1234', '1234')
      this.getSketchValue('10.0.0.4', '10.0.0.7', '1234', '1234')
      this.getSketchValue('10.0.0.4', '10.0.0.8', '1234', '1234')

      this.getSketchValue('10.0.0.5', '10.0.0.2', '1234', '1234')
      this.getSketchValue('10.0.0.5', '10.0.0.3', '1234', '1234')
      this.getSketchValue('10.0.0.5', '10.0.0.4', '1234', '1234')
      this.getSketchValue('10.0.0.5', '10.0.0.1', '1234', '1234')
      this.getSketchValue('10.0.0.5', '10.0.0.6', '1234', '1234')
      this.getSketchValue('10.0.0.5', '10.0.0.7', '1234', '1234')
      this.getSketchValue('10.0.0.5', '10.0.0.8', '1234', '1234')

      this.getSketchValue('10.0.0.6', '10.0.0.2', '1234', '1234')
      this.getSketchValue('10.0.0.6', '10.0.0.3', '1234', '1234')
      this.getSketchValue('10.0.0.6', '10.0.0.4', '1234', '1234')
      this.getSketchValue('10.0.0.6', '10.0.0.5', '1234', '1234')
      this.getSketchValue('10.0.0.6', '10.0.0.1', '1234', '1234')
      this.getSketchValue('10.0.0.6', '10.0.0.7', '1234', '1234')
      this.getSketchValue('10.0.0.6', '10.0.0.8', '1234', '1234')

      this.getSketchValue('10.0.0.7', '10.0.0.2', '1234', '1234')
      this.getSketchValue('10.0.0.7', '10.0.0.3', '1234', '1234')
      this.getSketchValue('10.0.0.7', '10.0.0.4', '1234', '1234')
      this.getSketchValue('10.0.0.7', '10.0.0.5', '1234', '1234')
      this.getSketchValue('10.0.0.7', '10.0.0.6', '1234', '1234')
      this.getSketchValue('10.0.0.7', '10.0.0.1', '1234', '1234')
      this.getSketchValue('10.0.0.7', '10.0.0.8', '1234', '1234')

      this.getSketchValue('10.0.0.8', '10.0.0.2', '1234', '1234')
      this.getSketchValue('10.0.0.8', '10.0.0.3', '1234', '1234')
      this.getSketchValue('10.0.0.8', '10.0.0.4', '1234', '1234')
      this.getSketchValue('10.0.0.8', '10.0.0.5', '1234', '1234')
      this.getSketchValue('10.0.0.8', '10.0.0.6', '1234', '1234')
      this.getSketchValue('10.0.0.8', '10.0.0.7', '1234', '1234')
      this.getSketchValue('10.0.0.8', '10.0.0.1', '1234', '1234')
    }
  },
  computed: {
    sortedSketchValues() {
      // 使用数组的slice方法创建一个新的数组，以避免直接修改原始数组
      return this.sketchValues.slice().sort((a, b) => b.Value - a.Value);
    }
  },
  data(){
    return{
      queryInfo:{},
      sketchValues: []  // 新增一个数组用于存储返回的值
    }
  }
}
</script>

<template>
  <el-button type="primary" style="margin-left: 1rem" @click="getAllSketachValue()">统计数据包</el-button>

  <div v-for="(value, index) in sortedSketchValues" :key="index">
    {{ index + 1 }}. Sketch value: {{ value }}
  </div>
</template>

<style scoped>

</style>