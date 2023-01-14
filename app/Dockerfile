FROM ehddnr/investment-data-pipeline
MAINTAINER ehddnr

RUN apt-get update && apt-get install -y cron

COPY . /home
WORKDIR /home

RUN pip install -q -r requirements.txt

ENTRYPOINT ["sh", "start.sh"]
