FROM python:3.6

# Install supervisor
RUN apt-get update && apt-get install -y supervisor

# Create directories for supervisor
RUN mkdir -p /var/log/supervisor
RUN mkdir -p /etc/supervisor/conf.d

WORKDIR /app
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

RUN groupadd -g 20 dialout && usermod -a -G dialout root

# Copy supervisor configuration files
COPY supervisord.conf /etc/supervisor/supervisord.conf
COPY gps_serial.conf /etc/supervisor/conf.d/gps_serial.conf
COPY ferex_serial.conf /etc/supervisor/conf.d/ferex_serial.conf

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
