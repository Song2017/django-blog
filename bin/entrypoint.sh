#!/usr/nginx/env bash
set -e

python --version

echo "INFO: config nginx ..."
echo '''
# user  nginx www-data;
worker_processes  1;

pid /var/run/nginx.pid;

events {
    worker_connections  1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    gzip  on;
    gzip_min_length 1;
    gzip_comp_level 1;
    gzip_types text/css application/xml image/jpeg image/gif image/png;

    #proxy_cache_path /data/nginx/tmpcache levels=2:2 keys_zone=two:10m loader_threshold=300
    #                   loader_files=200 max_size=200m inactive=1m;

    proxy_headers_hash_max_size 51200;
    proxy_headers_hash_bucket_size 6400;

    upstream proxyupstream {
        server unix:/tmp/gunicorn.sock fail_timeout=0;
    }

    server {
        listen       8080;
        server_name  localhost 127.0.0.1;

        charset utf-8;
        default_type 'text/html';

        # 日志
        #access_log /app/logs/nginx.access.log main;
        #error_log /app/logs/nginx.error.log;

        location /static/ {
           alias /app/server/static/;
        }
        location /techarea/ {
           autoindex on;
           alias /app/git/;
        }

        location / {
	        try_files $uri @proxy_to_app;
        }

        location @proxy_to_app {
            proxy_pass http://proxyupstream;
            proxy_headers_hash_bucket_size 64;
            proxy_set_header Host $http_host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_redirect off;
            client_body_in_single_buffer on;
            add_header Cache-Control 'max-age=3,stale-while-revalidate=3';
            add_header Vary *;
            add_header X-Accel-Expires 3;
	    }
    }
}

daemon off;
'''> /etc/nginx/nginx.conf # supervisord as daemon process
# chown app folder
chown -R www-data:www-data /app


# Start Supervisor
echo """
[supervisord]
nodaemon=true

[program:guncorn]
command=/usr/local/bin/gunicorn --workers 3 --threads 2 --bind unix:/tmp/gunicorn.sock server.wsgi:application
stdout_logfile=/dev/stdout
stdout_logfile_maxbytes=0
stderr_logfile=/dev/stderr
stderr_logfile_maxbytes=0
directory=/app/server
autostart=true
autorestart=true
environment=LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8

[program:nginx]
command=/usr/sbin/nginx -c /etc/nginx/nginx.conf
stdout_logfile=/dev/stdout
stdout_logfile_maxbytes=0
stderr_logfile=/dev/stderr
stderr_logfile_maxbytes=0
stopsignal=QUIT
""" >/etc/supervisor/conf.d/supervisord.conf
exec /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf

echo "INFO: Command Mode ..."
echo "$@"
