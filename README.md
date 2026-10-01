# Perch website

Public website, setup guidance and policies for [Perch](https://github.com/awtechs/perch), maintained by AWTechs.

## Hosting

The `dist/` directory contains the complete site as plain HTML, CSS and PNG assets. It can be served by any static host. There are no runtime dependencies, accounts, analytics or command relays.

Serve locally with `python3 -m http.server 8080 --directory dist`. Edit the committed files in `dist/` directly.

## Vercel

Import `awtechs/perch-website` into Vercel. The committed `vercel.json` selects static hosting and `dist/` as the output directory. Use `main` as the production branch. Vercel's GitHub integration deploys pushes automatically and creates previews for pull requests. No deployment token needs to be stored in this repository.

Add `perch.awtechs.com` to the project and apply the DNS records Vercel actually provides. Keep the existing site online until the Vercel deployment and domain are verified.

The GitHub Actions workflow verifies local links before changes merge. Production deployment requires the repository to be imported into Vercel; adding this configuration alone does not establish that connection.

## Policies

Support, privacy and terms are published in `dist/support/`, `dist/privacy/` and `dist/terms/`. Review policies when data handling or hosting changes.
