<template>
  <div class="demo">
    <el-container class="demoContainer">
      <el-header>
        <div class="bk-head">
<!--          <a style="float:left;" class="tooher" @click="tosc">统计</a>-->
<!--          <a style="float:left;margin-left: 10px;" class="tooher" >|</a>-->
<!--          <a style="float:left;margin-left: 10px;" class="tooher" @click="tomanager">管理</a>-->
<!--          <a style="float:left;margin-left: 10px;" class="tooher" v-show="this.userid">|</a>-->
<!--          <a style="float:left;margin-left: 10px;" v-show="this.userid" class="tooher" @click="logout">退出</a>-->
          <a class="wangcrtitle">随便聊聊</a>
<!--          <el-button type="primary" plain style="float:right;margin-top: 10px;" @click="loginDialogVisible = true" v-show="!this.userid">登录</el-button>-->
<!--          <a v-show="this.userid" class="userinfo" @click="logout">{{this.userid}}</a>-->
        </div>
      </el-header>
      <el-main>
        <div class="demoMain">
          <el-row>
            <el-col :span="24">
              <div>
              <el-select v-model="choseType" placeholder="请选择ai对话类型" style="width:100%" clearable>
                <el-option
                  v-for="item in answerType"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
              </div>
            </el-col>

            <el-col :span="24">
              <div style="margin-top: 10px">
                <el-input
                  type="textarea"
                  :autosize="{ minRows: 2, maxRows: 4}"
                  placeholder="请输入你的想法"
                  maxlength="200"
                  show-word-limit
                  v-model="msg">
                </el-input>
              </div>
            </el-col>
            <el-col :span="24">
              <div  style="margin-top: 10px">
                <el-button type="primary" style="width:100%;font-weight: bold;" @click="sendMsg" :loading="searchLoading">发 送 消 息</el-button>
              </div>
            </el-col>
            <el-col :span="24">
              <div v-if="historyList.length > 0" style="margin-top: 10px" class="answer-card">
                <el-card class="box-card" shadow="never">
                  <div slot="header" class="clearfix">
                    <span>对话列表</span>
                    <el-button style="float: right; padding: 3px 0" type="text" @click="clearMsg">清空</el-button>
                  </div>
                  <el-card v-for="item in historyList" class="box-card" shadow="hover" style="margin-bottom: 5px">
                    <a class="answer-text">{{item.role}} : </a>
                    <a class="answer-text">{{item.msg}}</a>
                  </el-card>
                </el-card>
              </div>
            </el-col>
          </el-row>

        </div>
      </el-main>
    </el-container>

  </div>
</template>

<script>
const qs = require('qs') //引入序列化功能
import {CHAT_TYPE} from './fb'
export default {
  name: 'answer',
  components: {},
  props: {},
  data() {
    return {
      IP:'http://127.0.0.1:29977',
      // IP:'http://chaoran.red:8081',
      answerType:[],
      choseType:'/answer/chat/all',
      msg:'',
      // 对话历史
      historyList:[],
      searchLoading: false,
    }
  },
  computed: {},
  watch: {},
  created() {
    this.answerType = CHAT_TYPE
  },
  mounted() {
  },
  methods: {
    // 发送消息
    sendMsg(){
      if(this.choseType != null && this.msg.length > 0){
        this.searchLoading = true
        // 将输入的消息插入历史
        const me = {
          role : '我',
          msg : this.msg
        }
        this.historyList.push(me)
        // 调用接口对话ai
        this.$request.post(this.IP + this.choseType,{"msg":this.msg})
          .then((res) => {
            // 成功 将返回结果插入历史
            console.log(res)
            const ai = {
              role: 'AI',
              msg: res.data
            }
            this.historyList.push(ai)
            // 清空消息
            this.msg = ''
            this.searchLoading = false
          }).catch((err) =>{
            console.log(err)
            this.searchLoading = false
            const ai = {
              role: 'AI',
              msg: '我遇到了问题，请重新尝试！'
            }
            this.historyList.push(ai)
            this.msg = ''
        })
      }else{
        this.$message({
          message: '请确认选择语言模型和想法',
          type: 'warning'
        });
      }
    },
    // 清空历史
    clearMsg(){
      this.historyList = []
    },
  },
}
</script>
<style lang="css" scoped>
.bk-head{

}
.bk-top{

}
.bk-main{
  margin-top: 5px;
}
.bk-foot{
  margin-top: 5px;
}
.bk-font{
  font-family: '微软雅黑';
  color: #333;
  font-weight: bold;
}
.bk-message{
  width: 50%;
  margin: 10px;
}
.answer-card{

}
.answer-text{
  color: black;
  font-family: '微软雅黑';
  font-size: medium;
}
/deep/ .el-message-box{
  width: 220px;
}
.userinfo{
  float:right;
  /*margin-top: 1px;*/
  font-family: '微软雅黑';
  color: #333;
  font-size: larger;
  font-weight: 800;
}
.demo {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
.demoContainer {
  height: 100%;
}
.el-header,
.el-footer {
  /*background-color: #7aa1e3;*/
  background: linear-gradient(to bottom right,  #116df8, #7aa1e3);
  color: #333;
  text-align: center;
  line-height: 60px;
}
.el-main {
  background-color: #e9eef3;
  color: #333;
  /* text-align: center; */
  /* line-height: 160px; */
}
.demoMain {
  /*margin-left: 200px;*/
  width: 100%;

}
.tooher{
  font-family: '微软雅黑';
  color: #333;
  font-weight: bold;
  font-size: large;
}
.demoOperation {
  margin-bottom: 10px;
}
.wangcrtitle {
  font-family: '微软雅黑';
  color: #ffffff;
  font-size: larger;
  font-weight: 800;
}
</style>
<style>
.el-message-box{
  width: 220px;
}
</style>
