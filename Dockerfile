FROM alpine:3.18
RUN apk add --no-cache bash
WORKDIR /workspace
CMD ["/bin/sh"]
