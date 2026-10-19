# Creepy Cute — public development journal

Canonical repository: `vdecommerce/creepy-cute-devlog`.
This is the public GitHub Pages companion to the private Roblox source project
`vdecommerce/roblox-cupy-obby`. The game remains a private test; publishing this
website does not authorize a public game release or pass sales.

Use Node.js 22+ without package dependencies. `npm run build` writes `dist/`;
`npm run check` verifies local links, media, metadata, feed and sitemap;
`npm run dev` serves the generated site at `/creepy-cute-devlog/`.
GitHub Pages serves the gh-pages branch. `npm run publish` builds/checks a clean,
reviewed main and commits only the generated site to that artifact branch. Keep
dist untracked on source branches. The current OAuth connection cannot add
Actions workflow files; do not expand its credentials just to deploy this site.
Work on a machine-named topic branch and review changes through a PR.

Keep Dutch updates in `content/posts.json`, site status in `content/site.json`
and selected media with their provenance in `content/media.json`. Publish
meaningful verified milestones. Explicitly distinguish concept illustrations,
Blender renders, native Studio inspection and user-reported playtesting.
Do not present a model inspection camera as ordinary player gameplay, simulated
mobile layouts as physical-phone proof, or an unpublished build as a release.
Retain historical articles with their original milestone status.

Never publish source game models/builds, private reference photographs,
credentials, account/tester details, internal machine paths or raw work logs.
Only copy selected optimized media to `public/assets/media/`; there is no
open-source or artwork reuse licence. No tracking, comments, accounts or forms
are requested. Future automatic updates require an explicit scheduling request.
