
```
+----+-------------+----------+------------+-------+-----------------------+-----------------------+---------+------+-------+----------+------------------------------------+
| id | select_type | table    | partitions | type  | possible_keys         | key                   | key_len | ref  | rows  | filtered | Extra                              |
+----+-------------+----------+------------+-------+-----------------------+-----------------------+---------+------+-------+----------+------------------------------------+
```
- id：数据表的读取顺序
  - id大的优先
  - id相等，以从上到下的顺序读取
  
- select_type：数据的读取方式：
  - simple = 简单的读取，不包含任何复杂查询（子查询或者union）
  - primary = 读取复杂查询（子查询或者union）最后操作的表
  - subquery = 读取子查询涉及的表
  - derived = 读取存放子查询结果的派生表
  - union = 读取union关键字之后的表
  - union result = 读取存放union结果的临时表

- table：操作的表
  - derived3，指的是id=3的子查询结果产生派生表

- type：最好到最差：system>const>eq_ref>ref>range>index>all
    - system：const且表只有一条记录
    - const：通过索引一次就找到了，主键或者唯一索引
    - eq_ref：唯一性索引扫描，每个索引键只有一条记录
    - ref：非唯一性索引扫描，每个索引键可能会匹配多条记录，匹配某个单独值
    - range：检索指定范围的行
    - index: 全索引扫描
    - all：全表扫描

- possible_keys：可能使用到的索引

- key：最终使用到的索引，如果为null，则没有使用索引

- key_len：表示索引中使用的字节数，表示索引字段的最大可能长度，并非实际使用长度

- ref：显示索引的哪一列被使用，有可能是null或者const

- rows：预计扫描的行数

- extra：包含不在其他列展示但十分重要的额外信息
    - using filesort：mysql无法利用索引完成的排序
    - using temporary：使用了临时表保存了中间结果，常见于order by和group by
    - using index：使用覆盖索引
    - using where：使用where条件
