FROM python

# Use bash instead of sh
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

WORKDIR /project

# install everything onto the image
RUN \
  apt-get update && \
  apt-get install -y nano
RUN \
  pip3 install numpy && \
  pip3 install nltk

COPY sample.txt /project/
COPY phrasefinder.py /project

ENTRYPOINT python phrasefinder.py
