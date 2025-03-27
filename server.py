import os

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/css", StaticFiles(directory="css"), name="css")
app.mount("/js", StaticFiles(directory="js"), name="js")
templates = Jinja2Templates(directory="views")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="terminal.html")


@app.get("/resume")
async def get_resume():
    headers = {"Content-Disposition": "inline; filename=Savage_Evan-Resume.pdf"}
    return FileResponse(
        "Savage_Evan-Resume.pdf", media_type="application/pdf", headers=headers
    )

@app.get("/my-resume", response_class=HTMLResponse)
async def embed_resume(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="resume.html",
    )

@app.get("/me")
async def get_profile():
    return FileResponse("me.jpg", media_type="image/jpeg")

@app.get("/profile-image", response_class=HTMLResponse)
async def embed_profile(request: Request):
    return HTMLResponse(
        content='<img src="/me" alt="Profile Image" style="max-width: 70%; height: auto;" />',
        status_code=200,
    )
@app.get("/contact", response_class=HTMLResponse)
async def embed_contact(request: Request):
    return HTMLResponse(
        content="""
        <div>
        <h2>Phone #: +1 (402) 575-1039</h2>
        <hr>
        <h2>Email: <a href="mailto:contact@evansavage.me">contact@evansavage.me</a></h2>
        <hr>
        <h2>LinkedIn: <a href="https://LinkedIn.com/in/evan-savage">https://linkedin.com/in/evan-savage</a></h2>
        <h2>Github: <a href="https://github.com/evansnavage">https://github.com/evansnavage</a></h2>
        </div>""",
        status_code=200,
    )

@app.get("/rhodium", response_class=HTMLResponse)
async def rhodium(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="rhodium.html",
    )

@app.get("/alchemy-alley", response_class=HTMLResponse)
async def alchemy_alley(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="alchemy_alley.html",
    )




@app.get("/folder/personal", response_class=HTMLResponse)
async def get_folder_personal(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="personal_folder.html",
    )
@app.get("/folder/projects", response_class=HTMLResponse)
async def get_folder_projects(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="projects_folder.html",
    )

@app.get("/favicon")
async def get_icon():
    return FileResponse("favicon.ico", media_type="image/ico")