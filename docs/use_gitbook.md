## 使用GitBook整理文档

### 是什么
> GitBook是一个给予Node.js的命令行工具，支持电子书的创建、阅读和格式转换。

### 为什么
> 人生苦短，怎么简单怎么来

### 怎么做
> 1. 使用Vim编写Markdown文章
> 2. GitBook生成电子书
> 3. Git管理电子书变更
> 4. Github托管电子书

### 使用前提
> 需要确保您所使用的机器支持以上工具，以我的机子为例

1. Vim机子自带，使用命令行工具打开即可
2. 安装GitBook工具

   - 安装Node.js,[官网](https://nodejs.org/en/download/)
   - 使用npm(node包管理工具)安装gitbook-cli
```
npm install -g gitbook-cli
```
安装过程可能没有想象中那么顺利，可能遇到以下问题：
1. npm ERR! code ECONNRESET
2. npm WARN checkPermissions Missing write access to /usr/local/lib/node_modules
针对前者，参考[link](https://stackoverflow.com/questions/18419144/npm-not-working-read-econnreset)修改配置走http而不是https；针对后者，使用sudo执行命令。

