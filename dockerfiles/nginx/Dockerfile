FROM nginx:1.19.2

COPY reload_scripts /usr/local/bin
COPY configs /etc/nginx

RUN chmod +x /usr/local/bin/nginxReloader.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get install inotify-tools -y

ENTRYPOINT [ "/usr/local/bin/docker-entrypoint.sh" ]
CMD [ "nginx", "-g", "daemon off;" ]