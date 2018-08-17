FROM alpine:3.8

RUN echo 'http://dl-cdn.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories && \
  apk --no-cache add \
    bash \
    sed \
    gcc \
    gfortran \
    g++ \
    musl-dev \
    lapack-dev \
    freetype-dev \
    supervisor \
    python3 \
    python3-dev

RUN pip3 install --upgrade pip && \
    ln -snf /bin/bash /bin/sh && \
    rm -fr /var/cache/apk/* && \
    pip3 install flask && \
    pip3 install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.9.0-cp36-cp36m-linux_x86_64.whl

COPY docker/conf/supervisord.conf /etc/supervisor.d/supervisord.ini
COPY docker/conf/.bashrc /root/.bashrc
COPY docker/start.sh /bin/original_start.sh

RUN sed -i -e 's/\r$//' /root/.bashrc && \
    tr -d '\r' < /bin/original_start.sh > /bin/start.sh && \
    chmod -R 700 /bin/start.sh

COPY . /var/app

WORKDIR /var/app

EXPOSE 80

ENV TERM xterm-color

CMD ["sh", "/bin/start.sh"]