# [Make a skype call through DBUS](http://live.gnome.org/Vala/DBusClientSamples#Skype_status_client)

DBUS connections:
```
--name "com.Skype.API" --path="/com/Skype" --interface "com.Skype.API"
```

Method:
```
Invoke("Name skype-client")
Invoke("PROTOCOL 5")  or Invoke("PROTOCOL 2")
Invoke("CALL echo123") or Invoke("CALL +861234567890")
```

