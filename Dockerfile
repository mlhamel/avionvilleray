FROM        mlhamel/mlhamel.base

WORKDIR     /home
RUN         mkdir /home/avionvilleray
COPY        . /home/avionvilleray/
RUN         cd /home/avionvilleray && pip install --editable .
RUN         mkdir -p /var/run/circus

EXPOSE      6543

WORKDIR     /home/avionvilleray
CMD         /usr/local/bin/circusd /home/avionvilleray/development.ini