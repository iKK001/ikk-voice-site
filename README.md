# iKK Voice – Website

Static site for the iKK Voice app, hosted on GitHub Pages. No build step, no
external fonts, scripts or trackers.

| Page | App Store Connect field |
|---|---|
| `index.html` | Marketing URL |
| `support.html` | Support URL (includes Impressum) |
| `datenschutz.html` | Privacy Policy URL |

## Languages

German is the primary language at the site root. Every other app language
has its own folder with the same three pages, named `index.html`,
`support.html` and `privacy.html`:

`en/` English · `fr/` Français · `it/` Italiano · `es/` Español ·
`hr/` Hrvatski · `sr/` Srpski (Latin) · `tr/` Türkçe · `pt/` Português ·
`nl/` Nederlands

App Store Connect gets the matching language per locale (set in
`store_assets/store_texts.py` of the app repo); Google Play has one privacy
URL per app, use `en/privacy.html`.

The language dropdown in the header and the `hreflang` links in `<head>` are
generated: after editing or adding a page run

```sh
python3 tools/lang_nav.py
```

It replaces the `<details class="lang-switch">` block (or the
`<!-- lang-nav -->` marker in a fresh page) and the `hreflang` lines, so it
can be run any number of times. The dropdown is a plain `<details>` element,
no JavaScript.

## Publish

1. Push this folder to a **public** GitHub repo (Pages on private repos needs a paid plan).
2. Repo → Settings → Pages → Source: *Deploy from a branch*, Branch: `main` / `(root)`.
3. The site appears at `https://<user>.github.io/<repo>/` after a minute.

## Custom domain

The site is served as `https://voice.ideenkaffee.ch/` (file `CNAME`).

1. At Hoststar add a DNS `CNAME` record: `voice` → `ikk001.github.io`.
2. Repo → Settings → Pages → Custom domain: `voice.ideenkaffee.ch`, then tick *Enforce HTTPS*
   once the certificate is issued (a few minutes after DNS resolves).
