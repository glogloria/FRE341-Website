
import os
import shutil
from pathlib import Path

import django

# Use the same settings module as manage.py.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.conf import settings
from django.test import Client, override_settings

BASE_DIR = Path(settings.BASE_DIR)
OUTPUT_DIR = BASE_DIR / "docs"
STATIC_DIR = BASE_DIR / "static"

# Django URL -> exported HTML filename
PAGES = {
    "/": "index.html",
    "/about/": "about.html",
    "/products/": "products.html",
    "/gallery/": "gallery.html",
    "/video/": "video.html",
}

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Copy static assets into docs/static.
destination_static = OUTPUT_DIR / "static"

if destination_static.exists():
    shutil.rmtree(destination_static)

if STATIC_DIR.exists():
    shutil.copytree(STATIC_DIR, destination_static)
    print("Copied static assets.")
else:
    print(f"Warning: Static directory not found: {STATIC_DIR}")

client = Client()

# Allow Django's test client hostname without changing settings.py.
with override_settings(
    ALLOWED_HOSTS=["testserver", "localhost", "127.0.0.1"]
):
    for route, filename in PAGES.items():
        response = client.get(route)

        if response.status_code != 200:
            print(
                f"Failed: {route} "
                f"returned HTTP {response.status_code}"
            )
            continue

        html = response.content.decode("utf-8")

        # Rewrite common Django navigation URLs.
        for django_url, target_filename in PAGES.items():
            if django_url == "/":
                replacement = "index.html"
            else:
                replacement = target_filename

            html = html.replace(
                f'href="{django_url}"',
                f'href="{replacement}"'
            )
            html = html.replace(
                f"href='{django_url}'",
                f"href='{replacement}'"
            )

        # Rewrite root-relative static asset paths.
        html = html.replace(
            'href="/static/',
            'href="static/'
        )
        html = html.replace(
            "href='/static/",
            "href='static/"
        )
        html = html.replace(
            'src="/static/',
            'src="static/'
        )
        html = html.replace(
            "src='/static/",
            "src='static/"
        )

        # Save the rendered page.
        output_file = OUTPUT_DIR / filename
        output_file.write_text(html, encoding="utf-8")

        print(f"Exported {route} -> docs/{filename}")

print("\nExport finished.")
print(f"Output directory: {OUTPUT_DIR}")
