# Стадия 1: Сборка отчета
FROM python:3.12-alpine AS build
WORKDIR /src
COPY tools/ tools/
COPY data/ data/
RUN python tools/build_report.py

# Стадия 2: Прогон тестов
FROM python:3.12-alpine AS test
COPY --from=build /src /src
WORKDIR /src
COPY tests/ tests/
RUN python -m unittest discover -s tests -v

# Стадия 3: Финальный чистый образ
FROM python:3.12-alpine
WORKDIR /shym-rent
COPY app/server.py .
COPY --from=test /src/out/report.json .
ENV BRANCH="Shymbulak"
ENV TOP="5"
EXPOSE 8080
CMD ["python", "server.py"]