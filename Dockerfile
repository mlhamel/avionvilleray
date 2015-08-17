FROM        mlhamel/mlhamel.base

WORKDIR     /home
RUN         mkdir /home/atelierlaurier
COPY        . /home/atelierlaurier/
RUN         cd /home/atelierlaurier && pip install --editable .
RUN         mkdir -p /var/run/circus

EXPOSE      6543

WORKDIR     /home/atelierlaurier
CMD         /usr/local/bin/circusd /home/atelierlaurier/development.ini