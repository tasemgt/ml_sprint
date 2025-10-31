FROM agrigorev/zoomcamp-model:2025
# add your stuff here

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /code

ENV PATH="/code/.venv/bin:$PATH"

COPY "pyproject.toml" "uv.lock" ".python-version" ./

RUN uv sync --locked

COPY "predict.py" ./

EXPOSE 9696

ENTRYPOINT ["uv", "run", "uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "9696"]