"""
routes/videos.py - Videos listing and HTMX filter fragments.
"""
from fasthtml.common import A, Div, H2, H3, H6, Iframe, P, Section, Span, Title
from faststrap import Badge, Card, Col, Container, Icon, Row, Tabs
from starlette.requests import Request

from components.ui.footer import portfolio_footer
from components.ui.layout import page_banner
from components.ui.navbar import portfolio_navbar
from data import OWNER, VIDEO_CATEGORIES, VIDEOS


def _video_card(v: dict) -> Card:
    """Single responsive video card."""
    return Card(
        Div(
            Iframe(
                src=f"https://www.youtube.com/embed/{v['video_id']}",
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture",
                allowfullscreen=True,
                loading="lazy",
                cls="position-absolute top-0 start-0 w-100 h-100",
                style="border:0;",
            ),
            cls="ratio ratio-16x9",
        ),
        Div(
            H6(v["title"], cls="fw-bold mb-1"),
            P(v["description"], cls="text-muted small mb-2"),
            Badge(
                v["category"].replace("-", " ").title(),
                variant="warning",
                cls="text-dark",
            ),
            cls="p-3 p-md-4",
        ),
        cls="portfolio-video-card h-100",
        body_cls="p-0",
    )


def _video_grid(category: str = "all") -> Div:
    """Return a video grid filtered by category."""
    filtered = VIDEOS if category == "all" else [
        v for v in VIDEOS if v["category"] == category
    ]

    if not filtered:
        return Div(
            Div(
                Icon("camera-video-off", style="font-size:2.5rem;color:#C9A84C;"),
                H3("No videos in this category yet", cls="mt-3 fw-bold"),
                P("Check back soon or view all videos.", cls="text-muted"),
                cls="text-center py-5",
            ),
            id="videos-grid",
        )

    return Div(
        Row(*[Col(_video_card(v), span=12, md=6) for v in filtered], cls="g-4"),
        id="videos-grid",
    )


def _filter_tabs(active_category: str = "all") -> Div:
    tabs = Tabs(
        *[
            (cat_id, cat_label, cat_id == active_category)
            for cat_id, cat_label in VIDEO_CATEGORIES
        ],
        htmx=True,
        cls="border-0",
    )

    nav = tabs.children[0]
    for item, (cat_id, _cat_label) in zip(nav.children, VIDEO_CATEGORIES):
        btn = item.children[0]
        btn.attrs["hx-get"] = f"/videos/filter?category={cat_id}"
        btn.attrs["hx-target"] = "#videos-filter-shell"
        btn.attrs["hx-swap"] = "outerHTML"
        btn.attrs["hx-push-url"] = "false"

    return Div(tabs, cls="portfolio-filter-tabs mb-4")


def _filter_shell(category: str = "all") -> Div:
    valid_categories = {cat_id for cat_id, _ in VIDEO_CATEGORIES}
    active_category = category if category in valid_categories else "all"
    return Div(
        _filter_tabs(active_category),
        _video_grid(active_category),
        id="videos-filter-shell",
    )


def _subscribe_cta() -> Section:
    return Section(
        Container(
            H2("Enjoy the content?", cls="text-white fw-bold mb-3"),
            P(
                "Subscribe to the channel for regular tutorials, walkthroughs, and data tips.",
                cls="text-muted-dark mb-4",
            ),
            A(
                Icon("youtube"),
                " Subscribe on YouTube",
                href=OWNER["youtube_channel"],
                target="_blank",
                cls="btn btn-danger fw-bold px-4",
            ),
        ),
        cls="portfolio-cta-banner text-center",
    )


def setup_videos_routes(app) -> None:
    @app.get("/videos")
    def videos_page():
        return (
            Title("Videos - Segun Banji"),
            portfolio_navbar("/videos"),
            page_banner(
                "Videos",
                "Data walkthroughs, tutorials, and tips.",
                breadcrumbs=[("Home", "/"), ("Videos", None)],
            ),
            Section(
                Container(
                    Span("Watch & Learn", cls="portfolio-eyebrow d-block mb-2 mt-2"),
                    H2("Video Library", cls="portfolio-section-heading mb-4"),
                    _filter_shell("all"),
                ),
                cls="section-white py-5 px-2 px-md-0",
            ),
            _subscribe_cta(),
            portfolio_footer(),
        )

    @app.get("/videos/filter")
    def videos_filter(request: Request):
        category = request.query_params.get("category", "all")
        return _filter_shell(category)
