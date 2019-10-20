# News extractor

This application displays latest news for given category.

## Installation

git clone https://github.com/rbm897/newsfeed.git

cd newsfeed

sudo docker build -t newsfeed .

sudo docker run -it -p 5000:5000 -e FLASK_APP=news_extractor.py newsfeed

http://localhost:5000