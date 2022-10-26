#!/usr/bin/env python3


import psutil
import os
import csv
from log_generator import generate_log, generate_csv
from emails import send_email


def check_status():
    cpu_usage_percent = psutil.cpu_percent(4)
    root_disk_usage_percent = psutil.disk_usage('/').percent
    memory_usage_percent = psutil.virtual_memory().percent
    is_up = psutil.net_if_stats()['lo'].isup

    return cpu_usage_percent, root_disk_usage_percent, memory_usage_percent, is_up

def raise_alert(cpu_usage_percent, root_disk_usage_percent, memory_usage_percent, is_up):
    path = os.getcwd()
    settings_dict = {}
    text = ''
    if not os.path.isfile(path + '/settings.csv'):
        print("settings.csv is missing")
        generate_log("raise alert", os.getpid(), "settings.csv is missing", 'health_check.log')
    with open(path + '/settings.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            settings_dict = row
    print(settings_dict)
    if cpu_usage_percent >= float(settings_dict['cpu_max_usage']):
        text = 'O uso do CPU esta acima do estipulado nas configuracoes.'
        generate_log('cpu_usage_percent', os.getpid(), text, 'health_check.log')
    if root_disk_usage_percent >= float(settings_dict['disk_max_usage']):
        text = '<p>O root da maquina 10 esta com espaco livre inferior ao estipulado nas configuracoes</p><p>Limite estipulado {percent1}%</p><p>Limite medido:{percent2}%</p>'.format(percent1=settings_dict['disk_max_usage'], percent2=root_disk_usage_percent)
        generate_log('root_disk_usage_percent', os.getpid(), text, 'health_check.log')
    if memory_usage_percent >= float(settings_dict['memory_max_usage']):
        text = 'O uso de memoria RAM esta acima do estipulado nas configuracoes'
        generate_log('memory_usage_percent', os.getpid(), text, 'health_check.log')
    if is_up == False:
        text = 'O computador esta sem rede'
        generate_log('is_up', os.getpid(), text, 'health_check.log')
    if text != '':
        send_email(text, 'andersonabe@cml.pr.gov.br')
    else:
        print("There is no alert to raise")

if __name__ == "__main__":
    cpu_usage_percent, root_disk_usage_percent, memory_usage_percent, is_up = check_status()
    generate_log('health_check', os.getpid(), 'CPU usage: {percent}%'.format(percent=cpu_usage_percent), 'health_check.log')
    generate_log('health_check', os.getpid(), 'Disk usage by root partition: {percent}%'.format(percent=root_disk_usage_percent), 'health_check.log')
    generate_log('health_check', os.getpid(), 'Memory usage {percent}%'.format(percent=memory_usage_percent), 'health_check.log')
    generate_log('health_check', os.getpid(), 'Network status is up: {boolean_value}'.format(boolean_value=is_up), 'health_check.log')
    generate_csv(cpu_usage_percent, root_disk_usage_percent, memory_usage_percent, is_up)
    raise_alert(cpu_usage_percent, root_disk_usage_percent, memory_usage_percent, is_up)
