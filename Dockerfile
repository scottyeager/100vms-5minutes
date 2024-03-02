FROM alpine
COPY get.sh /
ENTRYPOINT /get.sh
