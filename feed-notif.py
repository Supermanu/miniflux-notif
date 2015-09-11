#!/usr/bin/python3

## Copyright (C) 2015 Manuel Tondeur
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.


import requests
import json
from requests.auth import HTTPBasicAuth
import subprocess

url = "http://localhost/miniflux/jsonrpc.php"
user = "yourUsername"
password = "yourPassword"
conn = {"jsonrpc": "2.0",
        "method": "item.count_unread",
	        "id": 1,
		    }

response = requests.post(
        url, data=json.dumps(conn), auth=HTTPBasicAuth(user, password)).json()

unread_items = response['result']
if (unread_items > 0):
    subprocess.Popen(['kdialog', '--title', 'New feeds','--passivepopup','There are %i feeds unread' % unread_items])

