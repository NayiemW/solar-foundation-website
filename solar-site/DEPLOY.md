# Website deployments

**Repository:** [NayiemW/solar-foundation-website](https://github.com/NayiemW/solar-foundation-website)

**Pages URL:** [nayiemw.github.io/solar-foundation-website/](https://nayiemw.github.io/solar-foundation-website/)

**Railway URL:** [solar-foundation-website-production.up.railway.app](https://solar-foundation-website-production.up.railway.app)

**Canonical website:** [solar.org](https://solar.org)

## Deployment input

Deploy the committed content in `solar-site/`. It is a static website; GitHub Pages does not run `solar-site-server.js` or require a database.

The source HTML mixes root-relative clean routes with relative asset and document links. The Pages packaging step converts pages to directory index routes and adjusts local links for the repository's base path. Known archive references resolve to local snapshots; remaining blog references retain their source destination.

From the repository root, with Python 3 installed:

```sh
python3 scripts/build-pages.py --base-path /solar-foundation-website --output _site
```

The `_site/` directory is the Pages artifact. For example, `history.html` becomes the page served at `/solar-foundation-website/history/`. Images, JavaScript and downloads are also addressed under `/solar-foundation-website/`.

The historical Python regeneration pipeline is separate. It depends on original authoring files and is not part of the Pages deployment.

## Branches and publishing

- `prod` is the default and production branch.
- All development and content changes happen on `dev`.
- Merge a `dev` → `prod` pull request to publish.
- The production workflow packages the static files, uploads `_site/` and deploys through GitHub Pages.

GitHub Pages uses **GitHub Actions** as its publishing source. Changes on `dev` do not deploy.

## Canonical identity

This deployment is a mirror of the Solar website. Existing canonical links, social metadata and sitemap references to `https://solar.org` are preserved. Publishing this mirror does not require changing the `solar.org` domain.

## Railway

The existing Railway service follows `prod`. Railpack uses `package.json` to install Node 22 and runs `npm start`, as declared in `railway.json`. The server binds to `0.0.0.0` and the injected `PORT`, serving the original `solar-site/` with clean routes such as `/history` and `/evidence`. A successful response from `/` passes the deployment health check. No database or build-time content regeneration is needed.

## Verify a deployment

Check these paths beneath `https://nayiemw.github.io/solar-foundation-website/`:

| Path | Expected result |
| --- | --- |
| `/` | Homepage loads. |
| `history/` | History page loads directly and after refresh. |
| `agreement/` | Agreement page loads. |
| `report/` | Report and exhibit images load. |
| `evidence/` | Evidence rows expand to show screenshots. |
| `archive/resignation-statement-nayiem-w/` | Archived statement loads. |
| `app.js` | JavaScript is served. |
| `og.png` | Social image is served. |
| `solar-community-report.docx` | Report download is available. |
| `sitemap.xml` | Sitemap retains the canonical `solar.org` URLs. |
| An unknown path | HTTP 404. |

Also check the mobile menu, FAQ accordion and archive filters. Network metrics depend on the external Solar API; an unavailable API should show **status unknown**, not prevent the static site from loading.

For local source preview, run `node solar-site-server.js` from the repository root and visit [localhost:3100](http://localhost:3100).
