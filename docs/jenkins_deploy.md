> 一些约定

```
Jenkins所在的服务器为S1
项目部署的目标服务器S2
要部署的项目P
```
> 自动化部署流程

1. 在S1通过Git拉取P的源码
2. 在S1用Maven打成Jar包
3. 使用rsync将打好的Jar包同步到S2
4. S1通过spawn ssh连接S2
5. 连接成功后，通过send执行S2上的启动脚本
6. 启动成功后，S1断开连接

> Jenkins端的设置

1. 
![new_jenkins](https://note.youdao.com/noteshare?id=4f6d85d896cd0c4e22d236bd23f3fb43)


> <span id="jump1"> 遇到的问题 </span>

1. [hh](#jump1)
