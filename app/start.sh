#!/bin/bash

echo "Start Pykrx Cron"
cp cron /etc/cron.d/cron
chmod 755 /etc/cron.d/cron
crontab /etc/cron.d/cron

cron -f