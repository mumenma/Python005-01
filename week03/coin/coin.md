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
| user_assets | 用户总资产 | double unsigned |
```
create table balance ( user_id int not null primary key, user_assets double unsigned );
```
### 审计用表
| 列表 | 含义 | 类型 |
| -- | -- | -- |
| time | 转账时间 | datetime|
| from_id | 转账id | int |
| to_id | 被转账id | int |
| amount | 转账金额 | double |
```
 create table trans ( time datetime, from_id int , to_id int, amount double);
```

## 请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性。
见coin.py