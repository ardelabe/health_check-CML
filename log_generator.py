#!/usr/bin/env python3


from datetime import datetime
import os
import csv


# os.getpid()
# os.path.realpath(__file__)
def generate_log(service, pid, message, filename):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    text = "{now} {service}[{pid}]: {message}".format(now=now, service=service, pid=pid, message=message)
    path = os.path.realpath(__file__)[:-17] + '/log'
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + '/' + filename, 'a') as f:
        f.write(text + '\n')

def generate_csv(CPU, disk, memory, network):
    path = os.path.realpath(__file__)[:-17] + '/log'
    keys = ['date_and_time', 'CPU', 'disk', 'memory', 'network']
    date_and_time = datetime.now().isoformat()
    check = {'date_and_time': date_and_time, 'CPU': CPU, 'disk': disk, 'memory': memory, 'network': network}
    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.isfile(path + '/health_check.csv'):
        with open(path + '/health_check.csv', 'w') as info_csv:
            writer = csv.DictWriter(info_csv, fieldnames=keys)
            writer.writeheader()
    with open(path + '/health_check.csv', 'a') as info_csv:
        writer = csv.DictWriter(info_csv, fieldnames=keys)
        writer.writerow(check)


if __name__ == "__main__":
    print(os.path.realpath(__file__)[:-17])