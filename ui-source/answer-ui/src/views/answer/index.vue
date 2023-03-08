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
<!--                <el-button type="primary" style="width:100%;font-weight: bold;" @click="sendMsg" :loading="searchLoading">发 送 消 息</el-button>-->
                <el-button type="primary" style="width:100%;font-weight: bold;" @click="sendMsgWithNode" :loading="searchLoading">发 送 消 息</el-button>
              </div>
            </el-col>
<!--            <el-col :span="24">-->
<!--              <div  style="margin-top: 10px">-->
<!--                <el-button type="primary" style="width:100%;font-weight: bold;" @click="openDemo" :loading="searchLoading">测 试 按 钮</el-button>-->
<!--              </div>-->
<!--            </el-col>-->
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
import { Configuration,OpenAIApi} from "openai"
export default {
  name: 'answer',
  components: {},
  props: {},
  data() {
    return {
      IP:'http://127.0.0.1:29977',
      // IP:'https://api.openai.com',
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
    async openDemo(){
      const configuration = new Configuration({
        apiKey: "sk-XXXX",
      });
      const openai = new OpenAIApi(configuration);
      const response = await openai.listEngines();
    },
    sendMsgWithNode(){
      if(this.choseType != null && this.msg.length > 0){
        this.searchLoading = true
        // 将输入的消息插入历史
        const me = {
          role : '我',
          msg : this.msg
        }
        // debugger
        const sys1 = this.systemMsg(this.choseType)
        console.log(sys1)
        var chat_data
        if(this.choseType === '/answer/chat/all'){
          chat_data = {
            "model": "gpt-3.5-turbo",
            "messages": [
              {"role": "system", "content": "You are a helpful assistant."},
              {"role": "system", "content": "接下来的对话都用中文回答"},
              {"role": "user", "content": this.msg}
            ]
          }
        }else{
          chat_data = {
            "model": "gpt-3.5-turbo",
            "messages": [
              {"role": "system", "content": "You are a helpful assistant."},
              {"role": "system", "content": "接下来的对话都用中文回答"},
              {"role": "system", "content": sys1},
              {"role": "user", "content": this.msg}
            ]
          }
        }


        this.historyList.push(me)
      // https://api.openai.com/v1/chat/completions
        this.$request.post(this.IP + "/v1/chat/completions",chat_data,{
          headers:{
            'Content-Type' : 'application/json',
            'Authorization':'Bearer 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'
          }
        }).then((res) => {
          // 成功 将返回结果插入历史
          console.log(res)
          const ai = {
            role: 'AI',
            msg: res.data.choices[0].message.content
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
    // 根据不同的模型返回不同的前置条件
    systemMsg(str){
      if(str){
        if(str === "/answer/chat/originality"){
          return "根据人们的意愿产生数字创业点子。例如，当我说“我希望在我的小镇上有一个大型购物中心”时，你会为数字创业公司生成一个商业计划，其中包含创意名称、简短的一行、目标用户角色、要解决的用户痛点、主要价值主张、销售和营销渠道、收入流来源、成本结构、关键活动、关键资源、关键合作伙伴、想法验证步骤、估计的第一年运营成本以及要寻找的潜在业务挑战。将结果写在降价表中。"
        }else if(str === "/answer/chat/psychologist"){
          return "我想让你担任心理健康顾问。我将为您提供一个寻求指导和建议的人，以管理他们的情绪、压力、焦虑和其他心理健康问题。您应该利用您的认知行为疗法、冥想技巧、正念练习和其他治疗方法的知识来制定个人可以实施的策略，以改善他们的整体健康状况。我的第一个请求是“我需要一个可以帮助我控制抑郁症状的人。”"
        }else if(str === "/answer/chat/stack"){
          return "我想让你充当 stackoverflow 的帖子。我会问与编程相关的问题，你会回答应该是什么答案。我希望你只回答给定的答案，并在不够详细的时候写解释。不要写解释。当我需要用英语告诉你一些事情时，我会把文字放在大括号内{like this}。我的第一个问题是“如何将 http.Request 的主体读取到 Golang 中的字符串”"
        }else if(str === "/answer/chat/time"){
          return "我要你做我的时间旅行向导。我会为您提供我想参观的历史时期或未来时间，您会建议最好的事件、景点或体验的人。不要写解释，只需提供建议和任何必要的信息。我的第一个请求是“我想参观文艺复兴时期，你能推荐一些有趣的事件、景点或人物让我体验吗？”"
        }else if(str === "/answer/chat/it"){
          return "我希望你充当 IT 专家。我会向您提供有关我的技术问题所需的所有信息，而您的职责是解决我的问题。你应该使用你的计算机科学、大数据、网络基础设施和 IT 安全知识来解决我的问题。在您的回答中使用适合所有级别的人的智能、简单和易于理解的语言将很有帮助。用要点逐步解释您的解决方案很有帮助。尽量避免过多的技术细节，但在必要时使用它们。我希望您回复解决方案，而不是写任何解释。我的第一个问题是“我的笔记本电脑出现蓝屏错误”。"
        }else if(str === "/answer/chat/law"){
          return "我想让你做我的法律顾问。我将描述一种法律情况，您将就如何处理它提供建议。你应该只回复你的建议，而不是其他。不要写解释。我的第一个请求是“我出了车祸，不知道该怎么办”。"
        }else if(str === "/answer/chat/cook"){
          return "我要你做我的私人厨师。我会告诉你我的饮食偏好和过敏，你会建议我尝试的食谱。你应该只回复你推荐的食谱，别无其他。不要写解释。我的第一个请求是“我是一名素食主义者，我正在寻找健康的晚餐点子。”"
        }else if(str === "/answer/chat/title"){
          return "我想让你充当一个花哨的标题生成器。我会用逗号输入关键字，你会用花哨的标题回复。"
        }
      }else{
        return ""
      }
    },
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
