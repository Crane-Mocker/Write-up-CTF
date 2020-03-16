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

## Cryptography 

### Character Encoding

*easy*

Discription:
In the computing industry, standards are established to facilitate information interchanges among American coders. Unfortunately, I've made communication a little bit more difficult. Can you figure this one out? 41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D

Hex to ascii.

### Hextroadinary

*easy*

Discription:
Meet ROXy, a coder obsessed with being exclusively the worlds best hacker. She specializes in short cryptic hard to decipher secret codes. The below hex values for example, she did something with them to generate a secret code, can you figure out what? Your answer should start with 0x.
`0xc4115 0x4cf8`

ROXy means xor. So let's calculate xor and we can get `c0ded`
So `0xc0ded` is the flag.

### Base 2 2 the 6

*easy*

Discription:
There are so many different ways of encoding and decoding information nowadays... One of them will work! Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9

As the hint goes, just base64

### BruXOR

*easy*

Discription:
There is a technique called bruteforce. Message: q{vpln'bH_varHuebcrqxetrHOXEj No key! Just brute .. brute .. brute ... :D

As you can see, no key, just brute and xor. But before that we have to turn the string into hex at first.

Then `xortool -x -b xor.hex`
And `cat xx.out` one by one you can find the flag.

### Reverse Polarity

*easy*

Discription:
I got a new hard drive just to hold my flag, but I'm afraid that it rotted. What do I do? The only thing I could get off of it was this: 01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101

Binary to ascii.

### Vigenere Cipher

*easy*

Discription:
The vignere cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers based on the letters of a keyword.
I’m not sure what this means, but it was left lying around: blorpy
gwox{RgqssihYspOntqpxs}

vigenere cipher, the key is blorpy, and the ciphertext is gwox{RgqssihYspOntqpxs}

### Morse Code

*easy*

..-. .-.. .- --. ... .- -- ..- . .-.. -- --- .-. ... . .. ... -.-. --- --- .-.. -... -.-- - .... . .-- .- -.-- .. .-.. .. -.- . -.-. .... . . ...

Just Morse code, I recommand this [website](https://www.jb51.net/tools/morse.htm).

### HyperStream Test #2

*easy*

Discription:
I love the smell of bacon in the morning! ABAAAABABAABBABBAABBAABAAAAAABAAAAAAAABAABBABABBAAAAABBABBABABBAABAABABABBAABBABBAABB

As the hint goes, Bacon's chiper.

## Web

### Basic Injection
*easy*

Discription:
See if you can leak the whole database. The flag is in there somwhere… https://web.ctflearn.com/web4/

When we open the url, we can see "You know what to do" as the headline. Press "F12" to check the code. Then we can see the hint
`<!-- Try some names like Hiroki, Noah, Luke -->`

So let's try `Luke`. And we find that we need to inject.
So an easy payload is `Luke' or '1'='1`
And you can find the flag.

## Binary

### Lazy Game Challenge

*easy*

Discription:
I found an interesting game made by some guy named "John_123". It is some betting game. I made some small fixes to the game; see if you can still pwn this and steal $1000000 from me!

To get flag, pwn the server at `nc thekidofarcrania.com 10001`

The key point is that it's hard to win, so when you place a bet, input a negative number (for example: -1000000000) and then you can loose the game as you like it. Each time you loose a game, you gain some money. And when the game ends, you will get the flag.