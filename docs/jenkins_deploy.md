> 一些约定

```
Jenkins所在的服务器为S1
项目部署的目标服务器S2
目标服务器S2的IP为target_server_ip
要部署的项目P
项目P的artifactId为haibian_tsc
项目P的version为0.0.1
```
> 自动化部署流程

1. 在S1通过Git拉取P的源码
2. 在S1用Maven打成Jar包
3. 使用rsync将打好的Jar包同步到S2
4. S1通过spawn ssh连接S2
5. 连接成功后，通过send执行S2上的启动脚本
6. 启动成功后，S1断开连接

> Jenkins端的设置

1. 新建一个Jenkins构建项目
![new_jenkins](https://github.com/quinlanleuang/ThisIsMyHorse/blob/master/imgs/new_jenkins.jpg?raw=true)

2. 拉取源码的设置
![image](https://github.com/quinlanleuang/ThisIsMyHorse/blob/master/imgs/source_code_setting.jpg?raw=trueo)

3. 打包的设置
![image](https://github.com/quinlanleuang/ThisIsMyHorse/blob/master/imgs/build_setting.jpg?raw=trueo)

4. 打包后的后续操纵
![image](https://github.com/quinlanleuang/ThisIsMyHorse/blob/master/imgs/build_setting.jpg?raw=trueo)
其中有两个关键的操作jar的同步和jar包的启动，分别使用rsync和expect命令来完成。

- rsync【++注意自行替换target_server_ip++】[==notice!==](#rsync)
```
rsync -alvr --exclude=.svn --exclude=/.env target/haibian_tsc-0.0.1.jar work@target_server_ip::online/springboot/tsc-java/
```
- expect 【++注意自行替换target_server_ip++】[==notice!==](#expect)
```
expect -c "
spawn ssh work@target_server_ip
expect \"*#\"
send \"sh startup.sh restart\r\"
expect \"*#\"
send \"exit\r\"
"
```

5. S2上的startup.sh脚本 [==notice!==](#startup)
```
#!/bin/bash
#这里可替换为你自己的执行程序，其他代码无需更改
APP_NAME="haibian_tsc-0.0.1.jar"
WORK_PATH="/home/work/springboot/tsc-java" 
#使用说明，用来提示输入参数
usage() {
    echo "Usage: sh 执行脚本.sh [start|stop|restart|status]"
    exit 1
}
 
#检查程序是否在运行
is_exist(){
  pid=`ps -ef|grep $APP_NAME|grep -v grep|awk '{print $2}' `
  #如果不存在返回1，存在返回0     
  if [ -z "${pid}" ]; then
   return 1
  else
    return 0
  fi
}
 
#启动方法
start(){
  is_exist
  if [ $? -eq "0" ]; then
    echo "${APP_NAME} is already running. pid=${pid} ."
  else
    nohup ~/java/jdk1.8.0_211/bin/java -jar $APP_NAME --spring.profiles.active=test > /tmp/tsc.log 2>&1 &
    #nohup java -jar $APP_NAME --spring.profiles.active=test > /dev/null 2>&1 &
    echo "start!"
  fi
}
 
#停止方法
stop(){
  is_exist
  if [ $? -eq "0" ]; then
    kill -9 $pid
  else
    echo "${APP_NAME} is not running"
  fi  
}
 
#输出运行状态
status(){
  is_exist
  if [ $? -eq "0" ]; then
    echo "${APP_NAME} is running. Pid is ${pid}"
  else
    echo "${APP_NAME} is NOT running."
  fi
}
 
#重启
restart(){
  stop
  start
}
 
cd $WORK_PATH 
echo `pwd`
#根据输入参数，选择执行对应方法，不输入则执行使用说明
case "$1" in
  "start")
    start
    ;;
  "stop")
    stop
    ;;
  "status")
    status
    ;;
  "restart")
    restart
    ;;
  *)
    usage
    ;;
esac
```

> 值得注意的地方

1. <span id="rsync">Jar的命名是pom.xml文件中artifactId+version组合，请确保在rsync文件时填的是正确的文件名和正确的路径</span>
2. <span id="expect">请保证S1和S2支持expect通信，同时传输的命令，要注意路径是否正确</span>
3. <span id="startup">注意starup中命令的路径要正确，最好使用绝对路径，我就因为java的路径没写正确，导致在构建时stop成功执行，start却一直起不同</span>
4. 当然starup.sh的内容是可以放在expect中从S1处send给S2的，创建一个starup.sh的好处有变更时可以直接修改该文件，而不需要修改Jenkins的configure，尤其是不是所有人都有configure权限的情况下

> 参考

[使用Jenkins配置SpringBoot的自动化构建](https://blog.csdn.net/xlgen157387/article/details/78733729)

[Maven 教程](https://www.runoob.com/maven/maven-tutorial.html)

[Maven 命令](https://juejin.im/post/5bddbb5b6fb9a049a62c02e5)

[expect简易教程](https://my.oschina.net/u/561917/blog/848064)

[linux免交互登陆远程主机并执行命令(密钥对和Expect)](https://www.cnblogs.com/smail-bao/p/6170795.html)

[rsync命令](https://man.linuxde.net/rsync)
