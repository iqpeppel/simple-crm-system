# simple-crm-system
simple-crm-system

## 代码工作流程

![](./readme_img/代码工作流程.png)

## 项目架构

![](./readme_img/项目架构.png)

## 项目结构

```txt
│  LICENSE
│  README.md
│
└─database
    │  select-food-info.sql
    │  README.md
    │
    └─db-source
            main.sql
            crm.sqlite3

```
## fastapi相关
用到的包：
starlette==0.27.0
fastapi==0.104.1
tortoise-orm==0.20.0
pydantic==2.4.2
uvicorn==0.24.0
![](./readme_img/请求.png)


### 数据库相关 `./database`

- `./database/` 目录存放可能用到的 sql 语句文件。
- `./database/README.md` 为数据库和 sql 脚本说明。
- `./database/db-source/` 存放数据库文件和备份 sql 文件。



