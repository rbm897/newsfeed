FROM tiangolo/uwsgi-nginx:python3.7

LABEL maintainer="Ram Bhajan Mishra <rbm897@gmail.com>"
    
# Place your flask application on the server
COPY requirement.txt /app
RUN pip install -r requirement.txt
COPY ./templates /app/templates
COPY ./ /app/
WORKDIR /app

RUN echo 'export FLASK_APP="/app/news_extractor.py"' >> ~/.bash_profile
RUN echo 'export FLASK_APP="/app/news_extractor.py"' >> ~/.bashrc
RUN /bin/bash -c "source ~/.bashrc"

EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]