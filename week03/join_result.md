# 题目
以下两张基于 id 列，分别使用 INNER JOIN、LEFT JOIN、 RIGHT JOIN 的结果是什么?

Table1

| id | name |
| -- | --|
| 1 | table1_table2 |
| 2  | table1 |

Table2

| id | name |
| -- | -- |
| 1  | table1_table2 |
| 3 | table2 | 

# 回答
### INNER JOIN
#### 执行代码
```
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
INNER JOIN Table2
ON Table1.id = Table2.id;
```
#### 执行结果

| Table1.id | Table1.name | Table2.id | Table2.name |
| -- | -- | -- | -- | 
| 1 | table1_table2 | 1 | table1_table2|

### LEFT JOIN
#### 执行代码
```
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
LEFT JOIN Table2
ON Table1.id = Table2.id;
```
#### 执行结果
| Table1.id | Table1.name | Table2.id | Table2.name |
| -- | -- | -- | -- |
|    1 | table1_table2 |    1 | table1_table2 |
|    2 | table1        | NULL | NULL          |

### RIGHT JOIN 
#### 执行代码
```
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
RIGHT JOIN Table2
ON Table1.id = Table2.id;
```
#### 执行结果
| Table1.id | Table1.name | Table2.id | Table2.name |
| -- | -- | -- | -- |
|    1 | table1_table2 |    1 | table1_table2 |
| NULL | NULL          |    3 | table2        |