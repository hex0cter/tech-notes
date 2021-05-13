# Page Addressing

_Why Linux use multiple-level addressing to access a particular page?_

Intel CPU use memory page of size 4K(212) Bytes. Therefore the offset of each table entry takes 12 bits. If using direct index(one-level), each process need a mapping table that contains 220 (1M) entries to access all 232 (4G) virtual memories. This waste a lot since process usually takes much less memory than 4G.

When two-level index table is used, only 210 (1K) entries is needed in the table. The second level table is only available when the entry in the first table is valid.
