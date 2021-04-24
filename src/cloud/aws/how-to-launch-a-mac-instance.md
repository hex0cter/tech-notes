https://medium.com/aws-architech/how-to-run-macos-using-amazon-ec2-mac-instances-cur-d918094f9b65

<div><br>

</div>

<div>

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-size:21px">AWS&nbsp;<a href="https://aws.amazon.com/about-aws/whats-new/2020/11/announcing-amazon-ec2-mac-instances-for-macos/" rel="noopener nofollow" style="color:inherit">recently announced</a>&nbsp;that you can now run Mac instances via EC2. The Mac instances are listed under a new instance family called 'm1'. The two macOS versions listed are Catalina and High Sierra. Big Sur is not yet supported.</p>

<h1 style="color:rgb(41,41,41);font-family:sohne,Helvetica Neue,Helvetica,Arial,sans-serif;line-height:36px;font-weight:500;font-size:30px">How to launch a macOS EC2 instance</h1>

<h2 style="color:rgb(41,41,41);font-family:sohne,Helvetica Neue,Helvetica,Arial,sans-serif;font-weight:500;line-height:28px;font-size:22px">AWS Console: Make sure you are in a supported region</h2>

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-size:21px">Currently macOS on EC2 is only available in these regions: US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), and Asia-Pacific (Singapore). Make sure you're in one of these regions before you carry on with the next steps.</p>

<h2 style="color:rgb(41,41,41);font-family:sohne,Helvetica Neue,Helvetica,Arial,sans-serif;font-weight:500;line-height:28px;font-size:22px">AWS Console: Allocate a dedicated host</h2>

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-size:21px">Firstly, because the macOS EC2 instance will be running on actual Mac Minis and not on a virtual machines, you require a dedicated host.</p>

<ol style="margin:0px;padding:0px;list-style:none none;color:rgba(0,0,0,0.8);font-family:medium-content-sans-serif-font,-apple-system,system-ui,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;font-size:medium"><li style="color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;list-style-type:decimal;margin-left:30px;padding-left:0px;font-size:21px;margin-top:2em">Go to the EC2 Console.</li>

<li style="color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;list-style-type:decimal;margin-left:30px;padding-left:0px;font-size:21px;margin-top:1.05em">Under 'Instances', click on 'Dedicated Hosts'.</li>

<li style="color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;list-style-type:decimal;margin-left:30px;padding-left:0px;font-size:21px;margin-top:1.05em">Click on the 'Allocate Dedicated Hosts' button (it's the orange one).</li>

<li style="color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;list-style-type:decimal;margin-left:30px;padding-left:0px;font-size:21px;margin-top:1.05em">For the Dedicated Host settings page, input/select the following:</li>

</ol>

<blockquote style="box-shadow:rgb(41,41,41) 3px 0px 0px 0px inset;padding-left:23px;color:rgba(0,0,0,0.8);font-family:medium-content-sans-serif-font,-apple-system,system-ui,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;font-size:medium">

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-style:italic;font-size:21px">name --- whatever you'd like<br>

instance family --- mac1<br>

support multiple instance types --- disable this (it is enabled by default) Instance type --- mac1.metal<br>

availability zone --- any,<br>

Instance auto-placement --- enabled<br>

Host recovery --- disable this.</p>

</blockquote>

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-size:21px">Click 'Allocate'</p>

<h2 style="color:rgb(41,41,41);font-family:sohne,Helvetica Neue,Helvetica,Arial,sans-serif;font-weight:500;line-height:28px;font-size:22px">AWS Console: Launch the instance</h2>

<ol style="margin:0px;padding:0px;list-style:none none;color:rgba(0,0,0,0.8);font-family:medium-content-sans-serif-font,-apple-system,system-ui,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;font-size:medium"><li style="color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;list-style-type:decimal;margin-left:30px;padding-left:0px;font-size:21px;margin-top:0.86em">Go to the EC2 console.</li>

<li style="color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;list-style-type:decimal;margin-left:30px;padding-left:0px;font-size:21px;margin-top:1.05em">Click 'Launch Instance'</li>

<li style="color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;list-style-type:decimal;margin-left:30px;padding-left:0px;font-size:21px;margin-top:1.05em">Select 'macOS Catalina 10.15.7'</li>

<li style="color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;list-style-type:decimal;margin-left:30px;padding-left:0px;font-size:21px;margin-top:1.05em">Click 'Review and Launch'</li>

<li style="color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;list-style-type:decimal;margin-left:30px;padding-left:0px;font-size:21px;margin-top:1.05em">Use an existing key or create a new one. You'll need the key for later.</li>

</ol>

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-size:21px">If that failed, go to 'Edit Instance Details' and select manually the host that you created. Somehow the 'auto-placement' did not work for me.</p>

<h2 style="color:rgb(41,41,41);font-family:sohne,Helvetica Neue,Helvetica,Arial,sans-serif;font-weight:500;line-height:28px;font-size:22px">Connect via VNC</h2>

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-size:21px">So how can you connect to your macOS remotely? For that, you can use the VNC protocol.</p>

<ol style="margin:0px;padding:0px;list-style:none none;color:rgba(0,0,0,0.8);font-family:medium-content-sans-serif-font,-apple-system,system-ui,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;font-size:medium"><li style="color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;list-style-type:decimal;margin-left:30px;padding-left:0px;font-size:21px;margin-top:2em">AWS Console: Update the security group your mac instance is in to allow port 5900 but make sure to only allow your own IP address as it's insecure.</li>

<li style="color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;list-style-type:decimal;margin-left:30px;padding-left:0px;font-size:21px;margin-top:1.05em">SSH into the instance using the key from before. command:&nbsp;<em>ssh -i &lt;your private key.pem&gt; ec2-user@&lt;your public ip address&gt;</em></li>

<li style="color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;list-style-type:decimal;margin-left:30px;padding-left:0px;font-size:21px;margin-top:1.05em">In the EC2 Mac instance: Start up the VNC server on your mac. Refer to the commands&nbsp;<a href="https://gist.githubusercontent.com/nateware/3915757/raw/25d15f732cbf0038a75ebb6ab68d1d234c0e118b/gistfile1.txt" rel="noopener nofollow" style="color:inherit">here</a>, but note that the change password line does not work. For that, use the below:</li>

</ol>

<blockquote style="box-shadow:rgb(41,41,41) 3px 0px 0px 0px inset;padding-left:23px;color:rgba(0,0,0,0.8);font-family:medium-content-sans-serif-font,-apple-system,system-ui,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;font-size:medium">

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-style:italic;font-size:21px">echo "passwordhere" | perl -we 'BEGIN {&nbsp;<a href="http://twitter.com/k" rel="noopener nofollow" style="color:inherit">@k</a>&nbsp;= unpack "C*", pack "H*", "1734516E8BA8C5E2FF1C39567390ADCA"}; $_ = &lt;&gt;; chomp; s/^(.{8}).*/$1/;&nbsp;<a href="http://twitter.com/p" rel="noopener nofollow" style="color:inherit">@p</a>&nbsp;= unpack "C*", $_; foreach (<a href="http://twitter.com/k" rel="noopener nofollow" style="color:inherit">@k</a>) { printf "%02X", $_ ^ (shift&nbsp;<a href="http://twitter.com/p" rel="noopener nofollow" style="color:inherit">@p</a>&nbsp;|| 0) }; print "\n"' | sudo tee /Library/Preferences/com.apple.VNCSettings.txt</p>

</blockquote>

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-size:21px">Make sure to replace&nbsp;<em>passwordhere</em>&nbsp;with the actual password.</p>

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-size:21px">4. Download your VNC client on your local machine.</p>

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-size:21px">5. On the EC2 console, copy the IP address of our macOS ec2 instance.</p>

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-size:21px">6. Connect to your macOS ec2 instance via the VNC client. Use the obtained IP address from step 5 and the password you've set from step 2.</p>

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-size:21px">You should now be able to view your mac's login screen:</p>

<div style="width:680px">

<div style="margin-left:auto;margin-right:auto;max-width:1308px">

<div style="margin:auto;background-color:rgb(242,242,242)">

<div style="padding-bottom:503.234px;height:0px">

<div style="width:680px;overflow:hidden;height:503.234px"><img alt="Image for post" height="968" src="https://miro.medium.com/max/60/1*zKg7sbWLOvn_BjiN4OiHGA.png?q=20" style="vertical-align:middle;width:680px;height:503.234px" width="1308"></div>

<img alt="Image for post" height="968" src="https://miro.medium.com/max/2616/1*zKg7sbWLOvn_BjiN4OiHGA.png" style="vertical-align:middle;background-color:rgb(255,255,255);width:680px;height:503.234px" width="1308"></div>

</div>

</div>

</div>

<h2 style="color:rgb(41,41,41);font-family:sohne,Helvetica Neue,Helvetica,Arial,sans-serif;font-weight:500;line-height:28px;font-size:22px">Logging into your macOS instance</h2>

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-size:21px">Ok so you can connect via VNC, but where's the password for ec2-user?</p>

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-size:21px">For this, go back to your ssh session, and run the following to create a password for ec2-user:</p>

<blockquote style="box-shadow:rgb(41,41,41) 3px 0px 0px 0px inset;padding-left:23px;color:rgba(0,0,0,0.8);font-family:medium-content-sans-serif-font,-apple-system,system-ui,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;font-size:medium">

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-style:italic;font-size:21px">sudo passwd ec2-user</p>

</blockquote>

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-size:21px">You should be able to use that password to login in your VNC session to your Mac instance.</p>

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-size:21px">Let me know if that was useful! And if you have requests for other tutorials.</p>

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-size:21px">***</p>

<h2 style="color:rgb(41,41,41);font-family:sohne,Helvetica Neue,Helvetica,Arial,sans-serif;font-weight:500;line-height:28px;font-size:22px">Potential error messages</h2>

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-size:21px">Below is a list of possible error messages that you may encounter. These can all happen when you try to allocate a dedicated host.</p>

<blockquote style="box-shadow:rgb(41,41,41) 3px 0px 0px 0px inset;padding-left:23px;color:rgba(0,0,0,0.8);font-family:medium-content-sans-serif-font,-apple-system,system-ui,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;font-size:medium">

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-style:italic;font-size:21px">The requested configuration is currently not supported. Please check the documentation for supported configurations.</p>

</blockquote>

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-size:21px">I am currently in touch with someone in AWS in order to clarify on the correct configurations. I will update this story once I receive the clarification. UPDATE: the AWS contact has confirmed that this error pops up when there is a capacity issue. That means the selected AZ does not yet have a Mac dedicated host in it or it has run out.</p>

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-size:21px">Other errors:</p>

<blockquote style="box-shadow:rgb(41,41,41) 3px 0px 0px 0px inset;padding-left:23px;color:rgba(0,0,0,0.8);font-family:medium-content-sans-serif-font,-apple-system,system-ui,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;font-size:medium">

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-style:italic;font-size:21px">"m1 instance family is not supported"</p>

</blockquote>

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-size:21px">This is when you leave 'Support multiple instance types' enabled.</p>

<blockquote style="box-shadow:rgb(41,41,41) 3px 0px 0px 0px inset;padding-left:23px;color:rgba(0,0,0,0.8);font-family:medium-content-sans-serif-font,-apple-system,system-ui,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;font-size:medium">

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-style:italic;font-size:21px">Insufficient capacity.</p>

</blockquote>

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-size:21px">This is when you disable 'support multiple instance types' and select exactly 'mac1.metal'. I am guessing that AWS has run out of Mac Minis to support any more Mac instances. I will confirm this and update this post.</p>

<blockquote style="box-shadow:rgb(41,41,41) 3px 0px 0px 0px inset;padding-left:23px;color:rgba(0,0,0,0.8);font-family:medium-content-sans-serif-font,-apple-system,system-ui,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;font-size:medium">

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-style:italic;font-size:21px">Instance type 'mac1.metal' does not support host recovery.</p>

</blockquote>

<p style="word-break:break-word;color:rgb(41,41,41);line-height:32px;letter-spacing:-0.003em;font-family:charter,Georgia,Cambria,Times New Roman,Times,serif;font-size:21px">This is when you enable 'host recovery'. Disable it.</p>

</div>

<div><br>

</div>

<div><br>

</div>

<div><br>

</div>

<div><br>

</div>

<div><br>

</div>

<div><br>

</div>

<div><br>

</div>

<div><br>

</div>

<div><br>

</div>
