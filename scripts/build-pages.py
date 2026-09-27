#!/usr/bin/env python3
"""Package the committed static website for a GitHub Pages project path.

No historical authoring inputs or third-party Python dependencies are needed.
The original solar.org export is never modified.
"""
import argparse
import html
from html.parser import HTMLParser
from pathlib import Path
import re
import shutil
from urllib.parse import unquote, urljoin, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "solar-site"
ATTRIBUTE = re.compile(r'''(\b(?:href|src|action|poster|data-img)\s*=\s*)(["'])(.*?)\2''', re.I | re.S)


def package(base_path, output):
    base = base_path.rstrip("/")
    if base and not re.fullmatch(r"(?:/[A-Za-z0-9_-]+)+", base):
        raise ValueError("Base path must be empty, /, or a path such as /solar-foundation-website")
    output = output.resolve()
    if output.exists():
        raise ValueError(f"Output already exists: {output}. Choose a fresh directory.")

    pages = sorted(SOURCE.rglob("*.html"))
    routes = {}
    for page in pages:
        relative = page.relative_to(SOURCE).as_posix()
        destination = "/" if relative == "index.html" else "/" + relative.removesuffix(".html") + "/"
        routes["/" + relative] = destination
        routes[destination.rstrip("/") or "/"] = destination
        routes[destination] = destination
    # Copied article bodies contain blog-root links. Prefer a local snapshot
    # where one exists, otherwise retain the original blog destination.
    for page in (SOURCE / "archive").glob("*.html"):
        routes["/" + page.stem] = "/archive/" + page.stem + "/"
        routes["/" + page.stem + "/"] = "/archive/" + page.stem + "/"

    def rewrite(value, page):
        value = html.unescape(value)
        parts = urlsplit(value)
        if not value or value.startswith(("#", "?")) or parts.scheme or parts.netloc:
            return value
        resolved = urlsplit(urljoin("https://local.invalid/" + page, value))
        path = unquote(resolved.path)
        if path in routes:
            target = base + routes[path]
        elif (SOURCE / path.lstrip("/")).is_file():
            target = base + resolved.path
        elif page.startswith("archive/") and value.startswith("/"):
            return urlunsplit(("https", "blog.solar.org", resolved.path, resolved.query, resolved.fragment))
        else:
            raise ValueError(f"Unresolved local link in {page}: {value}")
        return urlunsplit(("", "", target, resolved.query, resolved.fragment))

    class RewriteHTML(HTMLParser):
        def __init__(self, page):
            super().__init__(convert_charrefs=False)
            self.page, self.parts = page, []

        def handle_starttag(self, tag, attrs):
            text = self.get_starttag_text()
            text = ATTRIBUTE.sub(lambda m: m[1] + m[2] + html.escape(rewrite(m[3], self.page), quote=True) + m[2], text)
            self.parts.append(text)

        handle_startendtag = handle_starttag

        def handle_endtag(self, tag):
            self.parts.append(f"</{tag}>")

        def handle_data(self, data):
            self.parts.append(data)

        def handle_entityref(self, name):
            self.parts.append(f"&{name};")

        def handle_charref(self, name):
            self.parts.append(f"&#{name};")

        def handle_comment(self, data):
            self.parts.append(f"<!--{data}-->")

        def handle_decl(self, decl):
            self.parts.append(f"<!{decl}>")

    output.mkdir(parents=True)
    copied = 0
    for source in sorted(SOURCE.rglob("*")):
        if not source.is_file() or source.suffix in (".html", ".md") or source.name == "CNAME":
            continue
        target = output / source.relative_to(SOURCE)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        copied += 1

    for page in pages:
        relative = page.relative_to(SOURCE).as_posix()
        parser = RewriteHTML(relative)
        parser.feed(page.read_text())
        parser.close()
        destination = routes["/" + relative].strip("/")
        target = output / destination / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("".join(parser.parts))

    (output / ".nojekyll").touch()
    (output / "404.html").write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex"><title>Page not found — Solar Foundation</title>
<style>body{{margin:0;background:#0e0d12;color:#f4f3f6;font:18px/1.6 system-ui,sans-serif;display:grid;min-height:100vh;place-items:center}}main{{padding:32px;max-width:620px}}a{{color:#ffc24a}}h1{{font-size:40px;line-height:1.2}}</style>
</head><body><main><p>Solar Foundation</p><h1>Page not found</h1><p>The page may have moved, or the address may be incomplete.</p><a href="{base}/">Return to the website →</a></main></body></html>''')
    print(f"Packaged {len(pages)} pages and {copied} assets for {base or '/'} in {output}")
    verify(output, base)


def verify(output, base):
    """Every local link must stay inside the Pages project and resolve on disk."""
    checked = 0

    class CheckHTML(HTMLParser):
        def handle_starttag(self, tag, attrs):
            nonlocal checked
            for name, value in attrs:
                if name not in ("href", "src", "poster", "action", "data-img") or not value or value.startswith(("#", "?")):
                    continue
                url = urlsplit(value)
                if url.scheme or url.netloc:
                    continue
                if not url.path.startswith(base + "/"):
                    raise ValueError(f"Link escapes the Pages project: {value}")
                target = output / unquote(url.path[len(base):]).lstrip("/")
                if target.is_dir():
                    target /= "index.html"
                if not target.is_file():
                    raise ValueError(f"Missing packaged target: {value}")
                checked += 1

    for page in output.rglob("*.html"):
        parser = CheckHTML()
        parser.feed(page.read_text())
        parser.close()
    print(f"Verified {checked} local navigation, download and asset references.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-path", default="/solar-foundation-website")
    parser.add_argument("--output", type=Path, default=ROOT / "_site")
    args = parser.parse_args()
    package(args.base_path, args.output)
