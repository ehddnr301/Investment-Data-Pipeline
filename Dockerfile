FROM ehddnr/investment-data-pipeline
MAINTAINER ehddnr

COPY . /home
WORKDIR /home

RUN pip install -q -r requirements.txt

ENTRYPOINT ["sh", "start.sh"]
