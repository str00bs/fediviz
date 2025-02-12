FROM python:3.13-slim

# ? Setup application directory
COPY src/ /app
COPY pyproject.toml /app/pyproject.toml
COPY dist.env /app/.env
COPY LICENSE.md PRIVACY.md README.md /app/
COPY LICENSE.md PRIVACY.md README.md /app/fediviz/static/

# ? Set cwd to app
WORKDIR /app

# ? Setup package management
RUN apt-get update && apt-get install --no-install-suggests --no-install-recommends --yes pipx
ENV PATH="${PATH}:/root/.local/bin"
RUN pipx install poetry

# ? Install dependencies
RUN poetry install

# ? Setting up global app variables
ENV PYTHONPATH "${PYTHONPATH}:/app"

# ? Run app
CMD ["poetry", "run", "streamlit", "run", "fediviz/__main__.py"]

# ? Expose app to internet
EXPOSE 80
