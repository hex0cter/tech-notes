
date: None  
author(s): None  

# [修改Windows系统时间同步间隔时间 - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/windows-tips/w32timetimeprovidersntpclient)

<http://r2.mcafeefans.com/?p=234>  


我的主板也不晓得咋的，也许我每天会断开电源后才去睡觉的缘故，每天时间会无缘无故慢5分钟左右，这个是我绝对不允许的，于是要用到windows时间同步，但是这个东西默认的间隔时间太变态了，至少对我来说是如此。因为是604800秒，也就是7天，我日，要慢半小时了。我的要求是，一小时给我校对一次，于是打开注册表路径，将其修改SpecialPollInterval键值为3600。

> [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\TimeProviders\NtpClient]  
  
---

