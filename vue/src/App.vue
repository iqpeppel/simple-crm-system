<template >
  <el-row :gutter="18">
    <el-col :span="3"><div class="grid-content ep-bg-purple" id="price" />
      <span>价格</span>
      <el-input-number
          :precision="2" :step="0.1" :min="0"
          size="large"
      v-model="price"
      class="w-50 m-2"
      type="text"
      placeholder="￥"
    />
    </el-col>
    <el-col :span="3"><div class="grid-content ep-bg-purple" id="classid" />
      <span>类别(70-90)</span>
      <el-input
      size="large"
      v-model="cid"
      class="w-50 m-2"
      type="text"
      placeholder="商品类别"
      :prefix-icon="CollectionTag"
    />
    </el-col>
<!--    <el-col :span="3"><div class="grid-content ep-bg-purple" id="goodname" />-->
<!--      <span>名称</span>-->
<!--      <el-input-->
<!--          label="商品名称"-->
<!--      size="large"-->
<!--      v-model="goodname"-->
<!--      class="w-50 m-2"-->
<!--      type="text"-->
<!--      placeholder="商品名称"-->
<!--      :prefix-icon="Goods"-->
<!--    />-->
<!--    </el-col>-->
    <el-col :span="3"><div class="grid-content ep-bg-purple" />
      <el-button type="primary" @click="submit" :icon="Search" id="search">搜索</el-button>
    </el-col>

  </el-row>
    <div id="content" style="margin-top:120px ;">
      <!--具体的每个商品-->
    <el-row :gutter="12" style="flex: auto; flex-direction: row;">
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
@import "@/assets/styles.css";
</style>
<script>
import { Goods,Search,CollectionTag } from '@element-plus/icons-vue';
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
            const responseData = response.data;
            const jsonString = JSON.stringify(responseData);
            const goodlist = JSON.parse(jsonString);

            for (let i = 0; i < 20; i++) {
            // 获取商品信息
            const currentGood = goodlist.tui_list[i];

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
          });

    
  }
  }
}
</script>