<!-- Sidebar.vue -->

<template>
    <div class="sidebar">
      <!-- 你的侧边栏内容在这里 -->
      <h1>111</h1>
      <slot></slot>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Sidebar',
    // 组件的逻辑和方法在这里
  }
  </script>
  
  <style scoped>
  /* 在这里添加样式，scoped 表示样式只在当前组件生效 */
  .sidebar {
    width: 200px;
    position: fixed;
    left: 0;
    top: 0;
    /* 其他样式设置 */
  }
  </style>
  