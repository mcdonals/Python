#!/usr/bin/python3
import getpass
import urllib.request
import urllib.parse

username = input("Username: ")
password = getpass.getpass()

#print("username: ", username)
#print("password: ", password)

data = urllib.parse.urlencode({'type': 'normal', 'username': username, 'password': password})
data = data.encode('ascii')
url = "https://api.taiga.io/api/v1/auth"

with urllib.request.urlopen(url, data) as f:
    #print(f.read().decode('utf-8'))
    x = f.read().decode('utf-8')

print(x.count('auth_token'))
y = x.index('auth_token')
print(y)
print(x[y+1])
