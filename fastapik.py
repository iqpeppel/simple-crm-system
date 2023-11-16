from starlette.requests import Request
from fastapi import FastAPI,Form,Body,Request
from starlette.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from tortoise.contrib.fastapi import register_tortoise
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from suanfa.ranked_recommend_goods import tuijian
import requests


app = FastAPI()
class ShopObject(BaseModel):
    name:str
    class_id:int
    price:int

templates = Jinja2Templates(directory="templates")

#数据库绑定

@app.get("/")
async def index(request:Request):
    return templates.TemplateResponse("post.html",{'request':request})


#前端访问ip+/crm/端口请求数据，发送Json
@app.post("/crm/")
async def tuijiancrm(shopobj:ShopObject):
    tui_list=[]
    tui_list=tuijian(shopobj.class_id,shopobj.price)
    print(tui_list)
    return {"tui_list":tui_list}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)