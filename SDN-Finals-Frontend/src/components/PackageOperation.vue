<script>
export default {
  name: "Queries",
  methods:{
    sendPackages() {
      fetch('http://127.0.0.1:8000/send')
          .then(() => {
            ElMessage.success("Send packages successfully!");
            console.log('Sent packages successfully');
          })
          .catch(error => {
            ElMessage.error('Error sending packages:', error);
            console.error('Error sending packages:', error);
          });
    },

    startSniffing() {
      fetch('http://127.0.0.1:8000/sniff')
          .then(() => {
            ElMessage.success("Started sniffing packets");
            console.log('Started sniffing packets');
          })
          .catch(error => {
            ElMessage.error('Error starting sniffing:', error);
            console.error('Error starting sniffing:', error);
          });
    },

    clearSketch() {
      fetch('http://127.0.0.1:8000/clear')
          .then(() => {
            ElMessage.success("Cleared sketch successfully'");
            console.log('Cleared sketch successfully');
          })
          .catch(error => {
            ElMessage.error('Error clearing sketch:', error);
            console.error('Error clearing sketch:', error);
          });
    },
  }
}
</script>

<template>
<div>
          <el-button type="primary" @click="sendPackages">发送数据包</el-button>
          <el-button type="primary" @click="startSniffing">开始嗅探</el-button>
          <el-button type="primary" @click="clearSketch">清空数据</el-button>
</div>
<div >拓扑图</div>
<iframe src="http://127.0.0.0:8181/index.html#/topology" width="1200px" height="1000px" frameborder="1"></iframe>
</template>

<style scoped>

</style>