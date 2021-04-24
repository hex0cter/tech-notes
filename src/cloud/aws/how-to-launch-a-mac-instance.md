
date: 2020-12-08 08:43:50.040000
author(s): Nazreen Mohamad

# [How to run macOS using Amazon EC2 Mac instances](https://medium.com/aws-architech/how-to-run-macos-using-amazon-ec2-mac-instances-cur-d918094f9b65)

![](https://miro.medium.com/max/2616/1*zKg7sbWLOvn_BjiN4OiHGA.png)

AWS [recently announced](https://aws.amazon.com/about-aws/whats-new/2020/11/announcing-amazon-ec2-mac-instances-for-macos/) that you can now run Mac instances via EC2. The Mac instances are listed under a new instance family called ‘m1’. The two macOS versions listed are Catalina and High Sierra. Big Sur is not yet supported.

## AWS Console: Make sure you are in a supported region

Currently macOS on EC2 is only available in these regions: US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), and Asia-Pacific (Singapore). Make sure you’re in one of these regions before you carry on with the next steps.

## AWS Console: Allocate a dedicated host

Firstly, because the macOS EC2 instance will be running on actual Mac Minis and not on a virtual machines, you require a dedicated host.

  1. Go to the EC2 Console.
  2. Under ‘Instances’, click on ‘Dedicated Hosts’.
  3. Click on the ‘Allocate Dedicated Hosts’ button (it’s the orange one).
  4. For the Dedicated Host settings page, input/select the following:



> name — whatever you’d like
> instance family — mac1
> support multiple instance types — disable this (it is enabled by default) Instance type — mac1.metal
> availability zone — any,
> Instance auto-placement — enabled
> Host recovery — disable this.

Click ‘Allocate’

## AWS Console: Launch the instance

  1. Go to the EC2 console.
  2. Click ‘Launch Instance’
  3. Select ‘macOS Catalina 10.15.7’
  4. Click ‘Review and Launch’
  5. Use an existing key or create a new one. You’ll need the key for later.



If that failed, go to ‘Edit Instance Details’ and select manually the host that you created. Somehow the ‘auto-placement’ did not work for me.

## Connect via VNC

So how can you connect to your macOS remotely? For that, you can use the VNC protocol.

  1. AWS Console: Update the security group your mac instance is in to allow port 5900 but make sure to only allow your own IP address as it’s insecure.
  2. SSH into the instance using the key from before. command: _ssh -i <your private key.pem> ec2-user@<your public ip address>_
  3. In the EC2 Mac instance: Start up the VNC server on your mac. Refer to the commands [here](https://gist.githubusercontent.com/nateware/3915757/raw/25d15f732cbf0038a75ebb6ab68d1d234c0e118b/gistfile1.txt), but note that the change password line does not work. For that, use the below:



> echo “passwordhere” | perl -we ‘BEGIN { [@k](http://twitter.com/k) = unpack “C*”, pack “H*”, “1734516E8BA8C5E2FF1C39567390ADCA”}; $_ = <>; chomp; s/^(.{8}).*/$1/; [@p](http://twitter.com/p) = unpack “C*”, $_; foreach ([@k](http://twitter.com/k)) { printf “%02X”, $_ ^ (shift [@p](http://twitter.com/p) || 0) }; print “\n”’ | sudo tee /Library/Preferences/com.apple.VNCSettings.txt

Make sure to replace _passwordhere_ with the actual password.

4\. Download your VNC client on your local machine.

5\. On the EC2 console, copy the IP address of our macOS ec2 instance.

6\. Connect to your macOS ec2 instance via the VNC client. Use the obtained IP address from step 5 and the password you’ve set from step 2.

You should now be able to view your mac’s login screen:

![](https://miro.medium.com/max/2616/1*zKg7sbWLOvn_BjiN4OiHGA.png)

## Logging into your macOS instance

Ok so you can connect via VNC, but where’s the password for ec2-user?

For this, go back to your ssh session, and run the following to create a password for ec2-user:

> sudo passwd ec2-user

You should be able to use that password to login in your VNC session to your Mac instance.

Let me know if that was useful! And if you have requests for other tutorials.

***

## Potential error messages

Below is a list of possible error messages that you may encounter. These can all happen when you try to allocate a dedicated host.

> The requested configuration is currently not supported. Please check the documentation for supported configurations.

I am currently in touch with someone in AWS in order to clarify on the correct configurations. I will update this story once I receive the clarification. UPDATE: the AWS contact has confirmed that this error pops up when there is a capacity issue. That means the selected AZ does not yet have a Mac dedicated host in it or it has run out.

Other errors:

> “m1 instance family is not supported”

This is when you leave ‘Support multiple instance types’ enabled.

> Insufficient capacity.

This is when you disable ‘support multiple instance types’ and select exactly ‘mac1.metal’. I am guessing that AWS has run out of Mac Minis to support any more Mac instances. I will confirm this and update this post.

> Instance type ‘mac1.metal’ does not support host recovery.

This is when you enable ‘host recovery’. Disable it.
