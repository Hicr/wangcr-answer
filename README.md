# wangcr-answer
use chartGPT create answer

本项目前提为已有ChartGPT账号

![](./media/Snipaste_2023-03-05_17-46-17.png)

## 使用本项目

1.拉取代码

2.申请chatGPT的密钥

3.配置密钥到项目内

​	3.1. python 服务方式

```shell
vim server-source/.env

OPENAI_API_KEY = 'sk-XXXXXXXXXXXX'
```

​	3.2. node服务方式

```shell
vim ui-source/answer-ui/src/views/answer/delete.js

const KEY = "open ai 的密钥"

const IP = "代理访问地址 或openai地址"

export {
  KEY,IP
}

```

4.打包部署

- 前端

```shell
npm run build
```

- python

```
# 启动
python3 -u mian.py &
# 将依赖下载到本地
pip3 install XXX==XXX(version) -t .
```

- nginx配置

```
server {
    listen       8082;
    server_name  localhost;
    location / {
        root /media/answer;
        index  index.html index.htm;
    }
    location /answer {
    	proxy_pass http://answerServer/answer ;
    }
}
```



## 项目参考

- [使用 Python 和 ChatGPT API 开发一个智能聊天程序](https://lwebapp.com/zh/post/python-chatgpt-api)
- [ChatGPT 中文调教指南](https://github.com/PlexPt/awesome-chatgpt-prompts-zh)
- [猴子也能学会的腾讯云函数搭建 OpenAI 国内代理教程](https://github.com/Ice-Hazymoon/openai-scf-proxy#%E8%87%AA%E6%89%98%E7%AE%A1)

### GhatGPT 官方

- [API 文档](https://platform.openai.com/docs/guides/chat/introduction)

- [生成chartGPT 密钥](https://platform.openai.com/account/api-keys)

