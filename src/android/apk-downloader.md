
date: 2012-02-24 16:15:57  
author(s): redphx  

# [[Official] APK Downloader – Download APK files from Android Market to PC](http://codekiem.com/2012/02/24/apk-downloader/)

**Update 02/13/2013:** If you’re using Android 2.2+ on a rooted device and having problem downloading incompatible apps, please try **[Market Helper](http://codekiem.com/market-helper)**

**First:** this project is made for my personal needs, then I decide to publish it because I think some people may need it. This is not a tool for pirating. It’s good or bad depend on how you use it. Please don’t make me look bad because of this.

**This is the official page of APK Downloader. Do not download the extension from other sources.**

**Use at your own risk. I’ll not take responsibility for anything happen to you or your account.**

![](https://i1.wp.com/codekiem.com/wp-content/uploads/2012/02/apk-big.png?resize=400%2C186)

> **APK Downloader** is a Google Chrome extension that allows you to download Android APK files from Android Market to your PC

**See it in action:**

  


**Download and Install:[ View this page for version 2.0](http://codekiem.com/2014/08/07/official-apk-downloader-v2/)**

After installed APK Downloader, you’ll need to follow these steps in able to use it

**I. Enter email and device ID on Options page**

**1.** There are two ways to get Email and Device ID

**a. Easy way:** install this **[Device ID](https://market.android.com/details?id=com.redphx.deviceid)** app, it will show you your emails and Device ID

**b. Difficult way:** Open dial pad, call ***#*#8255#*#*** ( 8255 = TALK ). If it opens “GTalk Service Monitor”, find lines that begin with **JID** and **Device ID**. Your email is **JID** , and your device id is a string that after **android-** prefix

For example: if it shows android-1234567890abcdef , then your device ID is **1234567890abcdef**

Do not type in random email or device ID, it won’t work

**2.** Enter your email’s password, then press **Login**. If everything is ok, now you can use **APK Downloader**

**III. Start using**

After finished two steps above, you can start using **APK Downloader**. Open **[Android Market](https://market.android.com)** , view any FREE apps ( for example: **[Simple Text](https://market.android.com/details?id=com.redphx.simpletext)** ), then press the **APK Downloader** icon on address bar ( see screenshot )

![](https://i2.wp.com/i.imgur.com/BAf91.png?resize=580%2C86)

**IV. FAQs:  
**

  * **Is is against Android Market’s ToS?  
** – I’m afraid that it is. Please read **[Section 3.3](https://www.google.com/mobile/android/market-tos.html) ** for more information. So again, you at your own risk.
  * **Where is the Options page?**  
– Click on the Wrench icon on the toolbar, go to Tools -> Extensions. Find APK Downloader. At the end of its description, you’ll see a link to Options page.
  * **Why do I have to enter my email, password and device ID? Does it store or send my password to another place?**  
– The extension only stores email, device id and Android Market cookie in Chrome local storage, on your computer. To be able to get Android Market cookie, it needs your email and password to login at <https://www.google.com/accounts/ClientLogin> . After it’s done, password is not stored, email is stored to display on Options page, Device ID and Cookie are stored for later requests. I do not send those information to another sites.
  * **Why don’t you just put one account in the extension, so we don’t have to use our information ?  
** – That’s good for users, but not for developers like us. For example, when 1000 users download same app, it only counts 1.
  * ****Again, do you collect our information?****
  * – I don’t want to get into trouble by collecting users information, so I try not to have it in any way. The only thing I’m collecting is which apps are downloaded by users. You can view the source code to make sure about this.
  * ****Can it download paid apps?****
  * – No, of course not, unless you purchased it with your logged account before. Please remember this isn’t a tool for pirating.
  * **Why do you make this extension?  
** – I’m an Android developer. While working on my new project, I have to decompile some apps on Android Market. Everytime I want to decompile one, I have to download it to my phone, use Astro to backup it to SDCard, connect phone to PC, then copy the apk file. That’s a really long and painful to me, because I have to do it over and over again. That’s why I come up with this idea.



**V. Changelogs:**

  * **1.4.3:** 07/16/2013 
    * Supports new Google Play layout. **Note:** if you have problems, switch to **[English language](https://play.google.com/?hl=en)**  

  * **1.4.2:** 03/04/2013 
    * This version is made by **Stephan Schmitz** , **Peter Wu** from [this repository](https://github.com/Lekensteyn/apk-downloader). Big thanks to them. I’m planning adding more features in the future.
  * **1.2.1:** 03/07/2012 
    * Switches from **android.market.com** to **play.google.com**
  * **1.2:** 02/27/2012 
    * Disable download button on paid apps
    * New feature: Change sim operator
  * **1.0:** 02/24/2012 



**I wanna say thanks to[@alexandre_t](https://twitter.com/alexandre_t) for his [Android Market API](https://code.google.com/p/android-market-api/)** , **Stephan Schmitz** and **Peter Wu** for making the [updated version](https://github.com/Lekensteyn/apk-downloader)

It took me 1 week to finish this, so hope you guys enjoy this 🙂

You can contact me at: **redphoenix89 [ at ] yahoo [ dot ] com**

Greetings from Vietnam 🙂

