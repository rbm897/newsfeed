FROM python:3.8.1

LABEL maintainer="Ram Bhajan Mishra <rbm897@gmail.com>"

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python app.py"]