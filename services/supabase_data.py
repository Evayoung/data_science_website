"""
Load portfolio content from Supabase through the PostgREST API.

The app keeps data.py as a local fallback. This module returns a dictionary with
the same constant names used by the routes when Supabase credentials are present.
"""
from __future__ import annotations

import json
import os
from collections import defaultdict
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


PROFILE_ID = os.getenv("PORTFOLIO_PROFILE_ID", "segun-banji")
TIMEOUT_SECONDS = max(float(os.getenv("SUPABASE_TIMEOUT_SECONDS", "10")), 8.0)
DEFAULT_PROFILE_IMAGE = "https://pdfsfspkptysfowokzgi.supabase.co/storage/v1/object/public/portfolio-images/profile/1779887668-5779de3f-profile.jpeg"
DEFAULT_PROFILE_ALT_IMAGE = "https://pdfsfspkptysfowokzgi.supabase.co/storage/v1/object/public/portfolio-images/profile/1779887670-16a28c66-profile2.jpeg"
DEFAULT_HERO_BACKGROUND_IMAGE = "https://pdfsfspkptysfowokzgi.supabase.co/storage/v1/object/public/portfolio-images/projects/1779887686-ed01e289-mcmoren-dashboard.jpg"


def _env_config() -> tuple[str, str] | None:
    url = os.getenv("SUPABASE_URL", "").rstrip("/")
    key = os.getenv("SUPABASE_ANON_KEY", "")
    if not url or not key:
        return None
    return url, key


def _request_rows(url: str, key: str, table: str, params: dict[str, str] | None = None) -> list[dict]:
    query = urlencode(params or {}, safe="(),.*")
    endpoint = f"{url}/rest/v1/{table}"
    if query:
        endpoint = f"{endpoint}?{query}"

    req = Request(
        endpoint,
        headers={
            "apikey": key,
            "Authorization": f"Bearer {key}",
            "Accept": "application/json",
        },
    )
    with urlopen(req, timeout=TIMEOUT_SECONDS) as response:
        return json.loads(response.read().decode("utf-8"))


def _insert_row(table: str, payload: dict) -> bool:
    config = _env_config()
    if not config:
        return False

    url, key = config
    endpoint = f"{url}/rest/v1/{table}"
    req = Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "apikey": key,
            "Authorization": f"Bearer {key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Prefer": "return=minimal",
        },
        method="POST",
    )
    try:
        with urlopen(req, timeout=TIMEOUT_SECONDS) as response:
            return 200 <= response.status < 300
    except (HTTPError, URLError, TimeoutError, OSError):
        return False


def _rows(table: str, params: dict[str, str] | None = None) -> list[dict]:
    config = _env_config()
    if not config:
        return []
    return _request_rows(*config, table, params)


def _first(table: str, params: dict[str, str] | None = None) -> dict | None:
    rows = _rows(table, params)
    return rows[0] if rows else None


def _cert_label(cert: dict) -> str:
    label = cert["title"]
    if cert.get("issuer"):
        label = f"{label}, {cert['issuer']}"
    if cert.get("date_label"):
        label = f"{label} ({cert['date_label']})"
    return label


def _group_by(rows: list[dict], key: str) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        grouped[row[key]].append(row)
    return grouped


def load_portfolio_data() -> dict | None:
    """Return route-compatible portfolio data from Supabase, or None on fallback."""
    if not _env_config():
        return None

    try:
        profile = _first(
            "portfolio_profiles",
            {"id": f"eq.{PROFILE_ID}", "select": "*", "limit": "1"},
        )
        if not profile:
            return None

        bio_rows = _rows(
            "portfolio_bio_paragraphs",
            {"profile_id": f"eq.{PROFILE_ID}", "select": "*", "order": "sort_order.asc"},
        )
        stats_rows = _rows(
            "portfolio_stats",
            {"profile_id": f"eq.{PROFILE_ID}", "select": "*", "order": "sort_order.asc"},
        )
        skills_rows = _rows(
            "portfolio_skills",
            {"profile_id": f"eq.{PROFILE_ID}", "select": "*", "order": "sort_order.asc"},
        )
        social_rows = _rows(
            "portfolio_social_links",
            {"profile_id": f"eq.{PROFILE_ID}", "select": "*", "order": "sort_order.asc"},
        )
        specialisation_rows = _rows(
            "portfolio_specialisations",
            {"profile_id": f"eq.{PROFILE_ID}", "select": "*", "order": "sort_order.asc"},
        )
        experience_rows = _rows(
            "portfolio_experience",
            {"profile_id": f"eq.{PROFILE_ID}", "select": "*", "order": "sort_order.asc"},
        )
        highlight_rows = _rows(
            "portfolio_experience_highlights",
            {"select": "*", "order": "sort_order.asc"},
        )
        education_rows = _rows(
            "portfolio_education",
            {"profile_id": f"eq.{PROFILE_ID}", "select": "*", "order": "sort_order.asc"},
        )
        certification_rows = _rows(
            "portfolio_certifications",
            {"profile_id": f"eq.{PROFILE_ID}", "select": "*", "order": "sort_order.asc"},
        )
        language_rows = _rows(
            "portfolio_languages",
            {"profile_id": f"eq.{PROFILE_ID}", "select": "*", "order": "sort_order.asc"},
        )
        soft_skill_rows = _rows(
            "portfolio_soft_skills",
            {"profile_id": f"eq.{PROFILE_ID}", "select": "*", "order": "sort_order.asc"},
        )
        work_category_rows = _rows(
            "work_categories",
            {"select": "*", "order": "sort_order.asc"},
        )
        project_rows = _rows(
            "portfolio_projects",
            {"profile_id": f"eq.{PROFILE_ID}", "select": "*", "order": "sort_order.asc"},
        )
        project_tool_rows = _rows(
            "portfolio_project_tools",
            {"select": "*", "order": "sort_order.asc"},
        )
        project_link_rows = _rows(
            "portfolio_project_links",
            {"select": "*", "order": "sort_order.asc"},
        )
        video_category_rows = _rows(
            "video_categories",
            {"select": "*", "order": "sort_order.asc"},
        )
        video_rows = _rows(
            "portfolio_videos",
            {"profile_id": f"eq.{PROFILE_ID}", "select": "*", "order": "sort_order.asc"},
        )
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError, OSError):
        return None

    highlights_by_experience = _group_by(highlight_rows, "experience_id")
    tools_by_project = _group_by(project_tool_rows, "project_slug")
    links_by_project = _group_by(project_link_rows, "project_slug")

    owner = {
        "name": profile["name"],
        "initials": profile["initials"],
        "title": profile["title"],
        "tagline": profile["tagline"],
        "phone": profile.get("phone") or "",
        "email": profile["email"],
        "linkedin": profile.get("linkedin_url") or "#",
        "github": profile.get("github_url") or "#",
        "location": profile.get("location") or "",
        "summary": profile.get("summary") or "",
        "bio": [row["body"] for row in bio_rows],
        "how_i_work": profile.get("how_i_work") or "",
        "youtube_channel": profile.get("youtube_channel_url") or "#",
        "availability": profile.get("availability") or "Available",
        "profile_image": profile.get("profile_image_url") or DEFAULT_PROFILE_IMAGE,
        "profile_alt_image": profile.get("profile_alt_image_url") or DEFAULT_PROFILE_ALT_IMAGE,
        "hero_background_image": profile.get("hero_background_image_url") or DEFAULT_HERO_BACKGROUND_IMAGE,
    }

    tools: dict[str, list[str]] = defaultdict(list)
    for skill in skills_rows:
        group = skill.get("group_name")
        if group and skill["name"] not in tools[group]:
            tools[group].append(skill["name"])

    projects = []
    for project in project_rows:
        slug = project["slug"]
        projects.append(
            {
                "slug": slug,
                "title": project["title"],
                "year": project.get("project_year"),
                "category": project["category_id"],
                "description": project["description"],
                "detail": project["detail"],
                "tools": [row["name"] for row in tools_by_project.get(slug, [])],
                "image": project.get("image_path"),
                "featured": project.get("featured", False),
                "links": {
                    row["label"].lower(): row["url"]
                    for row in links_by_project.get(slug, [])
                },
            }
        )

    return {
        "DATA_SOURCE": "supabase",
        "OWNER": owner,
        "STATS": [
            {"value": row["value"], "suffix": row["suffix"], "label": row["label"]}
            for row in stats_rows
        ],
        "SKILLS_FLAT": [row["name"] for row in skills_rows if row.get("show_on_home")],
        "TOOLS": dict(tools),
        "CV_SKILLS": [
            {"name": row["name"], "level": row["proficiency"]}
            for row in skills_rows
            if row.get("show_on_cv") and row.get("proficiency") is not None
        ],
        "EXPERIENCE": [
            {
                "role": row["role"],
                "org": row["organization"],
                "location": row.get("location"),
                "dates": row["date_label"],
                "description": row["description"],
                "highlights": [
                    highlight["body"] for highlight in highlights_by_experience.get(row["id"], [])
                ],
            }
            for row in experience_rows
        ],
        "EDUCATION": [
            {
                "degree": row["degree"],
                "institution": row["institution"],
                "location": row.get("location"),
                "year": row["year"],
                "gpa": row.get("gpa"),
                "honors": row.get("honors"),
            }
            for row in education_rows
        ],
        "CERTIFICATIONS": [_cert_label(row) for row in certification_rows],
        "LANGUAGES": [row["label"] for row in language_rows],
        "SOFT_SKILLS": [row["label"] for row in soft_skill_rows],
        "SPECIALISATIONS": [
            {
                "icon": row["icon"],
                "title": row["title"],
                "description": row["description"],
            }
            for row in specialisation_rows
        ],
        "PROJECTS": projects,
        "WORKS_CATEGORIES": [(row["id"], row["label"]) for row in work_category_rows],
        "VIDEOS": [
            {
                "video_id": row["video_id"],
                "title": row["title"],
                "description": row["description"],
                "category": row["category_id"],
            }
            for row in video_rows
        ],
        "VIDEO_CATEGORIES": [(row["id"], row["label"]) for row in video_category_rows],
        "SOCIAL_LINKS": [
            {
                "icon": row["icon"],
                "href": row["href"],
                "label": row["label"],
            }
            for row in social_rows
        ],
    }


def save_contact_message(values: dict[str, str]) -> bool:
    """Persist a validated contact form submission to Supabase when configured."""
    return _insert_row(
        "contact_messages",
        {
            "name": values["name"],
            "email": values["email"],
            "subject": values["subject"],
            "message": values["message"],
            "source": "portfolio",
        },
    )
