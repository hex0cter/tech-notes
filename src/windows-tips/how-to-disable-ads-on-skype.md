# [How to disable ads on Skype](http://superuser.com/questions/677293/disable-advertisements-on-skype)


You need to add entries to your `hosts` file, typically located here:`C:\Windows\System32\drivers\etc\hosts`

These are hostnames you'll want to block, by adding them to the `hosts` file:


    127.0.0.1     rad.msn.com
    127.0.0.1     g.msn.com
    127.0.0.1     live.rads.msn.com
    127.0.0.1     ads1.msn.com
    127.0.0.1     static.2mdn.net
    127.0.0.1     ads2.msads.net
    127.0.0.1     a.ads2.msads.net
    127.0.0.1     b.ads2.msads.net
    127.0.0.1     ad.doubleclick.net
    127.0.0.1     ac3.msn.com
    127.0.0.1     ec.atdmt.com
    127.0.0.1     msntest.serving-sys.com
    127.0.0.1     sO.2mdn.net
    127.0.0.1     aka-cdn-ns.adtech.de
    127.0.0.1     secure.flashtalking.com
    127.0.0.1     cdn.atdmt.com


Source of hostnames here: [wikiHow](http://www.wikihow.com/Stop-All-the-Ads-in-Hotmail), and [Skype forum](http://community.skype.com/t5/Windows-desktop-client/skype-ad-spam-disable/td-p/12156). Just a warning, but Microsoft Security Essentials (MSE) may think your hosts file was hijacked, so if you have issues make sure to allow the changes through MSE.
