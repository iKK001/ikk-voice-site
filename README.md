# iKK Voice – Website

Static site for the iKK Voice app, hosted on GitHub Pages. No build step, no
external fonts, scripts or trackers.

| Page | App Store Connect field |
|---|---|
| `index.html` | Marketing URL |
| `support.html` | Support URL (includes Impressum) |
| `datenschutz.html` | Privacy Policy URL |

## Publish

1. Push this folder to a **public** GitHub repo (Pages on private repos needs a paid plan).
2. Repo → Settings → Pages → Source: *Deploy from a branch*, Branch: `main` / `(root)`.
3. The site appears at `https://<user>.github.io/<repo>/` after a minute.

## Custom domain (optional)

1. At your DNS provider add a `CNAME` record, e.g. `ikkvoice` → `<user>.github.io`.
2. Repo → Settings → Pages → Custom domain: `ikkvoice.ideenkaffee.ch`, then tick *Enforce HTTPS*.
