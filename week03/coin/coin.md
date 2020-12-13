# 题目 
张三给李四通过网银转账 100 极客币，现有数据库中三张表：

一张为用户表，包含用户 ID 和用户名字，另一张为用户资产表，包含用户 ID 用户总资产，
第三张表为审计用表，记录了转账时间，转账 id，被转账 id，转账金额。

## 请合理设计三张表的字段类型和表结构；
### 用户表
| 列名 | 含义 |  类型 |
| -- | -- |  -- |
| user_id | 用户id | int，主键，递增  |
| user_name | 用户姓名 |  varchar |
```
create table user ( user_id int not null auto_increment primary key  ,user_name varchar(30) ) ;
```
### 用户资产表
| 列名 | 含义 | 类型 |
| -- | -- | -- |
| user_id | 用户id | int，主键 |
| user_assets | 用户总资产 | double |
```
create table balance ( user_id int not null primary key, user_assets double );
```
### 审计用表
| 列表 | 含义 | 类型 |
| -- | -- | -- |
| time | 转账时间 | Timestamp|
| from_id | 转账id | int |
| to_id | 被转账id | int |
| amount | 转账金额 | double |
```
 create table trans ( time timestamp, from_id int , to_id int, amount double);
```

## 请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性。
因为目前没有比较好的思路，所以没有下手写代码，正在学习中
考虑用事务执行，但是是否满足高于100怎么也写到事务中，不太清楚怎么解决，待寻找到解决办法后进行补充
如果先读然后再进行转账，有可能另外一个请求在这次读之后进行的转账，造成事故
也期望指导一下