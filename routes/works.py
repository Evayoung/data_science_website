"""
routes/works.py - Works listing, HTMX filter fragments, and project detail pages.
"""
from fasthtml.common import A, Div, H1, H2, H5, Img, P, Section, Span, Title
from faststrap import Badge, Card, Col, Container, Icon, Row, Tabs
from starlette.requests import Request

from components.ui.footer import portfolio_footer
from components.ui.layout import page_banner
from components.ui.navbar import portfolio_navbar
from data import PROJECTS, WORKS_CATEGORIES


def _project_card(proj: dict) -> A:
    """Build a full-link project card."""
    img_wrap = Div(
        *(
            [Img(src=proj["image"], alt=proj["title"], loading="lazy")]
            if proj.get("image")
            else [Div(Icon("bar-chart-fill"), cls="portfolio-project-img-placeholder")]
        ),
        *(
            [
                Badge(
                    "Featured",
                    variant="warning",
                    cls="text-dark position-absolute top-0 start-0 m-2",
                )
            ]
            if proj.get("featured")
            else []
        ),
        Div("View Project ->", cls="portfolio-project-overlay"),
        cls="portfolio-project-img-wrap position-relative",
    )

    tool_pills = Div(
        *[
            Badge(t, variant="light", cls="portfolio-skill-pill me-1 mb-1")
            for t in proj["tools"]
        ],
        cls="d-flex flex-wrap",
    )

    body = Div(
        Div(
            H5(proj["title"], cls="fw-bold mb-1 fs-6 text-dark"),
            Badge(
                proj["category"].replace("-", " ").title(),
                variant="warning",
                cls="text-dark mb-2",
            ),
        ),
        P(proj["description"][:120] + "...", cls="text-muted small mb-2"),
        tool_pills,
        cls="p-3 p-md-4",
    )

    return A(
        img_wrap,
        body,
        href=f"/works/{proj['slug']}",
        cls="portfolio-project-card d-block h-100",
    )


def _project_grid(category: str = "all") -> Div:
    """Return project cards filtered by category."""
    filtered = PROJECTS if category == "all" else [
        p for p in PROJECTS if p["category"] == category
    ]

    if not filtered:
        return Div(
            Div(
                Icon("search", style="font-size:2.5rem;color:#C9A84C;"),
                H5("No projects in this category yet", cls="mt-3 fw-bold"),
                P("Check back soon or view all projects.", cls="text-muted"),
                cls="text-center py-5",
            ),
            id="works-grid",
        )

    return Div(
        Row(
            *[Col(_project_card(p), span=12, md=6, lg=4) for p in filtered],
            cls="g-4",
        ),
        id="works-grid",
    )


def _filter_tabs(active_category: str = "all") -> Div:
    """Faststrap tabs wired for server-rendered HTMX filtering."""
    tabs = Tabs(
        *[
            (cat_id, cat_label, cat_id == active_category)
            for cat_id, cat_label in WORKS_CATEGORIES
        ],
        htmx=True,
        cls="border-0",
    )

    nav = tabs.children[0]
    for item, (cat_id, _cat_label) in zip(nav.children, WORKS_CATEGORIES):
        btn = item.children[0]
        btn.attrs["hx-get"] = f"/works/filter?category={cat_id}"
        btn.attrs["hx-target"] = "#works-filter-shell"
        btn.attrs["hx-swap"] = "outerHTML"
        btn.attrs["hx-push-url"] = "false"

    return Div(tabs, cls="portfolio-filter-tabs mb-4")


def _filter_shell(category: str = "all") -> Div:
    valid_categories = {cat_id for cat_id, _ in WORKS_CATEGORIES}
    active_category = category if category in valid_categories else "all"
    return Div(
        _filter_tabs(active_category),
        _project_grid(active_category),
        id="works-filter-shell",
    )


def setup_works_routes(app) -> None:
    @app.get("/works")
    def works_listing():
        return (
            Title("Works - Segun Banji Portfolio"),
            portfolio_navbar("/works"),
            page_banner(
                "Works",
                "A selection of analytics, BI, and education projects.",
                breadcrumbs=[("Home", "/"), ("Works", None)],
            ),
            Section(
                Container(
                    Span("Portfolio", cls="portfolio-eyebrow d-block mb-2 mt-2"),
                    H2("All Projects", cls="portfolio-section-heading mb-4"),
                    _filter_shell("all"),
                ),
                cls="section-white py-5 px-2 px-md-0",
            ),
            portfolio_footer(),
        )

    @app.get("/works/filter")
    def works_filter(request: Request):
        category = request.query_params.get("category", "all")
        return _filter_shell(category)

    @app.get("/works/{slug}")
    def works_detail(slug: str):
        proj = next((p for p in PROJECTS if p["slug"] == slug), None)
        if not proj:
            return (
                Title("Project Not Found"),
                portfolio_navbar("/works"),
                page_banner(
                    "Not Found",
                    "",
                    breadcrumbs=[("Home", "/"), ("Works", "/works"), ("Not Found", None)],
                ),
                Section(
                    Container(
                        Div(
                            H2("Project not found", cls="text-dark fw-bold"),
                            P("That project doesn't exist or has been moved.", cls="text-muted"),
                            A("<- Back to Works", href="/works", cls="text-warning fw-bold"),
                            cls="py-5",
                        ),
                    ),
                    cls="section-white",
                ),
                portfolio_footer(),
            )

        link_btns = []
        for link_type, url in proj.get("links", {}).items():
            icons = {"github": "github", "demo": "box-arrow-up-right", "dataset": "database"}
            labels = {"github": "View on GitHub", "demo": "Live Demo", "dataset": "Dataset"}
            link_btns.append(
                A(
                    Icon(icons.get(link_type, "link")),
                    f" {labels.get(link_type, link_type.title())}",
                    href=url,
                    target="_blank",
                    cls="btn btn-outline-warning btn-sm me-2 mb-2",
                )
            )

        tool_pills = Div(
            *[
                Badge(t, variant="light", cls="portfolio-skill-pill me-1 mb-1")
                for t in proj["tools"]
            ],
            cls="d-flex flex-wrap mb-3",
        )

        sidebar = Col(
            Card(
                Span("Tools Used", cls="portfolio-eyebrow d-block mb-2"),
                tool_pills,
                Span("Category", cls="portfolio-eyebrow d-block mb-1 mt-3"),
                P(proj["category"].replace("-", " ").title(), cls="text-muted small"),
                *(
                    [Div(Span("Links", cls="portfolio-eyebrow d-block mb-2"), *link_btns)]
                    if link_btns
                    else []
                ),
                title="Project Details",
                cls="portfolio-detail-card",
            ),
            span=12,
            lg=4,
        )

        main_col = Col(
            A("<- Back to Works", href="/works", cls="text-warning fw-bold d-block mb-3"),
            H1(proj["title"], cls="fw-bold mb-2"),
            P(proj.get("detail", proj["description"]), cls="text-muted"),
            span=12,
            lg=8,
        )

        return (
            Title(f"{proj['title']} - Segun Banji"),
            portfolio_navbar("/works"),
            page_banner(
                proj["title"],
                proj["category"].replace("-", " ").title(),
                breadcrumbs=[("Home", "/"), ("Works", "/works"), (proj["title"], None)],
            ),
            Div(
                Img(
                    src=proj["image"],
                    alt=proj["title"],
                    cls="w-100 portfolio-project-detail-hero",
                    loading="eager",
                ),
                cls="w-100 overflow-hidden bg-black",
            ),
            Section(
                Container(Row(main_col, sidebar, cls="g-4 mt-3 align-items-start")),
                cls="section-white py-4",
            ),
            portfolio_footer(),
        )
