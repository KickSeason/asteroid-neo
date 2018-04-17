FROM ubuntu:16.04

#expose ports


ADD . /var/www/asteroid-neo

ENV DOTNET_CLI_TELEMETRY_OPTOUT 1

RUN /var/www/asteroid-neo/install.sh

EXPOSE 20332
EXPOSE 20333

COPY crontab /etc/cron.d/state
RUN chmod 0644 /etc/cron.d/state

CMD ./var/www/asteroid-neo/run.sh 
