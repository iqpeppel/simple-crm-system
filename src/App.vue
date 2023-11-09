<template>
  <div id="price">
        <input type="text" placeholder="￥" v-model="pricespan.minprice"/>
        <p>-</p>
        <input type="text" placeholder="￥" v-model="pricespan.maxprice"/>
    </div>
    <select id="variety" v-model="classid">
        <option v-for="item in typelist" :value="item.cid" :key="item.cid">{{ item.name }}</option>
    </select>
    <button @click="submit" id="search">搜索</button>
</template>
<script>
import axios from 'axios';
export default {
  data(){
    return {
      pricespan : {
        minprice : '',
        maxprice : ''
      },
      classid : '',
      typelist : [
      {
        cid : 1,
        name : '饮料',
      },
      {
        cid : 2,
        name : '饼干'
      }]
    }
  },
  methods:{
    submit() {
          const dataToPost = {
              pricespan: this.pricespan,
              classid: this.classid
          };
          
          // 将数据转换为 JSON 字符串
          const jsonData = JSON.stringify(dataToPost)
          console.log(jsonData)
          // 定义请求的URL
          const apiUrl = 'https://api.example.com/data';  // 替换为你要请求的URL

          // 发起POST请求
          axios.post(apiUrl, jsonData)
          .then(response => {
              // 处理成功响应
              console.log('POST请求成功', response.data);
          })
          .catch(error => {
              // 处理错误
              console.error('POST请求错误', error);
          });
      }
  }
}
</script>