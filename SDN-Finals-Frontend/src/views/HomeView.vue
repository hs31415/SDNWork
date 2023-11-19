<script setup>
</script>


<template>
    <el-container>
      <el-header>
        <el-menu
            :default-active="menuActiveIndex"
            class="el-menu-demo"
            mode="horizontal"
            router
        >
          <el-menu-item index="package-operation">嗅探和发送数据包</el-menu-item>
          <el-menu-item index="query-package">统计数据包</el-menu-item>
        </el-menu>
      </el-header>

      <el-main>
        <RouterView></RouterView>
      </el-main>
    </el-container>
</template>

<script>
export default {
  methods: {

  },
  data(){
    return{
      menuActiveIndex:"0",
    }
  }
}
</script>