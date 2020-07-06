# We chall


<!-- vim-markdown-toc GFM -->

* [Training: Get Sourced](#training-get-sourced)
* [Training: Stegano 1](#training-stegano-1)
* [Crypto - Caesar I](#crypto---caesar-i)
* [Training: Crypto - Caesar II](#training-crypto---caesar-ii)
* [Training: MySQL I (MySQL, Exploit, Training)](#training-mysql-i-mysql-exploit-training)
* [PHP My Admin (Research)](#php-my-admin-research)

<!-- vim-markdown-toc -->

## Training: Get Sourced

F12 to view source, finding the password `html_sourcecode`

## Training: Stegano 1

Download the img, `vim stegano1.bmp`
We can see the hint `Look what the hex-edit revealed: passwd: steganoI`
So the answer should be `steganoI`
(By the way, you can also open it via a hex editor, as it goes. Or `cat`, or `strings`)

## Crypto - Caesar I

The key is 6.
The plaintext is "the quick brown fox jumps over the lazy dog of caesar and your unique solution is mimamgffoprm"

## Training: Crypto - Caesar II

Caesar + ascii -> ascii shift cipher

The format of the cipertext is hexadecimal ascii, it should be printed as ascii chars.

All the possible shifts are from 1 to 127. When using the shift of 44 we can get:

Goodtjob,tyoutsolvedtonetmoretchallengetintyourtjourney.tThistonetwastfairlyteasyttotcrack.tWasn'ttit?t128tkeystistatquitetsmalltkeyspace,tsotittshouldn'tthavettakentyouttootlongttotdecrypttthistmessage.tWelltdone,tyourtsolutiontistngrmigeodlpm.

We can find t is between words. So the answer should be `ngrmigeodlpm.`

## Training: MySQL I (MySQL, Exploit, Training)

As the hint goes, login yourself as admin.
Payload is `admin' or '1'='1+--`

## PHP My Admin (Research)

Using Google advanced search, all these words "phpmyadmin wechall.net", still didn't find the phpmyadmin. But found an interesting fact that the provider himself called it "pma".

Searching about: pma wechall.net
We can find `pma.wechall.net`
