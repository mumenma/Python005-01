# MySQL
三个版本：企业版、社区版、MariaDB  安装要用社区版
## 控制台
* 进入mysql  mysql -u root -p
* 离开   quit
* use testdb  切换到testdb这个数据库
* show tables; 查看目前数据库下的所有表
* show create table book 可以查看对应的book这个表的创建语句
* 

# yum的使用

# 不同的连接方式

# ORM
# 可以有的数据类型
Integer
String
DateTime
Flot
Decimal
Bollean
Text
# 三种配置
* ini
* yaml
* json
# sql
in 
exits
# 子查询
# join （比较常用的，前三种）
内连接
左连接
右连接（右外连接）
全连接（全外连接），mysql不支持
#  事务的特性
* 原子性
* 一致性
* 隔离性
* 持久性
# 

# 存在的疑问
### 在orm中，metadata.create_all()创建表，没有用到Base的子类，需要通过Table去定义，但是进行添加数据的时候是用到了Base的子类，这个是不是表明我要创建表和添加数据要分别对表结构进行定义，这个在我的感知里面是有些冗余的问题的，感觉不是那么的特别的智能，还是我哪里用错了
### 咱们可以对MySQL设置是否是事务性的，对于咱们正常开发因为咱们一般是控制哪些语句是事务的哪些是非事务的，那么是不是一般都要把MySQL那块改成非事务型的
### 咱们一般在开发环境，是开启调试模式的，对于生产环境是关闭调试模式的，对于APP开发可以区分debug和release来区分要不要有对应的调试功能，那么对于Python是否有什么好的办法根据不同的环境设置是否开启调试模式，要不每次上线前都要检查是否已经关闭了调试模式，感觉对于发布是存在一定的风险的
### 