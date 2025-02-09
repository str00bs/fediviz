# FediViz <img src='resources/images/bar-chart.png' width=32 alt="bar chart">

This repository contains a visualisation tool built on mastodon accountexports.
- For the apps license agreement, see `LICENSE.md`
- For the apps privacy statement, see `PRIVACY.md`

## Setup
This section contains steps for how to setup and run the application in various cases.

### For local runs
1. Install dependencies: `poetry install`
2. Copy configuration files
   - `mkdir src/.streamlit && cp dist.config.toml src/.streamlit/config.toml`
   - `cp dist.env src/.env`
3. Copy markdown pages:
   - `cp LICENSE.md src/fediviz/static/LICENSE.md`
   - `cp README.md src/fediviz/static/README.md`
   - `cp PRIVACY.md src/fediviz/static/PRIVACY.md`

### For docker runs
1. Build image: `docker build . --tag=fediviz:local`
2. Run image: `docker run fediviz:local`

### For production
TODO: Write instructions

## Testing
TODO: Setup test suite, and write instructions.

## Contributing
TODO: Write contribution guide.

## Resources
TODO: Write resources overview, so that people may learn the used tools.

### Credits
TODO: Filter and include the credits here, once it's clear which assets will be used.

## Housekeeping
A list of non-urgent TODO's
1. Setup badges
2. ~~Activate deepsource~~
3. ~~Activate dependabot~~
4. ~~Activate securitybot~~
5. ~~Run static analysis~~
6. ~~Make first release for github and dockerhub~~
7. ~~Add VSC helpers.~~
8. Write tests.
