# Preview and release review

## Reproducible local verification

Use Node >=22.23.4 (Node 24 is supported here), Python 3 and the locked dependencies:

```sh
npm ci
npm run verify
npm run preview
```

`verify` runs Astro diagnostics, unit/preservation tests, root and `/research-preview/` builds, and all built-output checks. It restores a root build after testing the project path, including after a failed preview check. This command does not run a browser, decode media, check outbound HTTP availability or deploy.

`docs/route-coverage.json` accounts for all 84 audited archive pages: 70 canonical aliases, nine excluded stock examples and the five old-entry posts explicitly excluded by the user. `npm run check:routes` validates both directory URLs and their exact-case `index.html` files, refresh/fallback destinations and canonical fragments. Run `npm run audit:routes` after changing a canonical mapping or alias.

## Prepared preview artifact workflow

`.github/workflows/preview.yml` is a manual `workflow_dispatch` job. It installs the lockfile with Node 24, runs the complete local verification command, then uploads the restored root build as a seven-day `research-homepage-preview` artifact. Download and extract the artifact and serve its directory with `python3 -m http.server 4321`; review at `http://localhost:4321/`.

The workflow is prepared locally and has not run on GitHub. It has only `contents: read` permission, has no push/PR/schedule trigger, and does not deploy or modify Pages settings. The artifact is a downloadable build, not a hosted preview URL. Hosting and production cutover remain separate approval steps.

References checked on 5 November 2026: [Astro GitHub Pages configuration](https://docs.astro.build/en/guides/deploy/github/), [checkout](https://github.com/actions/checkout), [setup-node](https://github.com/actions/setup-node), [upload-artifact](https://github.com/actions/upload-artifact). The prepared workflow uses the v7 major versions shown in the official action documentation. It omits the deployment job from Astro's guide.

## Browser acceptance still required

No browser acceptance is claimed. The current executor rejects a local socket bind with `Operation not permitted`, so it cannot serve the build for browser review here.

- Review Home, Research/projects, Tools/detail pages, Publications, Posts, Talks, News and About at 320px, 768px and desktop widths in both themes. Pay particular attention to the longer name, seven-link header, long project titles and chronological lists.
- Walk the site with Tab/Shift+Tab and Enter/Space. Check skip link, focus visibility/order, menu toggle and Escape focus return, current-page labels, theme toggle, details controls and native video controls. Repeat navigation without JavaScript.
- Check Temporal Logic's timeline and the steady-state notes' matrices/aligned equations at 320px, including horizontal scrolling and screen-reader treatment of native MathML. Scientific qualifications remain a separate content review in `content-review.md`.
- Inspect Network before and after activating the security player: no YouTube request before the button is used. Check the direct watch fallback, all local video starts/seeking, posters, download links and absent autoplay. Captions/transcripts are unavailable and have not been invented.
- Review images, reduced-motion behaviour, light/dark contrast and viewport overflow. Record browser/version, viewport, findings and screenshots when available.
- Verify outbound scholarly, project, historical workshop and software URLs separately. A failed fetch alone does not establish that a resource is broken.

The original external York hostname cannot be redirected by this static site. All alias validation concerns the new host.

## Resource dispositions

The October 2022 industry-exhibition poster and January 2023 revision remain separate downloads on the RoboChart/PRISM page. The exhibition talk links its October edition. The animation poster links from its related demonstration. The SoSyM award announcement links the preserved award PDF.

The older CV at `public/old_entry/uploads/CV-KangfengYe.pdf` is retained for preservation, without promoting it as a current CV. About links the current CV. Some original image masters are also retained separately from their lighter display derivatives; they are accounted for by the preservation manifest rather than loaded eagerly by pages.
