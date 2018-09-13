主键是一个特殊的索引
索引必须是唯一的
优点：查询快
缺点：增加了物理开销
原则：多使用的字段，小数据类型，避免null

操作，单列索引
组合索引

where 条件1 and 条件2 or 条件3
原则：建立过索引的放在前面，等值的放前面，范围放后面，and放前面
or放后面
创建索引，create index indexname on mytable(uersname(lenth));
多个索引用逗号分隔即可 

删除索引：
    drop index [indexname] on mytable
查看索引：
    show index from table_name

调试(索引之前)：
1.开启时间检测：set profiling=1;
2.执行查询语句
3.查看查询时间 show profiles

调试(索引之后)：
1.创建索引：create index titleIndex on areas(title(20))
1.开启时间检测：set profiling=1;
2.执行查询语句
3.查看查询时间 show profiles
