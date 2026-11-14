FROM python:3.12-alpine

LABEL org.opencontainers.image.title="ZPilot discovery runtime"
LABEL org.opencontainers.image.description="Read-only ZPilot repository discovery container"
WORKDIR /workspace

RUN apk add --no-cache git \
    && addgroup -S zpilot \
    && adduser -S -G zpilot -u 10001 zpilot

COPY zpilot.py /opt/zpilot/zpilot.py
USER 10001:10001

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python", "/opt/zpilot/zpilot.py"]
CMD ["--discover-only", "--json"]
