"""
components/ui/footer.py — Shared portfolio footer.
"""
from faststrap import FooterModern

from data import OWNER, SOCIAL_LINKS


def portfolio_footer() -> FooterModern:
    """Return the shared dark footer with brand, links, and social icons."""
    columns = [
        {
            "title": "Navigation",
            "links": [
                {"text": "Home",    "href": "/"},
                {"text": "About",   "href": "/about"},
                {"text": "Works",   "href": "/works"},
                {"text": "CV",      "href": "/cv"},
                {"text": "Videos",  "href": "/videos"},
                {"text": "Contact", "href": "/contact"},
            ],
        },
        {
            "title": "Connect",
            "links": [
                {"text": "LinkedIn", "href": OWNER["linkedin"]},
                {"text": "GitHub",   "href": OWNER["github"]},
                {"text": "Email",    "href": f"mailto:{OWNER['email']}"},
            ],
        },
    ]

    social_links = [
        {"icon": sl["icon"], "href": sl["href"]}
        for sl in SOCIAL_LINKS
    ]

    return FooterModern(
        brand="Segun Banji",
        tagline="Data Analyst & BI Expert — turning data into decisions.",
        columns=columns,
        social_links=social_links,
        copyright_text="© 2026 Segun Banji. All rights reserved.",
        bg_variant="dark",
        text_variant="light",
        cls="portfolio-footer",
    )
