# CTFlearn

[TOC]

## Forensics

### Pics

#### General skills
1. Use vim to search for flag directly
2. Use `file` to judge the type of the file. 
3. Use binwalk or foremost to extract the files hidden inside.

#### Forensics 101
*easy*

Download the pic at https://mega.nz/#!OHohCbTa!wbg60PARf4u6E6juuvK9-aDRe_bgEL937VO01EImM7c

Open the pic with Vim, `?flag`

#### Binwalk

*easy*

Discription:
Here is a file with another file hidden inside it. Can you extract it? https://mega.nz/#!qbpUTYiK!-deNdQJxsQS8bTSMxeUOtpEclCI-zpK7tbJiKV0tXYY

`binwalk PurpleThing.jpeg`
Find that there are hidden files using binwalk

Extract all the files
`binwalk --extract --dd=".*" PurpleThing.jpeg`

The flag is one of the files hidden inside.

#### WOW.... So Meta
*easy*

Discription:
This photo was taken by our target. See what you can find out about him from it. https://mega.nz/#!ifA2QAwQ!WF-S-MtWHugj8lx1QanGG7V91R-S1ng7dDRSV25iFbk

The flag is hidden in the exif info, but anyway, I prefer to get it using Vim directly.

### Zips or other files

#### General skills
1. Be careful with the hidden files or dirs `.XXX`
2. Track the streams

#### Taking LS

*easy*

Download the zip and unzip it https://mega.nz/#!mCgBjZgB!_FtmAm8s_mpsHr7KWv8GYUzhbThNn0I8cHMBi4fJQp8

There is a "The flag.pdf", which is protected, a password is needed.

`cd` into the dir and `ll`, you can find the hidden dir `.ThePassword/`

`cd .ThePassword/` and `cat ThePassword.txt`
`Nice Job!  The Password is "Im The Flag".`

Then you can use the password to open the pdf and get the flag.

#### A CAPture of a Flag

*easy*

Discription:
This isn't what I had in mind, when I asked someone to capture a flag... can you help? You should check out WireShark. https://mega.nz/#!3WhAWKwR!1T9cw2srN2CeOQWeuCm0ZVXgwk-E2v-TrPsZ4HUQ_f4

Open the pcap-ng capture file via wireshark.
Track the TCP stream and in the stream 5 you can find a strange string in the GET request.
`ZmxhZ3tBRmxhZ0luUENBUH0=`
That's obvious, base64
Decode it and you can get the flag.