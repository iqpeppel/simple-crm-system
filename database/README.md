# 数据库说明

## 脚本说明

- `select-food-info.sql` ：从数据库查询`fid, fname, fcid, fprice` 四列的所有元素。

## 表结构

参照完整性

![](./readme_img/数据库结构.png)

表结构 sql

```sql

CREATE TABLE IF NOT EXISTS "food_order" (
  "oid" TEXT NOT NULL,
  "did" TEXT,
  "fid" TEXT NOT NULL,
  "fcount" TEXT(255),
  "muid" TEXT(255),
  "time" TEXT(255),
  "fenliang" TEXT(255),
  "kouwei" TEXT(255),
  "call_time" TEXT,
  "print_time" TEXT(255),
  "end_time" TEXT(255),
  "status" TEXT(255),
  PRIMARY KEY ("oid", "fid"),
  FOREIGN KEY ("fid") REFERENCES "food" ("fid")
);

CREATE TABLE IF NOT EXISTS "food" (
  "fid" TEXT NOT NULL,
  "fname" TEXT(255),
  "fcid" TEXT(255),
  "fprice" TEXT(255),
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
  PRIMARY KEY ("fid"),
  FOREIGN KEY ("fcid") REFERENCES "food_category" ("fcid")
);

CREATE TABLE IF NOT EXISTS "food_category" (
  "fcid" TEXT NOT NULL,
  "fcname" TEXT(255),
  PRIMARY KEY ("fcid")
);
```