# 数据库说明

## 脚本说明

- `select-food-info.sql` ：从 `food`表查询`food.fid, food.fname, food.fcid, food.fprice` 四列的所有元素。

## 表结构

```sql
CREATE TABLE IF NOT EXISTS "food" (
  "fid" TEXT NOT NULL,
  "fcid" TEXT(255),
  "fnum" TEXT(255),
  "fname" TEXT(255),
  "ftitle" TEXT(255),
  "fprice" TEXT(255),
  "fcontent" TEXT(255),
  "fpic" TEXT(255),
  "fsort" TEXT(255),
  "ftop" TEXT(255),
  "fctime" TEXT(255),
  "status" TEXT(255),
  "salecount" TEXT(255),
  "iswaimai" TEXT(255),
  "goodsid" TEXT(255),
  "Code" TEXT(255),
  "Numb" TEXT(255),
  "departmentid" TEXT(255),
  PRIMARY KEY ("fid")
);


CREATE TABLE IF NOT EXISTS "food_order" (
  "oid" TEXT,
  "did" TEXT,
  "fid" TEXT,
  "fname" TEXT,
  "fcid" TEXT,
  "fcname" TEXT(255),
  "fprice" TEXT(255),
  "fcount" TEXT(255),
  "prices" TEXT(255),
  "muid" TEXT(255),
  "muname" TEXT(255),
  "time" TEXT(255),
  "fenliang" TEXT(255),
  "kouwei" TEXT(255),
  "call_time" TEXT,
  "print_time" TEXT(255),
  "end_time" TEXT(255),
  "status" TEXT(255),
  "goodsid" TEXT(255),
  "code" TEXT,
  "departmentid" TEXT(255),
  "isdeccount" TEXT(255),
  PRIMARY KEY ("oid", "did", "fid")
);
```