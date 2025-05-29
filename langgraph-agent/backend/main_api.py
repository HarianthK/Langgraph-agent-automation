# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from fastapi import Request
# from main import workflow

# app = FastAPI()

# # Allow frontend to access backend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # ✅ Updated request model


# class AgentRequest(BaseModel):
#     street: str
#     city: str
#     state: str
#     business_description: str


# @app.post("/run")
# async def run_agent(request: AgentRequest):
#     result = await workflow.ainvoke({
#         "street": request.street,
#         "city": request.city,
#         "state": request.state,
#         "business_description": request.business_description
#     })
#     return {
#         "success": True,
#         "result": result
#     }

# # Dummy form (optional for dev UI)
# templates = Jinja2Templates(directory="templates")


# @app.get("/dummy-form", response_class=HTMLResponse)
# async def get_dummy_form(request: Request):
#     return templates.TemplateResponse("form.html", {"request": request})

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from main import workflow

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AgentRequest(BaseModel):
    street: str
    city: str
    state: str
    business_description: str


@app.post("/run")
async def run_agent(request: AgentRequest):
    result = await workflow.ainvoke({
        "street": request.street,
        "city": request.city,
        "state": request.state,
        "business_description": request.business_description
    })
    return {
        "success": True,
        "result": result
    }

templates = Jinja2Templates(directory="templates")


@app.get("/dummy-form", response_class=HTMLResponse)
async def get_dummy_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})
