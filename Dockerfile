FROM continuumio/anaconda3

WORKDIR /usr/local/bin/
COPY recvall.py s.py ./
ENTRYPOINT "python" "s.py"
