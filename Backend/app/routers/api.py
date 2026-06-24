from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from app.utils.email import send_contact_notification, is_configured

router = APIRouter(prefix="/api")


class ContactForm(BaseModel):
    name: str
    email: str
    project_type: str
    message: str


@router.post("/contact")
async def contact(form: ContactForm):
    sent = await send_contact_notification(
        name=form.name,
        email=form.email,
        project_type=form.project_type,
        message=form.message,
    )

    if sent:
        return {"ok": True, "message": "Thank you! We'll be in touch within 24 hours."}

    if not is_configured():
        return {
            "ok": True,
            "message": "Thank you! We'll be in touch within 24 hours.",
            "note": "Email delivery not configured. Your message was logged.",
        }

    return {"ok": False, "message": "Failed to send. Please try again later."}
