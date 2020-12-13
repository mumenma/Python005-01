# 题目
## 使用 MySQL 官方文档，学习通过 sql 语句为上题中的 id 和 name 增加索引，并验证。

```
create index table2_id on Table2(id);
create index table2_id on Table2(id);

CREATE TABLE `Table1` (
  `id` int DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  KEY `table1_id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

## 根据执行时间，增加索引以后是否查询速度会增加？请论述原因，并思考什么样的场景下增加索引才有效。
会增加
通过平衡树结构进行查找，减少时间复杂度，会减少查询时间，增大查询速度
