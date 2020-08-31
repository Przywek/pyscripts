import logging
import pysftp
from base64 import decodebytes
import paramiko
import json
import re
from pprint import pprint
logger = logging.getLogger('Change_config')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('logs.log')
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(fh)
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
hostname = '192.168.1.10'
sftp_username = 'user'
sftp_pw = '####'
keydata = b"""AAAAB3NzaC1yc2EAAAADAQABAAABAQCx771e2y6lap8b8V6FfskJlWZhUW01fZRzPEMf/apuL6Lb9WxBFkPGUMaYYb5uZ2jzalRRCb3hd0eEQOdr6u8sZDME+Vqgub+oDVmVGMdgdV6chkTIFh267oSVUz9s/Ak9L+l3I16Po7ByCmw6Olr67E2VgDT3Hc3SkKnrJEyhmh8PI/ZdSE6vF9iLRT2peJGssk9o1KmY9/5aZfuDV+Uv4WAp/qvWxBl4wdVc2H6O+jrQkUHdSTxzHZQms8xPcZq8l/CyL8noas4V4zTFW5C9d13hvzEGQhP2sdRDFDNe6P2Pc5pstqJizotReLboGb7FN6jlwUuUOiYCO5FtdEjZ"""
key = paramiko.RSAKey(data=decodebytes(keydata))
cnopts = pysftp.CnOpts()
cnopts.hostkeys.add('192.168.1.10', 'ssh-rsa', key)
with pysftp.Connection(host=hostname, username=sftp_username, password=sftp_pw, cnopts=cnopts) as sftp:
    print ("Connection succesfully stablished ... ")
    sftp.chdir('/home/user/api/config')
    with open('cfg.json', mode='r', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    y = 'bearerToken:'
    z = 'config:'
    x = data['config'].split(y)[-1].split(z)[0]
    with open("replayScript.json", "w") as data_file:
        json.dump(data, data_file)
    pprint()
