"""
routes/about.py — About page (/about).
"""
from fasthtml.common import A, Div, H2, H3, H5, H6, Img, Li, P, Section, Span, Title, Ul
from faststrap import Badge, Card, Col, Container, Icon, ListGroup, ListGroupItem, Row

from components.ui.footer import portfolio_footer
from components.ui.layout import page_banner
from components.ui.navbar import portfolio_navbar
from data import (
    CERTIFICATIONS, EDUCATION, EXPERIENCE, OWNER,
    SOCIAL_LINKS, SPECIALISATIONS, TOOLS, refresh_data,
)


def _bio_section() -> Section:
    photo_col = Col(
        Div(
            Img(
                src=OWNER.get("profile_image", ""),
                alt=OWNER["name"],
                cls="portfolio-profile-photo mb-3",
            ),
            # Location
            Div(
                Icon("geo-alt-fill", cls="text-warning me-1"),
                Span(OWNER["location"], cls="text-muted small"),
                cls="d-flex align-items-center justify-content-center mb-3",
            ),
            # Social row
            Div(
                *[
                    A(
                        Icon(sl["icon"]),
                        href=sl["href"],
                        cls="portfolio-social-icon portfolio-social-icon-light me-2",
                        target="_blank",
                        rel="noopener noreferrer",
                        aria_label=sl["label"],
                    )
                    for sl in SOCIAL_LINKS
                ],
                cls="d-flex justify-content-center",
            ),
            cls="text-center",
        ),
        span=12, lg=4,
    )

    bio_col = Col(
        H2(f"Hi, I'm {OWNER['name']}", cls="fw-bold mb-3"),
        *[P(para, cls="text-muted mb-3", style="line-height:1.7;") for para in OWNER["bio"]],
        H5("How I work", cls="fw-bold text-dark mt-4 mb-2"),
        P(OWNER["how_i_work"], cls="text-muted", style="line-height:1.65;"),
        span=12, lg=8,
    )

    return Section(
        Container(
            Row(photo_col, bio_col, cls="gx-0 gy-5 gx-lg-5 align-items-start"),
        ),
        cls="section-white py-5",
    )


def _specialisations_section() -> Section:
    cards = []
    for spec in SPECIALISATIONS:
        cards.append(
            Col(
                Card(
                    Icon(spec["icon"], cls="text-warning mb-3", style="font-size:2rem;"),
                    H5(spec["title"], cls="fw-bold mb-2"),
                    P(spec["description"], cls="text-muted small", style="line-height:1.6;"),
                    cls="portfolio-spec-card h-100",
                    body_cls="p-3 p-md-4",
                ),
                span=12, md=4,
            )
        )

    return Section(
        Container(
            Span("What I Do", cls="portfolio-eyebrow d-block mb-2"),
            H2("Specialisations", cls="portfolio-section-heading mb-5"),
            Row(*cards, cls="g-4"),
        ),
        cls="section-off-white py-5 px-2 px-md-0",
    )


def _tools_section() -> Section:
    groups = []
    for group_name, items in TOOLS.items():
        pills = Div(
            *[
                Badge(
                    item,
                    variant="light",
                    cls="portfolio-skill-pill me-2 mb-2",
                )
                for item in items
            ],
            cls="d-flex flex-wrap mb-4",
        )
        groups.append(
            Div(
                Span(group_name, cls="portfolio-eyebrow d-block mb-2"),
                pills,
            )
        )

    return Section(
        Container(
            Span("Stack", cls="portfolio-eyebrow d-block mb-2"),
            H2("Tools & Technologies", cls="portfolio-section-heading mb-5"),
            *groups,
        ),
        cls="section-white py-5 px-2 px-md-0",
    )


def _experience_education_section() -> Section:
    # Experience timeline
    experience_items = []
    for exp in EXPERIENCE:
        experience_items.append(
            Div(
                Span(exp["dates"], cls="portfolio-timeline-date"),
                H6(exp["role"], cls="portfolio-timeline-role"),
                Span(exp["org"], cls="portfolio-timeline-org d-block"),
                P(exp["description"], cls="portfolio-timeline-desc mb-0"),
                cls="portfolio-timeline-item",
            )
        )

    exp_col = Col(
        H3("Experience", cls="fw-bold mb-4 text-dark"),
        *experience_items,
        span=12, lg=6,
    )

    # Education
    edu_cards = []
    for edu in EDUCATION:
        edu_cards.append(
            Div(
                H6(edu["degree"], cls="fw-bold mb-1 text-dark"),
                Span(edu["institution"], cls="text-warning small fw-semibold d-block"),
                Span(edu.get("location", ""), cls="text-muted small d-block"),
                Span(
                    " | ".join(
                        bit for bit in [
                            f"GPA: {edu.get('gpa')}" if edu.get("gpa") else "",
                            edu.get("honors", ""),
                        ] if bit
                    ),
                    cls="text-muted small d-block",
                ),
                Span(edu["year"], cls="text-muted small"),
                cls="portfolio-timeline-item",
            )
        )

    # Certifications
    cert_items = [
        ListGroupItem(
            Div(
                Icon("check-circle-fill", cls="portfolio-cert-icon"),
                Span(cert, cls="portfolio-cert-text"),
                cls="d-flex align-items-start gap-2",
            ),
            cls="portfolio-cert-item",
        )
        for cert in CERTIFICATIONS
    ]

    edu_col = Col(
        H3("Education", cls="fw-bold mb-4 text-dark"),
        *edu_cards,
        H3("Certifications", cls="fw-bold mt-5 mb-3 text-dark"),
        ListGroup(*cert_items, cls="portfolio-cert-list"),
        span=12, lg=6,
    )

    return Section(
        Container(
            Span("Background", cls="portfolio-eyebrow d-block mb-2"),
            H2("Experience & Education", cls="portfolio-section-heading mb-5"),
            Row(exp_col, edu_col, cls="gx-0 gy-5 gx-lg-5"),
        ),
        cls="section-off-white py-5 px-2 px-md-0",
    )


def setup_about_routes(app) -> None:
    @app.get("/about")
    def about_page():
        refresh_data()
        nav = portfolio_navbar("/about")
        footer = portfolio_footer()
        banner = page_banner(
            "About Me",
            "Get to know the person behind the data.",
            breadcrumbs=[("Home", "/"), ("About", None)],
        )
        return (
            Title(f"About {OWNER['name']} - {OWNER['title']}"),
            nav,
            banner,
            _bio_section(),
            _specialisations_section(),
            _tools_section(),
            _experience_education_section(),
            footer,
        )
