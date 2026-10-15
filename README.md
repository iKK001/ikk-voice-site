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

## Custom domain

The site is served as `https://voice.ideenkaffee.ch/` (file `CNAME`).

1. At Hoststar add a DNS `CNAME` record: `voice` → `ikk001.github.io`.
2. Repo → Settings → Pages → Custom domain: `voice.ideenkaffee.ch`, then tick *Enforce HTTPS*
   once the certificate is issued (a few minutes after DNS resolves).
