
# [SIP Timers](http://publib.boulder.ibm.com/infocenter/wasinfo/v6r1/index.jsp?topic=/com.ibm.websphere.base.doc/info/aes/ae/rsip_reftimesumm.html)

Request for Comments (RFC) 3261, "SIP: Session Initiation Protocol," specifies various timers that SIP uses.

[Summary of SIP timers](http://publib.boulder.ibm.com/infocenter/wasinfo/v6r1/topic/com.ibm.websphere.base.doc/info/aes/ae/rsip_reftimesumm.html#rsip_reftimesumm__table_timers) summarizes for each SIP timer the default value, the section of [RFC 3261](http://www.ietf.org/rfc/rfc3261.txt) that describes the timer, and the meaning of the timer.

Table 1. Summary of SIP timers

Timer| Default value| Section| Meaning
---|---|---|---
T1| 500 ms| 17.1.1.1| Round-trip time (RTT) estimate
T2| 4 sec.| 17.1.2.2| Maximum retransmission interval for non-INVITE requests and INVITE responses
T4| 5 sec.| 17.1.2.2| Maximum duration that a message can remain in the network
Timer A| initially T1| 17.1.1.2| INVITE request retransmission interval, for UDP only
Timer B| 64*T1| 17.1.1.2| INVITE transaction timeout timer
Timer D| > 32 sec. for UDP| 17.1.1.2| Wait time for response retransmissions
0 sec. for TCP and SCTP
Timer E| initially T1| 17.1.2.2| Non-INVITE request retransmission interval, UDP only
Timer F| 64*T1| 17.1.2.2| Non-INVITE transaction timeout timer
Timer G| initially T1| 17.2.1| INVITE response retransmission interval
Timer H| 64*T1| 17.2.1| Wait time for ACK receipt
Timer I| T4 for UDP| 17.2.1| Wait time for ACK retransmissions
0 sec. for TCP and SCTP
Timer J| 64*T1 for UDP| 17.2.2| Wait time for retransmissions of non-INVITE requests
0 sec. for TCP and SCTP
Timer K| T4 for UDP| 17.1.2.2| Wait time for response retransmissions
0 sec. for TCP and SCTP




<>
