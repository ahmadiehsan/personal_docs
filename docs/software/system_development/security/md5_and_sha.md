# MD5 & SHA

## Description

|                 | MD5                                             | SHA-1                               | SHA-2                                                             | SHA-3                        |
|-----------------|-------------------------------------------------|-------------------------------------|-------------------------------------------------------------------|------------------------------|
| Release Year    | 1992                                            | 1995                                | 2002                                                              | 2008                         |
| Output Length   | 128 bit                                         | 160 bit                             | 256/512 bit                                                       | 224/256/384/512 bit          |
| Hash Collisions | Frequent                                        | Frequent                            | Rare                                                              | Rare                         |
| Security Level  | Low, has been successfully attacked             | Low, has been successfully attacked | High                                                              | High                         |
| Applications    | Abandoned, still used for data integrity checks | Abandoned                           | Cryptocurrency transaction verification, digital signatures, etc. | Can be used to replace SHA-2 |

- **MD5** and **SHA-1** have been successfully attacked multiple times and are thus abandoned in various security applications.
- **SHA-2** series, especially SHA-256, is one of the most secure hash algorithms to date, with no successful attacks reported, hence commonly used in various security applications and protocols.
- **SHA-3** has lower implementation costs and higher computational efficiency compared to SHA-2, but its current usage coverage is not as extensive as the SHA-2 series.
