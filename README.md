# Easy-rasdial-v1.0
## 项目简介
本项目旨在解决以下两个问题：  
* 校园网宽带需要手动拨号上网  
* 使用平板串流电脑需要使用电脑ip，而校园网ip是动态ip（纯粹是不想买路由器），需要每次开机后手动查询
## 使用方法
### 一、配置python环境
1. 基础python  
2. yagmail：`pip install yagmail[all]`
### 二、修改文件参数
1. 在rasdialInfo.txt内输入宽带账号和密码
2. 在emailInfo.txt内输入邮箱地址、SMTP动态验证码以及对应邮箱的SMTP地址
### 三、添加任务计划程序
将rasdial.py加入计划程序即可
## 实现方法
### 宽带连接
  使用python的os包调用cmd，使用rasdial命令实现拨号
### ip查询
  同上，使用ipconfig查询ip后筛选文本
### 邮件发送
  使用yagmail包进行邮件发送
## 写在最后
  写着玩的（）
