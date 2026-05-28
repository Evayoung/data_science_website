"""
routes/home.py — Home page (/) and API fragments.
"""
from fasthtml.common import (
    A, Div, FastHTML, H1, H2, H3, Img, P, Section, Span, Title,
)
from faststrap import (
    Badge, Button, Card, Carousel, CarouselItem, Col, Container,
    Icon, Row, Spinner, StatCard,
)
from faststrap.presets import LazyLoad

from components.ui.footer import portfolio_footer
from components.ui.navbar import portfolio_navbar
from data import OWNER, PROJECTS, SKILLS_FLAT, SOCIAL_LINKS, STATS, VIDEOS


def _hero_section() -> Section:
    """Dark hero with availability badge, headline, CTA buttons, and social icons."""
    profile_image = OWNER.get("profile_image", "")
    profile_alt_image = OWNER.get("profile_alt_image") or profile_image
    hero_background = OWNER.get("hero_background_image", "")
    # Availability badge
    avail_badge = Badge(
        Span(cls="pulse-dot"),
        " ",
        OWNER["availability"],
        variant="warning",
        cls="text-dark portfolio-pulse-badge mb-3",
    )

    # Social icon row
    social_icons = Div(
        *[
            A(
                Icon(sl["icon"]),
                href=sl["href"],
                cls="portfolio-social-icon me-2",
                target="_blank",
                rel="noopener noreferrer",
                aria_label=sl["label"],
            )
            for sl in SOCIAL_LINKS
        ],
        cls="d-flex align-items-center mt-4",
    )

    content_col = Col(
        avail_badge,
        H1(OWNER["name"], cls="portfolio-hero-name text-white mb-1"),
        P(OWNER["title"], cls="portfolio-hero-title mb-3"),
        P(OWNER["tagline"], cls="text-muted-dark mb-4", style="max-width:520px;line-height:1.65;"),
        Div(
            Button(
                "View My Work",
                variant="warning",
                as_="a",
                href="/works",
                cls="text-dark fw-bold me-2 mb-2",
            ),
            Button(
                "Download CV",
                variant="outline-warning",
                as_="a",
                href="/cv/download",
                cls="mb-2",
            ),
            cls="d-flex flex-wrap",
        ),
        social_icons,
        span=12, lg=7,
        cls="py-3",
    )

    photo_col = Col(
        Div(
            Img(
                src=profile_image,
                alt="Segun Banji",
                cls="portfolio-profile-photo",
            ),
            cls="d-flex justify-content-center align-items-center h-100 py-4",
        ),
        span=12, lg=5,
        cls="d-none d-lg-block",
    )

    return Section(
        Container(
            Row(content_col, photo_col, cls="align-items-center"),
        ),
        style=f"--portfolio-hero-bg:url('{hero_background}');" if hero_background else "",
        cls="portfolio-hero",
    )


def _showcase_section() -> Section:
    """Rotating carousel of featured projects."""
    featured = [p for p in PROJECTS if p.get("featured")][:6]

    # Fallback: use first 6 if no featured
    if not featured:
        featured = PROJECTS[:6]

    items = []
    for i, proj in enumerate(featured):
        caption = Div(
            Badge(
                proj["category"].replace("-", " ").title(),
                variant="warning",
                cls="text-dark mb-2",
            ),
            H3(proj["title"], cls="text-white fw-bold mb-1 fs-5"),
            P(proj["description"][:100] + "…", cls="text-white-50 mb-0 small"),
        )
        items.append(
            CarouselItem(
                Div(
                    Img(
                        src=proj["image"],
                        alt=proj["title"],
                        cls="d-block w-100",
                        loading="lazy",
                    ),
                    Div(caption, cls="carousel-caption d-none d-md-block"),
                ),
                active=(i == 0),
            )
        )

    carousel = Carousel(
        *items,
        ride="carousel",
        interval=3500,
        cls="portfolio-showcase-carousel",
    )

    return Section(
        Container(
            Div(
                Span("Selected Work", cls="portfolio-eyebrow d-block mb-2"),
                H2("Projects Showcase", cls="portfolio-section-heading mb-4"),
                carousel,
            ),
        ),
        cls="section-dark py-5",
    )


def _about_stats_section() -> Section:
    """Two-column: photo+bio snapshot (left) and 2×2 stat grid (right)."""
    profile_image = OWNER.get("profile_image", "")
    profile_alt_image = OWNER.get("profile_alt_image") or profile_image
    # Stats grid
    stats_grid = Div(
        Row(
            *[
                Col(
                    Div(
                        Div(
                            Span(
                                "0",
                                cls="portfolio-stat-value",
                                id=f"stat-{i}",
                                data_count_target=str(s["value"]),
                                data_count_suffix=s["suffix"],
                            ),
                            P(s["label"], cls="portfolio-stat-label"),
                        ),
                        cls="portfolio-stat-card",
                    ),
                    span=6,
                )
                for i, s in enumerate(STATS)
            ],
            cls="g-3",
        ),
        id="stats-section",
    )

    bio_col = Col(
        Div(
            Img(
                src=profile_alt_image,
                alt=OWNER["name"],
                cls="portfolio-profile-photo mb-4",
                loading="lazy",
            ),
            cls="text-center text-lg-start",
        ),
        H2("About Segun", cls="text-white fw-bold mb-3"),
        P(
            "Data Analyst and Digital Consultant with 7+ years using Excel, SQL, "
            "and Power BI to improve logistics reporting, operational efficiency, "
            "and business intelligence decisions.",
            cls="text-muted-dark mb-3",
            style="line-height:1.65;",
        ),
        Button(
            "Learn more about me",
            variant="outline-warning",
            as_="a",
            href="/about",
            cls="mt-1",
        ),
        span=12, lg=6,
    )

    stats_col = Col(stats_grid, span=12, lg=6)

    return Section(
        Container(
            Row(bio_col, stats_col, cls="align-items-center gx-0 gy-5 gx-lg-5"),
        ),
        cls="section-dark py-5",
    )


def _skills_section() -> Section:
    """Off-white section with all skills as gold-bordered pills."""
    pills = Div(
        *[
            Badge(
                skill,
                variant="light",
                cls="portfolio-skill-pill me-2 mb-2",
            )
            for skill in SKILLS_FLAT
        ],
        cls="d-flex flex-wrap",
    )

    return Section(
        Container(
            Span("Tools & Skills", cls="portfolio-eyebrow d-block mb-2"),
            H2("What I Work With", cls="portfolio-section-heading mb-4"),
            pills,
        ),
        cls="section-off-white py-5 px-2 px-md-0",
    )


def _videos_teaser_section() -> Section:
    """LazyLoad placeholder that fetches the video teaser cards."""
    return Section(
        Container(
            Span("Content", cls="portfolio-eyebrow d-block mb-2"),
            H2("Latest Videos", cls="portfolio-section-heading mb-4"),
            LazyLoad(
                endpoint="/api/home/videos-teaser",
                placeholder=Div(
                    Spinner(cls="text-warning"),
                    P("Loading videos…", cls="text-muted mt-2"),
                    cls="text-center py-5",
                ),
                cls="py-2",
            ),
        ),
        cls="section-white py-5 px-2 px-md-0",
    )


def _cta_banner() -> Section:
    """Dark contact CTA banner."""
    return Section(
        Div(
            Container(
                H2("Ready to work together?", cls="text-white fw-bold mb-3"),
                P(
                    "Let's discuss how data can solve your business challenges.",
                    cls="text-muted-dark mb-4",
                ),
                Button(
                    "Get in Touch",
                    variant="warning",
                    as_="a",
                    href="/contact",
                    cls="text-dark fw-bold px-4",
                ),
            ),
        ),
        cls="portfolio-cta-banner",
    )


def _video_teaser_cards() -> Row:
    """Return 3 video card fragments for the lazy-loaded endpoint."""
    preview = VIDEOS[:3]
    cards = []
    for v in preview:
        cards.append(
            Col(
                Div(
                    Div(
                        Div(cls="portfolio-video-thumb-bg"),
                        A(
                            Icon("play-circle-fill"),
                            href=f"https://www.youtube.com/watch?v={v['video_id']}",
                            target="_blank",
                            rel="noopener noreferrer",
                            cls="portfolio-video-play",
                            aria_label=f"Watch {v['title']} on YouTube",
                        ),
                        cls="ratio ratio-16x9 portfolio-video-thumb",
                    ),
                    Div(
                        H3(v["title"], cls="fs-6 fw-bold mb-1"),
                        P(v["description"], cls="text-muted small mb-2"),
                        Badge(
                            v["category"].replace("-", " ").title(),
                            variant="warning",
                            cls="text-dark",
                        ),
                        cls="p-3",
                    ),
                    cls="portfolio-video-card",
                ),
                span=12, md=4,
            )
        )
    return Row(*cards, cls="g-4")


def setup_home_routes(app: FastHTML) -> None:
    @app.get("/")
    def home_page():
        nav = portfolio_navbar("/")
        footer = portfolio_footer()
        return (
            Title("Segun Banji — Data Analyst & BI Expert"),
            nav,
            _hero_section(),
            _showcase_section(),
            _about_stats_section(),
            _skills_section(),
            _videos_teaser_section(),
            _cta_banner(),
            footer,
        )

    @app.get("/api/home/videos-teaser")
    def videos_teaser_fragment():
        return _video_teaser_cards()
