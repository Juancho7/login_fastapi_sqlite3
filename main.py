from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from user import User
from check_password import check_user

app = FastAPI()

templates = Jinja2Templates(directory="./templates")


@app.get("/login", name="login", response_class=HTMLResponse)
@app.post("/login", name="login", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/user", name="user_index")
def user(request: Request, username: str = Form(), password: str = Form()):
    user = check_user(username, password)
    if user:
        return templates.TemplateResponse(
            "user.html", {"request": request, "user_data": user}
        )

    return RedirectResponse("/login")


@app.get("/signup", name="signup", response_class=HTMLResponse)
def signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


@app.post("/user-processing", response_class=RedirectResponse)
def user_processing(
    username: str = Form(),
    first_name: str = Form(),
    last_name: str = Form(),
    country: str = Form(),
    password: str = Form(),
):
    user_data = {
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
        "country": country,
        "password": password,
    }

    user_db = User(user_data)
    user_db.create_user()

    return RedirectResponse("/login")
