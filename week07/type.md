区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：


| | 含义| 容器序列/扁平序列 |  可变序列/不可变序列|
| --- | --- | --- | ---| 
| list | 列表 | 容器序列 | 可变 |
| tuple | 元组 | 容器序列 | 不可变 |
| str | 字符串 | 扁平序列 | 不可变 |
| dict | 字典 | 不是序列 | 可变 |
| collections.deque | 双向队列 | 容器序列 | 可变序列 |
| collections.namedtuple | 带命名的元组 | 容器序列  |  不可变|
| collections.counter | 计数器 | 不是序列 | |
| int | 整形  | | 不可变|
| float  | 浮点型 | | 不可变 |
| memoryview | 内存视图 | 扁平序列 | |
| bytes |   |    |   |
| bytearray |   |   |   |
| array.array |   |   |   |