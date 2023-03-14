FROM python:3.9.16-slim-buster

LABEL maintainer="Songgs<bensong2017@hotmail.com>"

ARG PG_CONF=''
ARG AREA=china

COPY . /app

WORKDIR /app

# Install Supervisord, nginx mirrors.huaweicloud.com
# nginx serve static files
# gunicorn serve django server
# RUN set -ex \
#     && if [ 'china' = "$AREA" ] ; then \
#         sed -i "s@http://deb.debian.org@https://mirrors.aliyun.com@g" /etc/apt/sources.list; \
#         sed -i "s@http://security.debian.org@http://mirrors.aliyun.com@g" /etc/apt/sources.list; \
#     fi \
#     && apt-get update \
#     && apt-get install -y supervisor nginx  \
#     && rm -rf /var/lib/apt/lists/*

RUN set -ex \
    && mkdir -p .pip  \
    && if [ 'china' = "$AREA" ] ; then \
      pip3 install -i https://pypi.douban.com/simple/ --upgrade pip; \
      pip3 install -i https://pypi.douban.com/simple/ -r requirements.txt; \
    else \
      pip3 install --upgrade pip; \
      pip3 install -r requirements.txt; \
    fi
# product server
# ENTRYPOINT ["sh", "/app/bin/entrypoint.sh"]
# CMD["bash"]

# fc server
ENTRYPOINT ["sh", "/app/bin/run_server_fc.sh"]