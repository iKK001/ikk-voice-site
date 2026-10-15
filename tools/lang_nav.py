#!/usr/bin/env python3
"""Injects the language dropdown and hreflang links into every page.

    python3 tools/lang_nav.py        # run after editing or adding pages

German lives at the site root (index.html, support.html, datenschutz.html);
every other language in <code>/ (index.html, support.html, privacy.html).
The dropdown is a <details> element: no JavaScript, keyboard accessible.
Re-running replaces the previously injected blocks, so it is idempotent.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://voice.ideenkaffee.ch/"

# folder -> (hreflang, native name, aria label for the menu, page names)
LANGS = {
    "": ("de", "Deutsch", "Sprache wählen"),
    "en": ("en", "English", "Choose language"),
    "fr": ("fr", "Français", "Choisir la langue"),
    "it": ("it", "Italiano", "Scegli la lingua"),
    "es": ("es", "Español", "Elegir idioma"),
    "hr": ("hr", "Hrvatski", "Odaberi jezik"),
    "sr": ("sr-Latn", "Srpski", "Izaberi jezik"),
    "tr": ("tr", "Türkçe", "Dil seçin"),
    "pt": ("pt-PT", "Português", "Escolher idioma"),
    "nl": ("nl", "Nederlands", "Taal kiezen"),
}
PAGES = {"index.html": "index.html", "support.html": "support.html", "datenschutz.html": "privacy.html"}


def file_in(folder, page):
    """File path of `page` (German file name) in `folder`, relative to the site root."""
    name = page if folder == "" else PAGES[page]
    return f"{folder}/{name}" if folder else name


def page_in(folder, page):
    """URL path of the same page; index.html is addressed as the folder ("" or "en/")."""
    if page == "index.html":
        return f"{folder}/" if folder else ""
    return file_in(folder, page)


def rel(from_folder, target):
    return ("../" if from_folder else "./") + target


def dropdown(folder, page):
    _, current, label = LANGS[folder]
    items = []
    for f, (code, name, _) in LANGS.items():
        href = rel(folder, page_in(f, page))
        cur = ' aria-current="true"' if f == folder else ""
        items.append(f'          <li><a href="{href}" lang="{code}" hreflang="{code}"{cur}>{name}</a></li>')
    return "\n".join([
        f'      <details class="lang-switch">',
        f'        <summary aria-label="{label}"><span aria-hidden="true">🌐</span> {current}</summary>',
        f'        <ul>',
        *items,
        f'        </ul>',
        f'      </details>',
    ])


def hreflangs(page):
    lines = []
    for f, (code, _, _) in LANGS.items():
        lines.append(f'  <link rel="alternate" hreflang="{code}" href="{SITE}{page_in(f, page)}">')
    lines.append(f'  <link rel="alternate" hreflang="x-default" href="{SITE}{page_in("", page)}">')
    return "\n".join(lines)


NAV_RE = re.compile(r'      <!-- lang-nav -->|      <details class="lang-switch">.*?</details>', re.S)
HREF_RE = re.compile(r'^[ \t]*<link rel="alternate" hreflang="[^"]*" href="[^"]*">\n', re.M)


def process(folder, page):
    path = ROOT / file_in(folder, page)
    if not path.exists():
        print(f"  missing {path.relative_to(ROOT)}")
        return
    s = path.read_text(encoding="utf-8")
    s, n = NAV_RE.subn(lambda _: dropdown(folder, page), s, count=1)
    if n == 0:
        print(f"  no <!-- lang-nav --> marker in {path.relative_to(ROOT)}")
        return
    s = HREF_RE.sub("", s)
    s = s.replace('  <link rel="stylesheet"', hreflangs(page) + '\n  <link rel="stylesheet"', 1)
    path.write_text(s, encoding="utf-8")
    print(f"  {path.relative_to(ROOT)}")


def main():
    for folder in LANGS:
        for page in PAGES:
            process(folder, page)


if __name__ == "__main__":
    main()
