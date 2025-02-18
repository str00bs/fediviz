# 📊 FediViz
[![Build Status](https://ci.cloud.adapdr.me/api/badges/str00bs/fediviz/status.svg?ref=refs/heads/main)](https://ci.cloud.adapdr.me/str00bs/fediviz)
[![Build Status](https://ci.cloud.adapdr.me/api/badges/str00bs/fediviz/status.svg?ref=refs/heads/ci_tmp)](https://ci.cloud.adapdr.me/str00bs/fediviz)
Is a free, open-source and privacy first visualisation tool, that is purpose-built for Mastodon utilizing user exports.
- 👱 Account overview with highlights & stats from your page.
- 📑 Bookmarks page with granular breakdown of available stats & metrics
- 👍 Likes *(favourites)* page with granular breakdown of available stats & metrics
- ✉️ Posts *(including boosts)* page with granular breakdown of available stats & metrics



## 📋 Preface
Please have a look at the supporting documents ⤵️
- [🤝 Contribution guide](./CONTRIBUTING.md)
- [🧑‍⚖️ License agreement](./LICENSE.md)
- [🛡️ Privacy statement](./PRIVACY.md)
- [✨ Asset credits](./CREDITS.md)


## ⚙️ Setup
This section contains steps for how to setup and run the application in various cases.

### Local
1. Install dependencies: `poetry install`
2. Copy configuration files
   - `mkdir src/.streamlit && cp dist.config.toml src/.streamlit/config.toml`
   - `cp dist.env src/.env`
3. Copy markdown pages:
   - `cp LICENSE.md src/fediviz/static/LICENSE.md`
   - `cp README.md src/fediviz/static/README.md`
   - `cp PRIVACY.md src/fediviz/static/PRIVACY.md`

### Docker
1. Build image: `docker build . --tag=fediviz:local`
2. Run image: `docker run fediviz:local`

### Production
The recommended way of deployment, is using the provided `prod.docker-compose.yml`
which uses traefik (with docker detection & LetsEncrypt) for SSL.

You can do this by
1. Cloning the repository: `git clone https://github.com/str00bs/fediviz.git && cd fediviz`
2. Copying over the compose file: `cp prod.docker-compose.yml docker-compose.yml`
3. And running it `docker-compose up -d `

Please note that this is the _primary_ method of deployment, feel free to do it differently or suggest other alternatives via PRs and issues.


## 🧑‍🔬 Testing
These instructions will be expanded upon by release `0.7.0 - Testable App`


## 🧰 Resources
Resources provided for the repository and application.

- IDE Configurations: [VSCode](resources/.vscode)
- Conventional Commits: [CC Docs](https://www.conventionalcommits.org/en/v1.0.0/)
  - Extension: [CC Ext](https://marketplace.visualstudio.com/items?itemName=vivaxy.vscode-conventional-commits)
- Graphing Framework: [Streamlit](https://docs.streamlit.io/)
   - Interface Components: [Streamlit Extras](https://extras.streamlit.app/)
   - Graphing Components [Plotly Dash](https://dash.plotly.com/)
- Web Requests: [Requests](https://requests.readthedocs.io/en/latest/)
- Settings Management: [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- Code Quality: [Deepsource](https://docs.deepsource.com/docs/introduction)
