"""
routes/contact.py - Contact page and HTMX form handler.
"""
import os
import re
import smtplib
import traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from fasthtml.common import A, Div, Form, H2, H5, Input, P, Section, Span, Textarea, Title
from faststrap import Badge, Card, Col, Container, FormErrorSummary, FormGroup, Icon, Row
from faststrap.presets import LoadingButton
from starlette.requests import Request

from components.ui.footer import portfolio_footer
from components.ui.layout import page_banner
from components.ui.navbar import portfolio_navbar
from data import OWNER, SOCIAL_LINKS
from services.supabase_data import save_contact_message


def _field_error(errors: dict[str, str], field: str) -> str | None:
    return errors.get(field)


def _contact_form(
    errors: dict[str, str] | None = None,
    values: dict[str, str] | None = None,
) -> Div:
    """Contact form wrapped in a single stable HTMX swap target."""
    errors = errors or {}
    values = values or {}

    return Div(
        Form(
            FormErrorSummary(
                errors,
                title="Please correct the highlighted fields",
                variant="danger",
                show_field_names=False,
                cls="mb-3",
            ) if errors else "",
            Div(
                FormGroup(
                    Input(
                        type="text",
                        name="name",
                        value=values.get("name", ""),
                        placeholder="e.g. Jane Smith",
                        cls="form-control",
                        required=True,
                        id="contact-name",
                    ),
                    label="Full Name",
                    required=True,
                    error=_field_error(errors, "name"),
                    is_invalid="name" in errors,
                ),
                FormGroup(
                    Input(
                        type="email",
                        name="email",
                        value=values.get("email", ""),
                        placeholder="jane@example.com",
                        cls="form-control",
                        required=True,
                        id="contact-email",
                    ),
                    label="Email Address",
                    required=True,
                    help_text="Use an inbox I can reply to.",
                    error=_field_error(errors, "email"),
                    is_invalid="email" in errors,
                ),
                FormGroup(
                    Input(
                        type="text",
                        name="subject",
                        value=values.get("subject", ""),
                        placeholder="How can I help you?",
                        cls="form-control",
                        required=True,
                        id="contact-subject",
                    ),
                    label="Subject",
                    required=True,
                    error=_field_error(errors, "subject"),
                    is_invalid="subject" in errors,
                ),
                FormGroup(
                    Textarea(
                        values.get("message", ""),
                        placeholder="Tell me about your project or inquiry...",
                        name="message",
                        rows=5,
                        cls="form-control",
                        required=True,
                        id="contact-message",
                    ),
                    label="Message",
                    required=True,
                    error=_field_error(errors, "message"),
                    is_invalid="message" in errors,
                ),
                cls="portfolio-contact-form",
            ),
            LoadingButton(
                Icon("send"),
                " Send Message",
                endpoint="/contact/send",
                method="post",
                target="#contact-form-area",
                variant="warning",
                cls="w-100 text-dark fw-bold",
                hx_swap="outerHTML",
            ),
        ),
        id="contact-form-area",
    )


def _contact_info_card() -> Div:
    """Left dark info card with contact details and social links."""
    info_rows = [
        ("telephone-fill", "Phone", OWNER["phone"], f"tel:{OWNER['phone']}"),
        ("envelope-fill", "Email", OWNER["email"], f"mailto:{OWNER['email']}"),
        ("linkedin", "LinkedIn", "linkedin.com/in/banjisegun", OWNER["linkedin"]),
        ("github", "GitHub", "banjisegun99", OWNER["github"]),
        ("geo-alt-fill", "Location", OWNER["location"], None),
    ]

    rows = [
        Div(
            Div(Icon(icon), cls="icon-wrap"),
            Div(
                Span(label, cls="portfolio-eyebrow d-block"),
                (
                    A(
                        text,
                        href=href,
                        cls="text-white text-decoration-none hover-gold small",
                        target="_blank" if href.startswith("http") else None,
                    )
                    if href
                    else Span(text, cls="text-muted-dark small")
                ),
            ),
            cls="portfolio-contact-info-row",
        )
        for icon, label, text, href in info_rows
    ]

    social_icons = Div(
        *[
            A(
                Icon(sl["icon"]),
                href=sl["href"],
                cls="portfolio-contact-social-icon me-2",
                target="_blank",
                rel="noopener noreferrer",
                aria_label=sl["label"],
            )
            for sl in SOCIAL_LINKS
        ],
        cls="d-flex flex-wrap mt-3",
    )

    return Div(
        H5("Get in Touch", cls="text-white fw-bold mb-4"),
        *rows,
        P("I typically respond within 24-48 hours.", cls="text-muted-dark small mt-2"),
        social_icons,
        cls="portfolio-contact-info-card p-3 p-md-4",
    )


def _availability_badge() -> Badge:
    return Badge(
        Span(cls="pulse-dot"),
        " ",
        OWNER["availability"],
        variant="warning",
        cls="text-dark portfolio-pulse-badge",
    )


def _success_card(name: str) -> Div:
    return Div(
        Card(
            Icon("check-circle-fill", style="font-size:3rem;color:#22c55e;"),
            H2("Message Sent!", cls="fw-bold mt-3 mb-2"),
            P(f"Thanks {name}! I'll get back to you within 24-48 hours.", cls="text-muted mb-4"),
            A("Send another message", href="/contact", cls="btn btn-outline-warning"),
            cls="portfolio-contact-success text-center",
            body_cls="py-5",
        ),
        id="contact-form-area",
    )


def setup_contact_routes(app) -> None:
    @app.get("/contact")
    def contact_page():
        return (
            Title("Contact - Segun Banji"),
            portfolio_navbar("/contact"),
            page_banner(
                "Get in Touch",
                "Available for consulting, data projects, and speaking engagements.",
                breadcrumbs=[("Home", "/"), ("Contact", None)],
                extra=_availability_badge(),
            ),
            Section(
                Container(
                    Row(
                        Col(_contact_info_card(), span=12, lg=4),
                        Col(
                            Div(_contact_form(), cls="portfolio-contact-form-shell p-3 p-md-4"),
                            span=12,
                            lg=8,
                        ),
                        cls="g-4 align-items-start",
                    ),
                ),
                cls="section-white py-5 px-2 px-md-0",
            ),
            portfolio_footer(),
        )

    @app.post("/contact/send")
    async def contact_send(request: Request):
        form = await request.form()
        values = {
            "name": str(form.get("name", "")).strip(),
            "email": str(form.get("email", "")).strip(),
            "subject": str(form.get("subject", "")).strip(),
            "message": str(form.get("message", "")).strip(),
        }

        errors: dict[str, str] = {}
        if not values["name"]:
            errors["name"] = "Full name is required."
        if not values["email"] or not re.match(r"[^@]+@[^@]+\.[^@]+", values["email"]):
            errors["email"] = "A valid email address is required."
        if not values["subject"]:
            errors["subject"] = "Subject is required."
        if not values["message"]:
            errors["message"] = "Please include a message."

        if errors:
            return _contact_form(errors=errors, values=values)

        save_contact_message(values)

        try:
            smtp_host = os.getenv("SMTP_HOST", "")
            smtp_port = int(os.getenv("SMTP_PORT", "587"))
            smtp_user = os.getenv("SMTP_USER", "")
            smtp_pass = os.getenv("SMTP_PASS", "")
            owner_email = os.getenv("OWNER_EMAIL", OWNER["email"])

            if smtp_host and smtp_user:
                msg = MIMEMultipart("alternative")
                msg["Subject"] = f"[Portfolio] {values['subject']}"
                msg["From"] = smtp_user
                msg["To"] = owner_email
                msg["Reply-To"] = values["email"]

                body = (
                    f"Name: {values['name']}\n"
                    f"Email: {values['email']}\n\n"
                    f"Subject: {values['subject']}\n\n"
                    f"Message:\n{values['message']}"
                )
                msg.attach(MIMEText(body, "plain"))

                with smtplib.SMTP(smtp_host, smtp_port) as server:
                    server.starttls()
                    server.login(smtp_user, smtp_pass)
                    server.sendmail(smtp_user, owner_email, msg.as_string())
        except Exception:
            traceback.print_exc()

        return _success_card(values["name"])
