# Solar Foundation static site

The committed HTML, JavaScript, images and documents for the [Solar Foundation website](https://solar.org). This directory is also the input for the [GitHub Pages mirror](https://nayiemw.github.io/solar-foundation-website/).

## Preview

From the repository root:

```sh
node solar-site-server.js
```

Open [localhost:3100](http://localhost:3100). Use this server to resolve the source site's extensionless navigation routes correctly.

## Content

| Page | Content |
| --- | --- |
| `index.html` | Project overview and network status. |
| `history.html` | Sourced project timeline. |
| `core5.html` | Core 5.0 upgrade record. |
| `agreement.html` | Published Token Swap Agreement. |
| `report.html` | Community report and downloadable document. |
| `evidence.html` | Searchable index of 82 screenshot exhibits. |
| `governance.html` | Governance proposal and vote record. |
| `status.html` | Network status and browser-fetched metrics. |
| `exchanges.html` | Exchange and network information. |
| `faq.html` | Frequently asked questions. |
| `archive.html` and `archive/` | Searchable archive and local statement snapshots. |

`app.js` provides navigation, accordions, archive filtering, evidence expansion and network metrics. It requests block and supply data from `https://api.solar.org` every 30 seconds on pages that display live data. If the API cannot be reached, the chain indicator shows **status unknown**.

## Publishing

GitHub Pages receives a packaged copy of this directory, with directory index routes and local URLs adapted to `/solar-foundation-website/`. Existing `solar.org` canonical metadata remains intact.

Make changes on `dev`. Publishing happens only after a `dev` → `prod` pull request is merged. See [deployment instructions](DEPLOY.md) for the packaging command and verification steps.

The historical scripts under `solar-build/` require original authoring inputs. They are not a prerequisite for deploying these committed files.
