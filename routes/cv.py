"""
routes/cv.py — CV page (/cv) and PDF download (/cv/download).
"""
from pathlib import Path

from fasthtml.common import (
    A, Div, H1, H2, H3, H5, Hr, Img, Li, P, Section, Span, Title, Ul,
)
from faststrap import Badge, Button, Col, Container, Icon, Progress, Row

from components.ui.footer import portfolio_footer
from components.ui.navbar import portfolio_navbar
from data import (
    CERTIFICATIONS, CV_SKILLS, EDUCATION, EXPERIENCE, OWNER, SOCIAL_LINKS,
)


def _cv_download_bar() -> Div:
    """Sticky bar just below navbar with download and print actions."""
    return Div(
        Container(
            Div(
                Span("Curriculum Vitae — Segun Banji", cls="text-muted small me-auto"),
                Div(
                    Button(
                        Icon("download"), " Download PDF",
                        variant="warning",
                        size="sm",
                        as_="a",
                        href="/cv/download",
                        cls="text-dark fw-bold me-2 no-print",
                    ),
                    Button(
                        Icon("printer"), " Print",
                        variant="outline-secondary",
                        size="sm",
                        onclick="window.print()",
                        cls="no-print",
                    ),
                    cls="d-flex gap-2",
                ),
                cls="d-flex align-items-center",
            ),
        ),
        cls="portfolio-cv-bar no-print",
    )


def _sidebar_col() -> Col:
    """Left dark CV sidebar: photo, name, title, contact, skills, languages."""
    contact_rows = [
        (OWNER["email"],    "envelope-fill",  f"mailto:{OWNER['email']}"),
        (OWNER["location"], "geo-alt-fill",   None),
        ("linkedin.com/in/banjisegun", "linkedin", OWNER["linkedin"]),
        ("github.com/banjisegun99",    "github",   OWNER["github"]),
    ]

    contact_divs = [
        Div(
            Icon(icon, cls="text-warning flex-shrink-0"),
            (
                A(label, href=href, cls="cv-contact-row-text")
                if href else
                Span(label, cls="cv-contact-row-text")
            ),
            cls="cv-contact-row",
        )
        for label, icon, href in contact_rows
    ]

    skill_bars = []
    for sk in CV_SKILLS:
        skill_bars.append(
            Div(
                Div(
                    Span(sk["name"], cls=""),
                    Span(f"{sk['level']}%", cls=""),
                    cls="portfolio-cv-skill-label",
                ),
                Progress(
                    sk["level"],
                    variant="warning",
                    cls="portfolio-cv-skill-bar",
                ),
                cls="mb-3",
            )
        )

    return Col(
        Div(
            # Profile photo
            Div(
                Img(
                    src="/assets/images/profile.jpeg",
                    alt="Segun Banji",
                    cls="portfolio-profile-photo mb-3",
                    style="width:130px;height:130px;",
                ),
                cls="text-center",
            ),
            H5("Segun Banji", cls="text-center text-white mb-0"),
            P(OWNER["title"], cls="cv-title text-center mb-3"),
            Hr(cls="cv-gold-hr"),
            # Contact
            Div(
                Span("Contact", cls="portfolio-cv-section-heading d-block mb-2"),
                *contact_divs,
                cls="mb-4",
            ),
            # Skills
            Hr(cls="cv-gold-hr"),
            Div(
                Span("Core Skills", cls="portfolio-cv-section-heading d-block mb-3"),
                *skill_bars,
                cls="mb-4",
            ),
            # Languages
            Hr(cls="cv-gold-hr"),
            Div(
                Span("Languages", cls="portfolio-cv-section-heading d-block mb-2"),
                P("English — Fluent", cls="text-muted small mb-1"),
                P("Yoruba — Native", cls="text-muted small mb-0"),
                cls="mb-2",
            ),
            cls="portfolio-cv-sidebar",
        ),
        span=12, lg=4,
        cls="p-0",
    )


def _main_col() -> Col:
    """Right white CV main area: summary, experience, education, certifications."""

    def section_heading(text: str) -> Div:
        return Div(
            Span(text, cls="portfolio-cv-section-heading"),
            Hr(cls="portfolio-cv-divider"),
        )

    # Profile summary
    summary = Div(
        section_heading("Profile Summary"),
        P(
            f"{OWNER['name']} is a seasoned Data Analyst and Business Intelligence Expert "
            "with 7+ years of experience helping SMEs and organisations leverage analytics "
            "to boost efficiency and profitability. Currently serving as Digital Consultant "
            "at McMoren Logistics and Data Analytics Lecturer at Midramo Institute, he "
            "combines deep technical expertise with a passion for clear data storytelling "
            "and practical education.",
            cls="text-muted small",
            style="line-height:1.7;",
        ),
        cls="mb-4",
    )

    # Experience
    exp_items = []
    for exp in EXPERIENCE:
        exp_items.append(
            Div(
                Span(exp["dates"], cls="portfolio-timeline-date text-muted small"),
                H3(exp["role"], cls="portfolio-timeline-role fs-6"),
                Span(exp["org"], cls="portfolio-timeline-org d-block small"),
                P(exp["description"], cls="portfolio-timeline-desc small mb-0"),
                cls="portfolio-timeline-item",
            )
        )

    experience_section = Div(
        section_heading("Work Experience"),
        *exp_items,
        cls="mb-4",
    )

    # Education
    edu_items = [
        Div(
            Span(edu["year"], cls="portfolio-timeline-date text-muted small"),
            H3(edu["degree"], cls="portfolio-timeline-role fs-6"),
            Span(edu["institution"], cls="portfolio-timeline-org d-block small"),
            cls="portfolio-timeline-item",
        )
        for edu in EDUCATION
    ]

    education_section = Div(
        section_heading("Education"),
        *edu_items,
        cls="mb-4",
    )

    # Certifications
    cert_items = [
        Div(
            Icon("check-circle-fill", cls="text-warning me-2 flex-shrink-0"),
            Span(cert, cls="small text-muted"),
            cls="d-flex align-items-start mb-2",
        )
        for cert in CERTIFICATIONS
    ]

    certs_section = Div(
        section_heading("Certifications"),
        *cert_items,
    )

    return Col(
        Div(
            summary,
            experience_section,
            education_section,
            certs_section,
            cls="portfolio-cv-main",
        ),
        span=12, lg=8,
        cls="p-0",
    )


def setup_cv_routes(app) -> None:
    @app.get("/cv")
    def cv_page():
        nav = portfolio_navbar("/cv")
        footer = portfolio_footer()
        return (
            Title("CV — Segun Banji"),
            nav,
            _cv_download_bar(),
            Section(
                Container(
                    Div(
                        Row(
                            _sidebar_col(),
                            _main_col(),
                            cls="g-0",
                        ),
                        cls="portfolio-cv-doc mx-auto my-5",
                    ),
                ),
                cls="section-off-white py-3 px-2 px-md-0",
            ),
            footer,
        )

    @app.get("/cv/download")
    def cv_download():
        from fasthtml.common import FileResponse
        pdf_path = Path("static/cv/cv.pdf")
        if not pdf_path.exists():
            from fasthtml.common import H2, P
            return (
                Title("CV PDF Not Found"),
                portfolio_navbar("/cv"),
                Section(
                    Container(
                        Div(
                            H2("CV PDF not available", cls="text-dark fw-bold mt-5"),
                            P(
                                "The CV PDF has not been uploaded yet. "
                                "Please drop cv.pdf into the static/cv/ folder.",
                                cls="text-muted",
                            ),
                            A("← Back to CV", href="/cv", cls="text-warning fw-bold"),
                            cls="py-5",
                        ),
                    ),
                    cls="section-white",
                ),
                portfolio_footer(),
            )
        return FileResponse(
            pdf_path,
            media_type="application/pdf",
            headers={"Content-Disposition": 'attachment; filename="Segun_Banji_CV.pdf"'},
        )
