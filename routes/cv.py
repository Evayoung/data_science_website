"""
CV page (/cv) and PDF download (/cv/download).
"""
from pathlib import Path

from fasthtml.common import (
    A, Div, H2, H3, H5, Hr, Img, Li, P, Section, Span, Title, Ul,
)
from faststrap import Button, Col, Container, Icon, Progress, Row

from components.ui.footer import portfolio_footer
from components.ui.navbar import portfolio_navbar
from data import (
    CERTIFICATIONS, CV_SKILLS, EDUCATION, EXPERIENCE, LANGUAGES, OWNER,
    PROJECTS, SOFT_SKILLS, refresh_data,
)


def _cv_download_bar() -> Div:
    """Sticky bar just below navbar with download and print actions."""
    return Div(
        Container(
            Div(
                Span(f"Curriculum Vitae - {OWNER['name']}", cls="text-muted small me-auto"),
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
        (OWNER["phone"], "telephone-fill", f"tel:{OWNER['phone']}"),
        (OWNER["email"], "envelope-fill", f"mailto:{OWNER['email']}"),
        (OWNER["location"], "geo-alt-fill", None),
        ("linkedin.com/in/banjisegun", "linkedin", OWNER["linkedin"]),
    ]

    contact_divs = [
        Div(
            Icon(icon, cls="text-warning flex-shrink-0"),
            A(label, href=href, cls="cv-contact-row-text") if href else Span(label, cls="cv-contact-row-text"),
            cls="cv-contact-row",
        )
        for label, icon, href in contact_rows
    ]

    skill_bars = [
        Div(
            Div(
                Span(sk["name"]),
                Span(f"{sk['level']}%"),
                cls="portfolio-cv-skill-label",
            ),
            Progress(sk["level"], variant="warning", cls="portfolio-cv-skill-bar"),
            cls="mb-3",
        )
        for sk in CV_SKILLS
    ]

    return Col(
        Div(
            Div(
                Img(
                    src=OWNER.get("profile_image", ""),
                    alt=OWNER["name"],
                    cls="portfolio-profile-photo mb-3",
                    style="width:130px;height:130px;",
                ),
                cls="text-center",
            ),
            H5(OWNER["name"], cls="text-center text-white mb-0"),
            P(OWNER["title"], cls="cv-title text-center mb-3"),
            Hr(cls="cv-gold-hr"),
            Div(
                Span("Contact", cls="portfolio-cv-section-heading d-block mb-2"),
                *contact_divs,
                cls="mb-4",
            ),
            Hr(cls="cv-gold-hr"),
            Div(
                Span("Core Skills", cls="portfolio-cv-section-heading d-block mb-3"),
                *skill_bars,
                cls="mb-4",
            ),
            Hr(cls="cv-gold-hr"),
            Div(
                Span("Languages", cls="portfolio-cv-section-heading d-block mb-2"),
                *[P(lang, cls="text-muted small mb-1") for lang in LANGUAGES],
                cls="mb-2",
            ),
            Hr(cls="cv-gold-hr"),
            Div(
                Span("Soft Skills", cls="portfolio-cv-section-heading d-block mb-2"),
                P(" | ".join(SOFT_SKILLS), cls="text-muted small mb-0"),
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

    summary = Div(
        section_heading("Profile Summary"),
        P(OWNER["summary"], cls="text-muted small", style="line-height:1.7;"),
        cls="mb-4",
    )

    exp_items = []
    for exp in EXPERIENCE:
        highlights = [
            Li(item, cls="portfolio-timeline-desc small mb-1")
            for item in exp.get("highlights", [])[:3]
        ]
        exp_items.append(
            Div(
                Span(exp["dates"], cls="portfolio-timeline-date text-muted small"),
                H3(exp["role"], cls="portfolio-timeline-role fs-6"),
                Span(
                    f"{exp['org']} - {exp.get('location', '')}".strip(" -"),
                    cls="portfolio-timeline-org d-block small",
                ),
                P(exp["description"], cls="portfolio-timeline-desc small mb-0"),
                Ul(*highlights, cls="ps-3 mt-2 mb-0") if highlights else "",
                cls="portfolio-timeline-item",
            )
        )

    experience_section = Div(
        section_heading("Work Experience"),
        *exp_items,
        cls="mb-4",
    )

    edu_items = []
    for edu in EDUCATION:
        detail_bits = []
        if edu.get("gpa"):
            detail_bits.append(f"GPA: {edu['gpa']}")
        if edu.get("honors"):
            detail_bits.append(f"Honors: {edu['honors']}")
        edu_items.append(
            Div(
                Span(edu["year"], cls="portfolio-timeline-date text-muted small"),
                H3(edu["degree"], cls="portfolio-timeline-role fs-6"),
                Span(
                    f"{edu['institution']} - {edu.get('location', '')}".strip(" -"),
                    cls="portfolio-timeline-org d-block small",
                ),
                P(" | ".join(detail_bits), cls="portfolio-timeline-desc small mb-0")
                if detail_bits else "",
                cls="portfolio-timeline-item",
            )
        )

    education_section = Div(
        section_heading("Education"),
        *edu_items,
        cls="mb-4",
    )

    project_items = [
        Div(
            Span(project.get("year", ""), cls="portfolio-timeline-date text-muted small"),
            H3(project["title"], cls="portfolio-timeline-role fs-6"),
            Span(", ".join(project["tools"]), cls="portfolio-timeline-org d-block small"),
            P(project["description"], cls="portfolio-timeline-desc small mb-0"),
            cls="portfolio-timeline-item",
        )
        for project in PROJECTS[:5]
    ]

    projects_section = Div(
        section_heading("Selected Projects"),
        *project_items,
        cls="mb-4",
    )

    cert_items = [
        Div(
            Icon("check-circle-fill", cls="text-warning me-2 flex-shrink-0"),
            Span(cert, cls="small text-muted"),
            cls="d-flex align-items-start mb-2",
        )
        for cert in CERTIFICATIONS
    ]

    certs_section = Div(
        section_heading("Certifications & Training"),
        *cert_items,
    )

    return Col(
        Div(
            summary,
            experience_section,
            projects_section,
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
        refresh_data()
        nav = portfolio_navbar("/cv")
        footer = portfolio_footer()
        return (
            Title(f"CV - {OWNER['name']}"),
            nav,
            _cv_download_bar(),
            Section(
                Container(
                    Div(
                        Row(_sidebar_col(), _main_col(), cls="g-0"),
                        cls="portfolio-cv-doc mx-auto my-5",
                    ),
                ),
                cls="section-off-white py-3 px-2 px-md-0",
            ),
            footer,
        )

    @app.get("/cv/download")
    def cv_download():
        refresh_data()
        from fasthtml.common import FileResponse

        pdf_path = Path("static/cv/cv.pdf")
        if not pdf_path.exists():
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
                            A("Back to CV", href="/cv", cls="text-warning fw-bold"),
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
