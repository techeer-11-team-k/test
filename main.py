# fastapi import
from fastapi import FastAPI, Request
from enum import Enum
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

# fastapi 객체 생성
app = FastAPI()

# 템플릿 설정
templates = Jinja2Templates(directory="templates")

items_db = [{"doro" : "도로"}, {"rong" : "롱"}, {"dorodoro" : "도로도로"}]


# Path 오퍼레이션 생성. Path는 도메인명을 제외하고, /로 시작하는 URL 부분.
# 만약 url이 http://example.com/items/foo 라면, path는 /items/foo
# Operation은 GET, POST, PUT/PATCH, DELETE 등의 HTTP 메소드이다.

@app.get("/", summary="여기엔 요약", tags=["여기엔 태그"])
async def root():
    '''
    이 부분의 텍스트는 소스코드의 주석 부분이지만 /docs에서도 설명으로 들어가게 됩니다.
    '''
    return {"message": "Hello, World!"}


# Path Parameter 예시 코드
@app.get("/items/{item_id}", summary="item_id를 인자로 받는 라우터")
async def read_item(item_id : int): 
    return {"item_id" : item_id}


# Path 파라미터값과 특정 지정 Path가 충돌되어 422에러가 발생함.
# /docs에서 직접 테스트 해 보세요.
@app.get("/items/all", summary='충돌!')
async def all_item():
    return {"message" : "all items"}


# Query Parameter 예시 코드
# 예 : localhost:8081/query?skip=0&limit=2
# skip = 0, limit = 2라면, items_db[0: (0+2)]를 읽겠죠.
@app.get("/query")
async def read_query(skip : int = 0, limit: int = 2): # 초기값을 지정한 것입니다. 다른 인자로 바꿀 수 있어요.
    return items_db[skip : skip + limit]


# 여기서부터 1월 5일의 과제를 시작합니다..

@app.get("/chanyoung")
async def chanyoung():
    return {"message": "chanyoung"}

@app.get("/chanyoung/html")
async def chanyoung_html(
    request: Request, name: str = "chanyoung",
    desc: str = "안녕하세요, chanyoung"
):

    return templates.TemplateResponse(
        "example.html", {"request": request, "name": name, "desc": desc}
    )


@app.get("/hangjung")
async def hangjung():
    return {"message": "hangjung"}

@app.get("/hangjung/html")
async def hangjung_html(request: Request, name: str = "항중",desc: str = "주제가 안나오네요"):
    return templates.TemplateResponse("hangjung.html", {"request": request, "name": name, "desc": desc})



@app.get("/sua")
async def sua():
    return {"message": "sua"}
@app.get("/sua/html")
async def sua_html(request: Request, name: str="조수아", desc: str="안녕하세요, 저는 조수아"):
    return templates.TemplateResponse("example.html", {"request": request, "name": name, "desc": desc})