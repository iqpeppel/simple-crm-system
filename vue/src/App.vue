<template >
  <h1 style="color: #67C23A;text-align: center;border-bottom:2px solid #67C23A">推荐系统</h1>
  <el-row :gutter="18">
    <el-col :span="4"></el-col>
    <el-col :span="6">
      <p>价格</p>
      <el-input-number
          :precision="2" :step="0.1" :min="0"
          size="large"
      v-model="price"
      type="text"
      placeholder="￥"
    />
    </el-col>
    <el-col :span="6">
      <p>类别(70-90)</p>
      <el-input
      size="large"
      v-model="cid"
      type="text"
      placeholder="商品类别"
      :prefix-icon="CollectionTag"
    />
    </el-col>
    <el-col :span="4">
      <p> <br></p>
      <el-button type="success" @click="submit" :icon="Search" id="search">搜索</el-button>
    </el-col>
  </el-row>

    <div id="content" style="margin:30px; border:2px solid #67C23A; border-radius: 10px ;min-height: 36px;">
      <!--具体的每个商品-->
      <el-row :gutter="12">
        <el-col :span="4" v-for="item in content" :key="item.id">
          <el-card shadow="hover">
            <p>商品名：{{ item.gname }}</p>
            <p>商品号：{{ item.gnum }}</p>
            <p>价格：{{ item.gprice }}</p>
          </el-card>
        </el-col>
      </el-row>
    </div>
</template>
<style>
/* 其他样式 */
@import "./assets/styles.css";
</style>
<script>
import { Goods,Search,CollectionTag } from '@element-plus/icons-vue';
import {ElMessage} from "element-plus";
import axios from 'axios';
export default {
  data(){
    return {
      Search,
      Goods,
      CollectionTag,
      price : '',
      cid : '',
      goodname : '',
      content :[]
    }
  },
  methods:{
    submit() {
            this.content=[]
            const dataToPost = {
              name: this.goodname,
              class_id:this.cid,
              price: this.price.toString(),
            };

            // 将数据转换为 JSON 字符串
            const jsonData = JSON.stringify(dataToPost);
            console.log(jsonData);

            const instance = axios.create({
          baseURL: 'api/crm/', // 设置基础URL
          //baseURL:''
          timeout: 5000, // 设置请求超时时间为5秒
          headers: {
            'Content-Type': 'application/json',
            // 如果需要设置其他默认请求头，可以在这里添加
          },
        });
        instance.post('/',  jsonData )
          .then(response => {
            console.log('请求成功', response.data);
            ElMessage.success("请求成功")
            const responseData = response.data;
            const jsonString = JSON.stringify(responseData);
            const goodList = JSON.parse(jsonString);

            for (let i = 0; i < 20; i++) {
            // 获取商品信息
            const currentGood = goodList.tui_list[i];

            // 将商品信息添加到content列表中
            this.content.push({
              id: this.content.length + 1,
              gname: currentGood[0],
              gnum: currentGood[1],
              gprice: currentGood[2]
            });
          }

          })
          .catch(error => {
            console.error('请求失败', error);
            ElMessage.error("连接超时")
          });

    
  }
  }
}
</script>