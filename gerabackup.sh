#!/bin/sh
#
cd /root/scripts/BackupGrafana
/root/scripts/BackupGrafana/backup-grafana-dash.py
mv *.json /home/backup/grafana_dash/