from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

COMMAND_RESPONSES = {}

def generate_help_prompt():
    help_text = "Available commands:\n"
    for command, description in COMMAND_RESPONSES.items():
        # Find the longest command name
        max_length = max(len(cmd) for cmd in COMMAND_RESPONSES.keys())
        help_text += f"    <strong style='display: inline-block; min-width: {max_length + 2}ch;'>{command}</strong> {description[0]}\n"
    return help_text

def generate_commands():
    for filename in os.listdir("./commands"):
        if filename.endswith(".info"):
            command_name = filename[:-5]
            with open(os.path.join("./commands", filename), "r") as file:
                read_file = file.read()
                sections = read_file.split("#!")
                description = ""
                response = ""
                for section in sections:
                    if section.startswith("Description:"):
                        description = section.split("Description:")[1].strip()
                    elif section.startswith("Response:"):
                        response = section.split("Response:")[1].strip()
                COMMAND_RESPONSES[command_name] = (description, response)

generate_commands()
COMMAND_RESPONSES["help"] = "Shows the help message, but you shouldn't be able to see this...",generate_help_prompt()

app = FastAPI()
app.mount("/css", StaticFiles(directory="css"), name="css")
templates = Jinja2Templates(directory="views")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="terminal.html")
@app.get("/resume")
async def get_pdf():
    headers = {
        "Content-Disposition": "inline; filename=Savage_Evan-Resume.pdf"
    }
    return FileResponse("Savage_Evan-Resume.pdf", media_type="application/pdf", headers=headers)
@app.get("/me")
async def get_profile():
    return FileResponse("me.jpg", media_type="image/jpeg")
@app.get("/terminal-command/", response_class=HTMLResponse)
async def process_command(command: str = "help"):
    ### Exceptions to standard
    if command == "clear":
        return HTMLResponse('<meta http-equiv="refresh" content="0;" />')
    if command == "resume":
        return HTMLResponse('<meta http-equiv="refresh" content="0; url=/resume" />')
    if command == "welcome" or command == "help":
        generate_commands()
    ### Normal command handling
    try:
        return f"<p>{COMMAND_RESPONSES[command][1]}</p>"
    except KeyError:
        return f"<p>Did not find a command matching: `{command}`, check `help` for the list of possible commands.</p>"
