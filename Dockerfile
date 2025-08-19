FROM python:3.12-slim

WORKDIR /Cropcure

COPY . /Cropcure

RUN pip install  --no-cache-dir  -r requirements.txt

EXPOSE 7860


CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app"]
