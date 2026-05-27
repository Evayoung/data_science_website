"""
main.py - Segun Banji Data Science Portfolio entrypoint.
"""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).with_name(".env"))

from fasthtml.common import FastHTML, Link, Script, serve
from faststrap import add_bootstrap, mount_assets

from components.shared.theme import THEME, apply_component_defaults


# Project CSS and the small stats counter script are served from mounted assets.
custom_hdrs = (
    Link(rel="stylesheet", href="/assets/css/style.css"),
    Script(src="/assets/js/main.js", defer=True),
)

app = FastHTML(
    hdrs=custom_hdrs,
    secret_key=os.getenv("FASTHTML_SECRET_KEY", "banjisegun-portfolio-static-site"),
)

add_bootstrap(
    app,
    font_family="Inter",
    theme=THEME,
    mode="dark",
)

# Mount project files away from Faststrap's own /static namespace.
mount_assets(app, "static", url_path="/assets")

apply_component_defaults()

from routes.home import setup_home_routes
from routes.about import setup_about_routes
from routes.works import setup_works_routes
from routes.cv import setup_cv_routes
from routes.videos import setup_videos_routes
from routes.contact import setup_contact_routes

setup_home_routes(app)
setup_about_routes(app)
setup_works_routes(app)
setup_cv_routes(app)
setup_videos_routes(app)
setup_contact_routes(app)

if __name__ == "__main__":
    serve()
