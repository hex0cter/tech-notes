
date: None  
author(s): None  

# [Setup your own Raspberry Pi AirPlay Receiver - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/setup-your-own-raspberry-pi-airplay-receiver)

This tutorial primarily involves you connecting your Raspberry Pi to your speakers then installing software so that it becomes recognized as an AirPlay receiver on your internet network. To set up your AirPlay Receiver, we will be making use of the open source software called Shairport Sync.

This software allows the Raspberry Pi to act as an AirPlay receiver by implementing Apple’s proprietary protocols so that it can receive music from those devices.

This setup will allow you to play music from any AirPlay-enabled device to your Raspberry Pi meaning you can use almost any iPhone product and even some Android products with a compatible app installed.

A Raspberry Pi AirPlay Receiver is very simple and cost-efficient way to setup wireless speakers without the huge cost of buying a set of wireless speakers. It can easily help you modernize your speakers and help cut the cord.

As a bonus, this tutorial works perfectly alongside our [Raspberry Pi Alexa tutorial](https://pimylifeup.com/raspberry-pi-alexa/) and is excellent for bringing in music support to the tutorial.

##  Equipment List

Below are all the bits and pieces that I used for this Raspberry Pi AirPlay Receiver tutorial, you will need an internet connection to be able to complete this tutorial.

### Recommended

[Raspberry Pi](https://go.pimylifeup.com/l8KF94/amazon/raspberrypi) 2 or 3

[Micro SD Card](https://go.pimylifeup.com/DUVENo/amazon/microsdcard)

[Power Supply](https://go.pimylifeup.com/TwjJnF/amazon/powersupply)

[Network Connection](https://go.pimylifeup.com/9YIU76/amazon/ethernetcord)

[Speakers](https://go.pimylifeup.com/5qFXQ6/amazon/speakers)

[AirPlay enabled device](https://go.pimylifeup.com/2zdjTd/amazon/iphone)

### Optional

[Raspberry Pi Case](https://go.pimylifeup.com/vbWKKX/allraspberrypicases)

##  Setting up an Apple AirPlay Receiver

Setting up your Raspberry Pi AirPlay receiver is an incredibly simple task, as long as you have a good internet connection and a set of speakers to connect your Raspberry Pi to it is a relatively straightforward process.

1. Before we get started let’s first run an [update and upgrade on our Raspberry Pi](https://pimylifeup.com/update-raspbian/) to ensure we are running the latest software.
    
    
    sudo apt-get update
    sudo apt-get upgrade

2. Once that has completed we need to install several different packages, run the following commands on your Raspberry Pi to install all of the packages that we need.
    
    
    sudo apt-get install autoconf libtool libdaemon-dev libasound2-dev libpopt-dev libconfig-dev
    sudo apt-get install avahi-daemon libavahi-client-dev
    sudo apt-get install libssl-dev
    

3. We will now clone the [shairport-sync source](https://github.com/mikebrady/shairport-sync) to our Raspberry Pi. Shairport-Sync is the best fork of the original Shairport code and allows syncing across multiple rooms.

Run the following commands on your Raspberry Pi to download the source code to your Raspberry Pi.
    
    
    cd ~
    git clone https://github.com/mikebrady/shairport-sync.git
    

4. Now that we have cloned the Shairport-Sync repository to our Raspberry Pi we can now build and install the Shairport software.

Before we get started, we must first move into the shairport-sync folder and configure the system. To do this, we must run a few commands on our Raspberry Pi.
    
    
    cd shairport-sync
    autoreconf -i -f
    ./configure --with-alsa --with-avahi --with-ssl=openssl --with-systemd --with-metadata
    

The autoreconf command setups the basic config file. The configure command further sets up the build system, telling it to utilize the ALSA audio backend, the Avahi network and set it to use OpenSSL for encryption.

5. With the configuration process now completed we can finally compile Shairport-sync and install it. We can run the two make commands below on our Raspberry Pi to compile and install Shairport-Sync to the device. This process will set up numerous things including the autostart script.
    
    
    make
    sudo make install

6. To enable the Shairport Sync software to start automatically at system startup you need to enter the following command into the terminal on the Raspberry Pi.
    
    
    sudo systemctl enable shairport-sync

7. Finally, we can start up the Shairport software immediately by running the command below on our Raspberry Pi.
    
    
    sudo service shairport-sync start

You should now be able to play audio files through your Raspberry Pi AirPlay Receiver using any AirPlay-capable device. If you are using a non-apple device such as an Android device, then there are few apps that allow you to utilize Airplay.

On your AirPlay-enabled device your Raspberry Pi AirPlay receiver should appear as RaspberryPi in the devices list, please note that this name will be the same as your devices hostname. If you would like to know how to change your Raspberry Pi’s hostname, you can check out our [raspi-config guide](https://pimylifeup.com/raspi-config-tool/).

##  Improving the Analogue Audio output

With our Raspberry Pi AirPlay receiver now setup. There are several different things we can do to improve it. The first of these is to change the Raspberry Pi so it will utilize a newer version of the audio driver.

To run this improved audio driver and get the benefits of it fully then there are a few changes we will have to make. If you would like to read about the audio driver, you check out this topic on it on the [Raspberry Pi forums](https://www.raspberrypi.org/forums/viewtopic.php?t=136445).

1. Firstly we need to update the Raspberry Pi’s firmware, and we can do this by running the following command, it can take some time. Make sure your Raspberry Pi doesn’t lose power during this.
    
    
    sudo rpi-update

2. Once the firmware update has completed, turn off your Raspberry Pi and take out your SD Card. Once you have removed your SD Card, insert the SD Card into a reader connected to a computer. The reason for this is that we need to modify the Raspberry Pi’s boot config file

The file we are after is located at /boot/config.txt on the SD Card, open it up with your favorite text editor. Add the following new line to this file.
    
    
    audio_pwm_mode=2

Once you have edited this file, you can save it and place the SD Card back into your Raspberry Pi and power it back on.

3. With your Raspberry Pi powered back on, there are two more things we need to do before the improved analog audio driver works well with Shairport. The next step is to set it, so the analog jack is the main audio out and not the HDMI output.

We can utilize the following command in the Raspberry Pi’s terminal to do this.
    
    
    amixer cset numid=3 1

4. Now there is one final thing we must do to finish improving our Raspberry Pi AirPlay device, and that is to modify the volume db Range that Shairport uses. We can modify the range by changing it in the configuration file.

Run the following command to begin editing the configuration file.
    
    
    sudo nano /usr/local/etc/shairport-sync.conf

5. Within this file make the following changes.

Find
    
    
    //      volume_range_db = 60 ;

Replace with
    
    
            volume_range_db = 30;

We can now save the file by pressing Ctrl + X then pressing Y and then Enter.

6. Now to make sure all these changes are properly loaded in, we will restart the Raspberry Pi by running the following command.
    
    
    sudo reboot

##  Improving your Raspberry Pi AirPlay Receivers Wi-Fi Performance

1. To improve the Wi-Fi performance of your AirPlay device, you will want to disable the Raspberry Pi’s WLAN adaptor power management. This reason for this is that it can prevent Shairport from being visible on your list of Airplay devices due to it powering down the Wi-Fi adaptor.

Luckily it is easy to stop the Raspberry Pi from doing this with most adaptors. The way to do this is by modifying the network interfaces file. We can open the file by using the following command in terminal.
    
    
    sudo nano /etc/network/interfaces

2. Within this file, we need to locate and add the following text to the interfaces file. This edit will tell the Raspberry Pi not to manage its wireless power and will not turn it off to save power.

If you have upgraded to Raspbian Stretch then wlan0 may be called something different. If you’re unsure which one is the correct one to use, then use the `ifconfig` command to see what the new name is.

Find
    
    
    iface wlan0 inet manual

Add Below
    
    
            wireless-power off

We can now save the file by pressing Ctrl + X then pressing Y and then Enter.

3. Now to make sure all these changes are properly loaded in, we will restart the Raspberry Pi by running the following command.
    
    
    sudo reboot

You should now hopefully have a fully working Raspberry Pi AirPlay receiver. If you have any issues or feedback, then feel free to drop us a comment over at our forums. If you enjoyed this tutorial, then be sure to check out our [other projects](https://pimylifeup.com/category/projects/).

