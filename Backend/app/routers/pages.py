from pathlib import Path
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory=str(Path(__file__).resolve().parent.parent.parent.parent / "Frontend" / "templates"))


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/demo/web-development", response_class=HTMLResponse)
async def demo_web_dev(request: Request):
    return templates.TemplateResponse("demos/web-dev.html", {"request": request, "title": "Website Development", "tag": "Modern Web Development", "subtitle": "Live site built with Next.js, Tailwind, optimized for speed & SEO."})


@router.get("/demo/ai-agents", response_class=HTMLResponse)
async def demo_ai_agents(request: Request):
    return templates.TemplateResponse("demos/ai-agents.html", {"request": request, "title": "AI Agents & Automation", "tag": "AI Agent System", "subtitle": "Autonomous AI agents handling real business workflows in real-time."})


@router.get("/demo/chatbots", response_class=HTMLResponse)
async def demo_chatbots(request: Request):
    return templates.TemplateResponse("demos/chatbots.html", {"request": request, "title": "Chatbots", "tag": "AI Chatbot Interface", "subtitle": "Intelligent conversational AI that qualifies leads and provides 24/7 support."})


@router.get("/demo/saas-mvp", response_class=HTMLResponse)
async def demo_saas_mvp(request: Request):
    return templates.TemplateResponse("demos/saas-mvp.html", {"request": request, "title": "SaaS MVP Development", "tag": "SaaS Dashboard", "subtitle": "Rapid-built SaaS dashboard with real metrics, analytics, and user management."})


@router.get("/demo/business-automation", response_class=HTMLResponse)
async def demo_biz_auto(request: Request):
    return templates.TemplateResponse("demos/biz-auto.html", {"request": request, "title": "Business Automation", "tag": "Automation Pipeline", "subtitle": "End-to-end automated workflow processing invoices, approvals, and payments."})


@router.get("/demo/maintenance-support", response_class=HTMLResponse)
async def demo_maint_support(request: Request):
    return templates.TemplateResponse("demos/maint-support.html", {"request": request, "title": "Maintenance & Support", "tag": "System Health Monitor", "subtitle": "24/7 monitoring dashboard with real-time system health and incident response."})


@router.get("/demo/login-portal", response_class=HTMLResponse)
async def demo_login_portal(request: Request):
    return templates.TemplateResponse("demos/login-portal.html", {"request": request, "title": "Login Portal", "tag": "Secure Authentication", "subtitle": "Modern login interface with social authentication, validation, and responsive design."})
