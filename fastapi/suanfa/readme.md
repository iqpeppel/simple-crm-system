## 代码说明
函数声明：
def tuijian(class_id, price):
导入该代码，传入推荐的类id和价格，返回一个list，按照货物的推荐顺序进行排序
需要的库已经写在requirement.txt中
**注**：根据源数据库，类id在**70~90**间，价格在**4.00~50.00**之间

可以调用以下代码测试模块，参数可修改：
```
class_id = 70
price = 60
result = tuijian(class_id, price)
print(result)
```

