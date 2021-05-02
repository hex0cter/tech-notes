# [wireshark won't display any network interface on Linux](http://www.wireshark.org/faq.html#q9.2)

Replace command from wireshark to gksu wireshark which will run with the root privileges.

Refer to the following for details.

<http://www.wireshark.org/faq.html#q9.2>


Q 9.1: I'm running Wireshark on a UNIX-flavored OS; why does some network interface on my machine not show up in the list of interfaces in the "Interface:" field in the dialog box popped up by "Capture->Start", and/or why does Wireshark give me an error if I try to capture on that interface?

A: You may need to run Wireshark from an account with sufficient privileges to capture packets, such as the super-user account, or may need to give your account sufficient privileges to capture packets. Only those interfaces that Wireshark can open for capturing show up in that list; if you don't have sufficient privileges to capture on any interfaces, no interfaces will show up in the list. See the Wireshark Wiki item on capture privileges for details on how to give a particular account or account group capture privileges on platforms where that can be done.

If you are running Wireshark from an account with sufficient privileges, then note that Wireshark relies on the libpcap library, and on the facilities that come with the OS on which it's running in order to do captures. On some OSes, those facilities aren't present by default; see the Wireshark Wiki item on adding capture support for details.

And, even if you're running with an account that has sufficient privileges to capture, and capture support is present in your OS, if the OS or the libpcap library don't support capturing on a particular network interface device or particular types of devices, Wireshark won't be able to capture on that device.

On Solaris, note that libpcap 0.6.2 and earlier didn't support Token Ring interfaces; the current version, 0.7.2, does support Token Ring, and the current version of Wireshark works with libpcap 0.7.2 and later.

If an interface doesn't show up in the list of interfaces in the "Interface:" field, and you know the name of the interface, try entering that name in the "Interface:" field and capturing on that device.

If the attempt to capture on it succeeds, the interface is somehow not being reported by the mechanism Wireshark uses to get a list of interfaces; please report this to wireshark-dev@wireshark.org giving full details of the problem, including

the operating system you're using, and the version of that operating system (for Linux, give both the version number of the kernel and the name and version number of the distribution you're using);

the type of network device you're using.

If you are having trouble capturing on a particular network interface, and you've made sure that (on platforms that require it) you've arranged that packet capture support is present, as per the above, first try capturing on that device with tcpdump.

If you can capture on the interface with tcpdump, send mail to wireshark-users@wireshark.org giving full details of the problem, including

the operating system you're using, and the version of that operating system (for Linux, give both the version number of the kernel and the name and version number of the distribution you're using);

the type of network device you're using;

the error message you get from Wireshark.

If you cannot capture on the interface with tcpdump, this is almost certainly a problem with one or more of:

the operating system you're using;

the device driver for the interface you're using;

the libpcap library;

so you should report the problem to the company or organization that produces the OS (in the case of a Linux distribution, report the problem to whoever produces the distribution).

You may also want to ask the wireshark-users@wireshark.org and the tcpdump-workers@lists.tcpdump.org mailing lists to see if anybody happens to know about the problem and know a workaround or fix for the problem. In your mail, please give full details of the problem, as described above, and also indicate that the problem occurs with tcpdump not just with Wireshark.

Q 9.2: I'm running Wireshark on a UNIX-flavored OS; why do no network interfaces show up in the list of interfaces in the "Interface:" field in the dialog box popped up by "Capture->Start"?

A: This is really the same question as the previous one; see the response to that question.
