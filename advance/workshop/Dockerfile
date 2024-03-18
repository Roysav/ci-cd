FROM python as builder


WORKDIR /app
COPY . /app

FROM python as test
COPY --from=builder /app /app
WORKDIR /app
RUN python3 -m pip install pytest
RUN python3 -m pip install -e '.[dev]'
RUN ["python3", "-m", "pytest"]


FROM python:slim
COPY --from=builder /app /app
WORKDIR /app
ENV FLASK_APP=talkshow/app.py
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST='0.0.0.0'
ENV FLASK_RUN_PORT=5002

RUN python3 -m pip install -e '.[dev]'

CMD ["python3", "-m", "flask", "run"]