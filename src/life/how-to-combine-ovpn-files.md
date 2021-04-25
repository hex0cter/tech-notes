
# [How to combine ovpn files](https://community.openvpn.net/openvpn/wiki/IOSinline)

I had to setup openvpn on 4 non-jailbroken IOS devices yesterday. These devices were not setup to sync to computers, so I had to add the openvpn files via email. This is a bad (insecure) way to add openvpn to the devices, but in this case it was the only way, and security was not very important on this setup. If I was able to sync these devices with a computer, I could have used my original config file and cert files by adding the files from within iTunes. In order to make this work, You need to use in-line certificate files. My original config file looked like this: Before:


    client
    dev tun
    proto udp
    remote vpn.server.hostname 1194
    resolv-retry infinite
    nobind
    persist-key
    persist-tun
    ns-cert-type server
    verb 3
    ca ca.crt
    cert jeff.crt
    key jeff.key
    tls-auth ta.key 1



After changing my config files to work with in-line certificates, they looked like this: After


    client
    dev tun
    proto udp
    remote vpn.server.hostname 1194
    resolv-retry infinite
    nobind
    persist-key
    persist-tun
    ns-cert-type server
    verb 3
    key-direction 1
    <ca>
    -----BEGIN CERTIFICATE-----
    ...
    -----END CERTIFICATE-----
    </ca>
    <cert>
    -----BEGIN CERTIFICATE-----
    ...
    -----END CERTIFICATE-----
    </cert>
    <key>
    -----BEGIN RSA PRIVATE KEY-----
    ...
    -----END RSA PRIVATE KEY-----
    </key>
    <tls-auth>
    -----BEGIN OpenVPN Static key V1-----
    ...
    -----END OpenVPN Static key V1-----
    </tls-auth>



Notice that --tls-auth takes a direction (1/0) when using it from a file, but when using tls-auth inline you must also use --key-direction (1/0). Then on the Iphone/Ipad/Ipod touch go to the app store, search for openvpn connect, and install it. Then email the final config (with file extension .ovpn) as an attachment from an email account on your computer (or a webmail) to the email address setup on IOS in the Mail app. In the mail app open the email and open the .ovpn file, then choose to open it with OpenVPN. If you did it right, OpenVPN opens and you can click a + icon next to your config to import it. Now you can simply slide Off to On and your VPN connects. If your VPN server is at your house, and you are connecting to the Internet IP (as opposed to using the LAN IP in --remote) you can not connect to it from your house.
