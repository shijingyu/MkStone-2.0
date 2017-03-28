# MkStone-2.0
MkStone2.0 Python重构版
MkStone一个纯粹的技术分享小站。分为主页，文章，资源，视频，博客，关于。
#MkStone-1.0

#概述
##开发
>技术栈 jQuery+ThinkPHP+AJAX+php-mysql
>部署工具 Centos+Apache+MySQL+PhpAdmin
###开发工具 
- 开发系统：MacOS Sierra
- 开发工具：Sublime Text3
- 命令行：iTerm2

#MkStone-2.0 当前版本
##开发
>技术栈 jQuery+Django+Mongo+AJAX
>部署工具 Centos+Virtualenv+Nginx+Mongo DB+uWSGI+Supervisor
###开发工具
- 开发系统：macOS Sierra
- 开发工具：PyCharm
- 包管理器：pip
- 数据库管理：Robomongo
##构建流程：
####1.在PyCHarm中安装virtualenv构建虚拟化独立开发环境，安装Django框架，安装MongoEngine。MongoEngin是Django的mongo的ORM接口，底层采用pymongo，安装Pycharm的Mongo插件，设置GitHub。

####2.采用Django的Auth_User管理用户，Django Admin以及Auth_User不支持Mongo等NoSQL，需要用Django-mongonaut构建。

####3.采用Django email插件发送验证用户激活邮件。

####4.增添视频会员解析接口。
####5.后台管理页面，引入Django-mongonaut，及Django Admin。
##部署：
Nginx处理静态文件，动态文件由uWSGI进行处理。
使用supervisor进程管理来管理进程。

##MkStone3.0预期

- 资源下载页面加入支付接口
- 自动化脚本，定时备份数据库到Google Drive
- 问答论坛以及会员个人中心
- GitHub Page博客引入，形成动态博客小站模式
