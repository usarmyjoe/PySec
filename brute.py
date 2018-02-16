#!/usr/bin/python3
import paramiko

def main():
    user = 'root'
    passw = 'passw'
    uphash = [('root','password'),('root','password2'),('happy','cow')]
    ip = '127.0.0.1'
    port = 22
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy)
    for u,p in uphash: 
        try:
            print(u,p)
            client.connect(ip, port=port, username=u,password=p)
        except paramiko.AuthenticationException:
            print(ip,':', port,'', " Authentication Failed", sep='')
        except paramiko.NoValidConnectionsError:
            print(ip,':', port,'', " Network Error", sep='')
        except paramiko.BadAuthenticationType:
            print(ip,':', port,'', " Unsupported Authentication Type", sep='')

if __name__ == "__main__":
    main()
