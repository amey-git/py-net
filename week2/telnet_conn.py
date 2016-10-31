#!/usr/bin/env python

import telnetlib
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 5

def telnet_connect(ip_addr, TELNET_PORT, TELNET_TIMEOUT, username, password):
    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    print remote_conn.read_until("sername:", TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    print remote_conn.read_until("assword:", TELNET_TIMEOUT)
    remote_conn.write(password + '\n')
    time.sleep(1)
    remote_conn.read_very_eager()
    return remote_conn
       

def send_commands(remote_conn, cmd):
    remote_conn.write(cmd + '\n')
    time.sleep(1)
    print remote_conn.read_very_eager()
    

def main():
    
    ip_addr = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass'

    remote_conn_main = telnet_connect(ip_addr, TELNET_PORT, TELNET_TIMEOUT, username, password)
    
    #remote_conn.read_until("username", TELNET_TIMEOUT)
    #remote_conn.write('pyclass'+'\n')
    #remote_conn.read_until('password',TELNET_TIMEOUT)
    #remote_conn.write('88newclass'+'\n')
    #remote_conn.write('sh ip int br'+'\n')
    send_commands(remote_conn_main, 'sh ip int br')
    remote_conn_main.close()

if __name__ == '__main__':
    main()
