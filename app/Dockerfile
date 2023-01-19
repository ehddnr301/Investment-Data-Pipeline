FROM ehddnr/investment-data-pipeline:3.0.0
MAINTAINER ehddnr

COPY . /home
WORKDIR /home

RUN pip install -q -r requirements.txt

ENTRYPOINT ["sh", "start.sh"]
