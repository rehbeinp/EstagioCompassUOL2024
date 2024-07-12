FROM python:3

RUN python -m ensurepip --default-pip

RUN pip install boto3

RUN pip install botocore

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install -i /usr/local/aws-cli -b /usr/local/bin \
    && rm awscliv2.zip

COPY ./Filmes+e+Series/movies.csv /RawZone/

COPY ./Filmes+e+Series/series.csv /RawZone/

COPY parte1.py /RawZone/

WORKDIR /RawZone/
