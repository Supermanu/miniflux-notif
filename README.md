# miniflux-notif
A simple python3 script to notify new feeds on KDE.

In order to work you need to replace your host url, username and API key from miniflux API.
Those can be find in miniflux settings.
```
url = "http://localhost/miniflux/jsonrpc.php"
user = "yourUsername"
password = "yourPassword"
```

### Other DE
`miniflux-notif` can be easily changed to be Desktop Environment agnostic. You just need to change the following:
```
	subprocess.Popen(['kdialog', '--title', 'New feeds','--passivepopup','There are %i feeds unread' % unread_items])
```
to
```
	subprocess.Popen(['notify-send', 'There are %i feeds unread' % unread_items])
```