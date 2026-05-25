"""
components/ui/navbar.py — Shared portfolio navbar.
"""
from fasthtml.common import A, Div, Span
from faststrap import Button, Icon, Navbar


def portfolio_navbar(current_path: str = "/") -> Navbar:
    """Return the shared sticky dark navbar with gold accent."""

    def _is_active(path: str) -> bool:
        if path == "/":
            return current_path == "/"
        return current_path.startswith(path)

    # Brand slot: circular initials badge + name
    brand = Div(
        Div("SB", cls="portfolio-brand-badge"),
        Span("Segun Banji", cls="portfolio-brand-text"),
        cls="d-flex align-items-center text-decoration-none",
    )

    nav_items = [
        {"text": "Home",    "href": "/",        "active": _is_active("/")},
        {"text": "About",   "href": "/about",   "active": _is_active("/about")},
        {"text": "Works",   "href": "/works",   "active": _is_active("/works")},
        {"text": "CV",      "href": "/cv",      "active": _is_active("/cv")},
        {"text": "Videos",  "href": "/videos",  "active": _is_active("/videos")},
        {"text": "Contact", "href": "/contact", "active": _is_active("/contact")},
    ]

    # CV download button goes in the collapsible area after the nav links
    cv_btn = Div(
        Button(
            Icon("download"),
            " Download CV",
            variant="warning",
            size="sm",
            as_="a",
            href="/cv/download",
            cls="text-dark fw-bold ms-lg-3 mt-2 mt-lg-0",
        ),
        cls="d-flex align-items-center",
    )

    return Navbar(
        cv_btn,
        brand=brand,
        brand_href="/",
        items=nav_items,
        variant="dark",
        expand="lg",
        sticky="top",
        cls="portfolio-nav bg-black",
    )
