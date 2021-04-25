# [Gmail for Nokia E72](http://mail.google.com/support/bin/answer.py?answer=78799)

Now getting your **email** from gmail into your nokia E72: Here **Nokia is at fault, and a serious deficiency.** I went to email setup in the menu's and started the wizard to create a new account. It seemed to have preconfigured setups for common email providers like gmail, yahoo etc. I started the gmail set up wizard, keyed in my username and password, then waited 5 seconds, and the screen went back to the previous one. This kept repeating, every time I tried. Tried everything: checked internet connectivity (wifi), closed all other apps including the MFE I had set up earlier, switched off and on the phone, everything short of standing on my head. So what works? How do you set up a personal gmail account on your nokia e72? go here:

<http://www.techniqx.com/2010/02/workaround-for-configuring-gmail.html>

(I paste that text here in case that page is removed:

> The email software in Nokia E72 still has lots of bugs. To configure your Gmail account, it’s not as easy as selecting Gmail and entering the credentials. That simply won’t work as there is a bug. Instead, workaround is to select “Other” and enter a false id like [asa@dss.com](mailto:asa@dss.com), this will take you to the next page to select the type. Select “POP/IMAP”. Now, you will get an option to enter your credentials and modify advanced settings. Here change your email id back to [xxx@gmail.com](mailto:xxx@gmail.com) and enter the credentials as mentioned here> (the gmail site for imap manual setup):

And you have gmail set up. Quite inelegant process of setting up gmail on this nokia phone, I would say.

您可以使用以下信息为许多邮件客户端配置 IMAP。如果您遇到问题，建议您与邮件客户端的客户支持部门联系，以获得进一步的说明 - 我们无法对未在[此处](http://mail.google.com/support/bin/answer.py?answer=75726)列出的邮件客户端的配置问题提供帮助。

|  **接收邮件 (IMAP) 服务器 - 需要 SSL：**|  imap.gmail.com **使用 SSL** ：是 **端口** ： 993
---|---
 **外发邮件 (SMTP) 服务器 - 需要 TLS：**|  smtp.gmail.com（使用身份验证）<br> **使用身份验证** ：是 <br> **使用 STARTTLS** ：是（某些客户端称其为 SSL）<br> **端口** ： **587**
 **帐户名称：**|  您的 Gmail 用户名（包括 @gmail.com）
 **电子邮件地址：**|  您的完整 Gmail 电子邮件地址（用户名@gmail.com）
 **密码：**|  您的 Gmail 密码

请注意，如果您的客户端不支持 SMTP 身份验证，您将无法通过客户端用 Gmail 地址发送电子邮件。
