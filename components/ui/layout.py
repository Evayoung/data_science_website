"""
components/ui/layout.py — Shared layout helpers (page_banner, page shell, etc.)
"""
from typing import Any

from fasthtml.common import Div, H1, P, Span
from faststrap import Breadcrumb, Container


def page_banner(
    title: str,
    subtitle: str = "",
    breadcrumbs: list[tuple[str, str | None]] | None = None,
    extra: Any | None = None,
) -> Div:
    """
    Dark page banner for inner pages.

    Args:
        title: Page H1 heading
        subtitle: Optional muted subtitle
        breadcrumbs: list of (label, href) tuples. Last item href should be None.
    """
    # Breadcrumb items are (label, href) tuples — last item href is None → active
    crumb_tuples: list[tuple] = []
    if breadcrumbs:
        last_idx = len(breadcrumbs) - 1
        for i, (label, href) in enumerate(breadcrumbs):
            if i == last_idx or href is None:
                crumb_tuples.append((label, None, True))
            else:
                crumb_tuples.append((label, href, False))

    parts: list[Any] = [H1(title, cls="mb-2")]
    if subtitle:
        parts.append(P(subtitle, cls="text-muted-dark mb-3"))
    if extra:
        parts.append(Div(extra, cls="mb-3"))
    if crumb_tuples:
        parts.append(Breadcrumb(*crumb_tuples, cls="mb-0"))

    return Div(
        Container(*parts),
        cls="portfolio-page-banner",
    )


def page_shell(
    *content: Any,
    navbar: Any,
    footer: Any,
    title: str = "Portfolio",
) -> tuple[Any, ...]:
    """
    Return the full page component tuple: navbar, *content, footer.
    FastHTML Title is handled per-route via Title().
    """
    return (navbar, *content, footer)
