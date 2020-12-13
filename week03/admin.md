# 题目
## 在 Linux 环境下，安装 MySQL5.6 以上版本，修改字符集为UTF8mb4 并验证，新建一个数据库 testdb，并为该数据库增加远程访问的用户。

### 将修改字符集的配置项、验证字符集的 SQL 语句作为作业内容提交
```
#修改
alter database testdb character set utf8mb4;

验证
show variables like '%character%';
```
###  将增加远程用户的 SQL 语句作为作业内容提交
```
GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';
```




