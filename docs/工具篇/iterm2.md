# ssh使用perm文件登录服务器

```shell
# 方式一

ssh -i key.perm user@host
# 如果报错，则文perm件权限过大，需要重新设置
sudo chmod 600 key.perm


# 方式二

ssh-add -k key.perm
ssh user@host

mac系统iterm2的设置：
profiles->open profiles->edit profiles->general->command
```


# iterm2克隆会话

## Mac系统：

1. 修改iterm2的配置：
```
profiles->open profiles->edit profiles->general->working directory->reuse previous session'directory
```

1. 修改ssh配置文件:
```shell
vi ~/.ssh/config
```
添加下面三行代码：
```
host *
ControlMaster auto
ControlPath ~/.ssh/master-%r@%h:%p
```

# 避免长时间空闲而断开连接
## Mac系统：
```
profiles->open profiles->edit profiles->session->when idle,send ASCII code
```

# 参考
- [SSH使用PEM文件登录](https://blog.csdn.net/chushoufengli/article/details/96842820)
- [iterm2克隆会话](https://www.jianshu.com/p/cadb63e8cf33)