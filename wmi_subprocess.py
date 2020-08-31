import logging
import subprocess
import wmi
import os
import time
import getpass
logger = logging.getLogger('Application properties configurator')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('logs_app.log')
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(fh)
hostname = []
dir_path = os.getcwd()
with open(dir_path+"\\ip.txt",'r') as f:
    for line in f:
        mpk1 = line.replace("\n", "")
        hostname.append(mpk1)
app_prop_cur = open(dir_path +"\\application.properties", "r+",encoding='cp1252')
cv1 = app_prop_cur.read()
app_prop_cur.close()
username = input("Nazwa Uzytkownika? ")
password = getpass.getpass("Password: ")
for x in hostname:
    try:
        c = wmi.WMI(x, user=username, password=password)
        for service in c.Win32_Service(Name="api"):
            result, = service.StopService()
            if result == 0:
                print("Service", service.Name, "stopped")
                logger.error("Service "+service.Name+"stopped: " + x)
            else:
                logger.error("SMth went wrong with restarting service: " + x)
        logger.info("Rozpoczalem w : " + x)
        subprocess.call(r'net use m: \\'+ x+'\d$', shell=True)
        app_prop= open('M:\\custom\\api\\application.properties',"r+",encoding='cp1252')
        contents =app_prop.read()
        y = 'api.rest='
        z = 'api.source='
        id_wbo = contents.split(y)[-1].split(z)[0]
        app_prop.close()
        cv1 = cv1.replace('014', id_wbo)
        cv1 = cv1.replace('192.168.1.10', x)
        with open('M:\\custom\\api\\application.properties',"w+",encoding='cp1252') as f:
            f.truncate(0)
            f.write(cv1)
            f.close()
        cv1 = cv1.replace(id_wbo, '014')
        cv1 = cv1.replace(x, '192.168.1.10')
        subprocess.call(r'net use m: /del', shell=True)
        logger.info("Skonczylem w : " + x)
        time.sleep(5)
        for service in c.Win32_Service(Name="api"):
            result, = service.StartService()
            if result == 0:
                logger.error("Service " + service.Name + "started: " + x)
            else:
                logger.error("SMth went wrong with restarting service: " + x)
    except:
        logger.error("Nie moglem sie polaczyc : " + x)
        continue
