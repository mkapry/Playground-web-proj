FROM python:3.5.6
ADD . /proj
COPY . /proj
RUN pip3 install -r /proj/src/requirements.txt
EXPOSE 8000
VOLUME /proj
WORKDIR /proj/src
