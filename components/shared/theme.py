"""
components/shared/theme.py — Brand tokens and Faststrap component defaults.
"""
from faststrap import create_theme, set_component_defaults

# ---------------------------------------------------------------------------
# Brand colour constants (import these into CSS helpers and route modules)
# ---------------------------------------------------------------------------
GOLD = "#C9A84C"
BLACK = "#111111"
OFF_WHITE = "#F5F0E8"
WHITE = "#FFFFFF"
MUTED_DARK = "rgba(255,255,255,0.65)"
MUTED_LIGHT = "#6B6B6B"
BORDER_SUBTLE = "rgba(201,168,76,0.25)"
BORDER_EMPHASIS = "rgba(201,168,76,0.6)"

# ---------------------------------------------------------------------------
# Faststrap theme (Bootstrap CSS variable overrides)
# ---------------------------------------------------------------------------
THEME = create_theme(
    primary=GOLD,
    dark=BLACK,
    light=OFF_WHITE,
)

# ---------------------------------------------------------------------------
# Global component defaults
# ---------------------------------------------------------------------------
def apply_component_defaults() -> None:
    """Call once at app start to set Faststrap-wide component defaults."""
    set_component_defaults(
        "Navbar",
        variant="dark",
        expand="lg",
        sticky="top",
        container=True,
    )
    set_component_defaults(
        "Badge",
        variant="warning",
    )
    set_component_defaults(
        "Button",
        variant="warning",
    )
    set_component_defaults(
        "FooterModern",
        bg_variant="dark",
        text_variant="light",
    )
