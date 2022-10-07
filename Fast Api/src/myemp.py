from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from day09.emp_dao import EmpDaO


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/emp_list", response_class=HTMLResponse)
async def emp_list(request: Request):
    ed = EmpDaO
    emps = ed.selects()
    
    return templates.TemplateResponse("emp_list.html", {"request": request})

# uvicorn myemp:app --reload
