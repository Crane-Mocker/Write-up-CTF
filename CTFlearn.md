# CTFlearn

[TOC]

## Forensics

### Pics

#### General skills
1. Use vim to search for flag directly
2. Use `file` to judge the type of the file. 
3. Use binwalk or foremost to extract the files hidden inside.
4. Be careful with the hidden files or dirs `.XXX

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

#### 07601
*easy*

Discription:
https://mega.nz/#!CXYXBQAK!6eLJSXvAfGnemqWpNbLQtOHBvtkCzA7-zycVjhHPYQQ I think I lost my flag in there. Hopefully, it won't get attacked...

First, `file AGT.png`
`AGT.png: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 300x168, frames 3`
We can find that it's actually jpeg, so change the name into .jpeg

But then we find nothing useful about the jpeg only. So let's use binwalk to check if there are hidden files.
Yes, ofc, there are hidden file. 
Extract them all `binwalk --extract --dd=".*" AGT.jpeg`

Then we find the strange dir like this `_AGT.jpeg.extracted/Secret Stuff.../Don't Open This...`

We can find a jpeg here, but fail to open it directly. Check its format `file I\ Warned\ You.jpeg`
`I Warned You.jpeg: data`

So it's clear that we can try to find out the strings hidden in the jpeg, which is actually in the format of data.
`strings I\ Warned\ You.jpeg >> string.txt`

`vim string.txt`
`?CTF`
And you can get the flag.

#### Up For A Little Challenge?

*Medium*

Discription:
https://mega.nz/#!LoABFK5K!0sEKbsU3sBUG8zWxpBfD1bQx_JY_MuYEWQvLrFIqWZ0
You Know What To Do ...

`binwalk Begin\ Hack.jpg` and we can find the hidden file. Extract as we always do.
` binwalk --extract --dd=".*" Begin\ Hack.jpg`

Then we got `0` and `1E`, the two files.
Open `0`, it's a pic. Use vim to find the flag.`?flag`
We only get `flag{Not_So_Simple...}`

So let's check `iE`
`file 1E` We can find the format`TIFF image data`, but we can't open it.
It's a natural idea that we can try to find out the strings in the file.
`strings 1E >> string.txt`
And open the txt, we can find a URL!`https://mega.nz/#!z8hACJbb!vQB569ptyQjNEoxIwHrUhwWu5WCj1JWmU-OFjf90Prg`

Open the URL and download the zip it offers.
`unzip` the compressed package and `cd Did\ I\ Forget\ Again\?/`
`ll` to find that there are two files in the dir.
`'Loo Nothing Becomes Useless ack.jpg'` and `.Processing.cerb4`

This `.cerb4` is a little strange. I have never seen this format before. Let's check it.
`file .Processing.cerb4`
`.Processing.cerb4: Zip archive data, at least v2.0 to extract`

It's clear now we should unzip it.
`uzip .Processing.cerb4` but password is needed.
So we can check the jpg to find if the password is hidden somewhere.

Unfortunately we can find nothing to do with password. So maybe we should get back to the first pic to see if there is a password there.
`vim 'Begin Hack.jpg'` and `?pass`
Yes, we can find a password.
`password: Really? Again?` We can try it, but it isn't the real one. Do it again!
`?key` Here we go! 
`Mp_real_unlock_key: Nothing Is As It Seems` It works.

Now we get a `skycoder.jpg`. We open it and find the flag at the bottom of the pic.
(The string is not clear actually, I use stegsolve to XOR, and it's fine)

### Zips or other files

#### General skills
1. Be careful with the hidden files or dirs `.XXX`
2. Track the streams
3. Pay atten to Git

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

#### Git Is Good
*medium*

Discription:
The flag used to be there. But then I redacted it. Good Luck. https://mega.nz/#!3CwDFZpJ!Jjr55hfJQJ5-jspnyrnVtqBkMHGJrd6Nn_QqM7iXEuc

`cd` into the dir, you can find `.git/` and `cat flag.txt`, you can only find
`flag{REDACTED}`

As the hint goes, we should use git to help get the former version of flag.txt.(Git is a version control system, as we all know.)
`git log` to see the versions.
According to the messages, we could find the second version should be the one we want.

`git reset --hard {commit id}` could help.
By the way, you can also use `HEAD^` to reset the last version. Because HEAD means the version now, ^ means one version before it.(HEAD^^ is the one before the former one.)

Then you can `cat flag.txt` and get the flag.