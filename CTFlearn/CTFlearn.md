# CTFlearn


<!-- vim-markdown-toc GFM -->

* [Forensics](#forensics)
	* [Pics](#pics)
		* [General skills](#general-skills)
		* [Forensics 101](#forensics-101)
		* [Binwalk](#binwalk)
		* [WOW.... So Meta](#wow-so-meta)
		* [07601](#07601)
		* [Up For A Little Challenge?](#up-for-a-little-challenge)
		* [The adventures of Boris Ivanov. Part 1.](#the-adventures-of-boris-ivanov-part-1)
		* [The Keymaker](#the-keymaker)
* [|EOI|0xd9|End of Image|](#eoi0xd9end-of-image)
		* [Exclusive Santa](#exclusive-santa)
		* [MountainMan](#mountainman)
		* [ShahOfGimli](#shahofgimli)
		* [Exif](#exif)
		* [Rubber Duck](#rubber-duck)
		* [Snowboard](#snowboard)
		* [PikesPeak](#pikespeak)
	* [Zips or other files](#zips-or-other-files)
		* [General skills](#general-skills-1)
		* [Taking LS](#taking-ls)
		* [A CAPture of a Flag](#a-capture-of-a-flag)
		* [Git Is Good](#git-is-good)
		* [Milk's Best Friend](#milks-best-friend)
		* [Digital Camouflage](#digital-camouflage)
* [Cryptography](#cryptography)
	* [Character Encoding](#character-encoding)
	* [Hextroadinary](#hextroadinary)
	* [Base 2 2 the 6](#base-2-2-the-6)
	* [BruXOR](#bruxor)
	* [Reverse Polarity](#reverse-polarity)
	* [Vigenere Cipher](#vigenere-cipher)
	* [Morse Code](#morse-code)
	* [HyperStream Test #2](#hyperstream-test-2)
* [Web](#web)
	* [Basic Injection](#basic-injection)
	* [POST Practice](#post-practice)
	* [Prehashbrown](#prehashbrown)
	* [Don't Bump Your Head(er)](#dont-bump-your-header)
	* [Inj3ction Time](#inj3ction-time)
* [Binary](#binary)
	* [Lazy Game Challenge](#lazy-game-challenge)
* [Misc](#misc)
	* [Help Bity](#help-bity)
* [Programming](#programming)
		* [Simple Programming](#simple-programming)

<!-- vim-markdown-toc -->

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

####The adventures of Boris Ivanov. Part 1.

*medium*

Discription:The KGB agent Boris Ivanov got information about an attempt to sell classified data. He quickly reacted and intercepted the correspondence. Help Boris understand what exactly they were trying to sell. Here is the interception data: https://mega.nz/#!HfAHmKQb!zg6EPqfwes1bBDCjx7-ZFR_0O0-GtGg2Mrn56l5LCkE

As we look at the pic, we can find the bar at the bottom, flag must be there. Maybe it's related to offset, I guess.

Try to use stegsolve simply, choose analyse > stereogram solver and you can see the flag att offset 102

#### The Keymaker

*medium*

Discription:Jpeg comments can be very interesting.

----
First, let's see what's jpeg comments.

reference:
https://www.scootersoftware.com/vbulletin/forum/beyond-compare-4-discussion/general/14227-jpeg-exif-comments-vs-jpeg-header-comments

With JPEG images there are two different types of comments that can be edited within the file metadata:
1.EXIF comments
2.JPEG header comments

----

Let's use vim, we can see `CTFlearn{TheKeymakerIsK00l}` , but when we submit it, it isn't the flag.
And `b3BlbnNzbCBlbmMgLWQgLWFlcy0yNTYtY2JjIC1pdiBTT0YwIC1LIFNPUyAtaW4gZmxhZy5lbmMgLW91dCBmbGFnIC1iYXNlNjQKCml2IGRvZXMgbm90IGluY2x1ZGUgdGhlIG1hcmtlciBvciBsZW5ndGggb2YgU09GMAoKa2V5IGRvZXMgbm90IGluY2x1ZGUgdGhlIFMwUyBtYXJrZXIKCg==`
Base64 decode it, we can get

```
openssl enc -d -aes-256-cbc -iv SOF0 -K SOS -in flag.enc -out flag -base64

iv does not include the marker or length of SOF0

key does not include the S0S marker

```

----

A JPEG file is partitioned by markers. Each marker is immediately preceded by an all 1 byte (0xff). Although there are more markers, We will discuss the following markers:

|Marker Name|Marker Identifier|Description|
|---|---|---|
|SOI|0xd8|Start of Image|
|APP0|0xe0|JFIF application segment|
|APPn|0xe1 – 0xef|Other APP segments|
|DQT|0xdb|Quantization Table|
|SOF0|0xc0|Start of Frame|
|DHT|0xc4|Huffman Table|
|SOS|0xda|Start of Scan|
|EOI|0xd9|End of Image|
----

This the progress to decode(-d) flag.enc and get flag.
So, we also need `flag.enc` to decode and get `flag`. But now, we only have the jpeg. 
Let's think about the jpeg comment. `imagemagick` has a command line tool named `identify` to find image metadata.(You can install imagemagick using apt)
`identify -verbose image.png` to check metadata.
We can find `comment: mmtaSHhAsK9pLMepyFDl37UTXQT0CMltZk7+4Kaa1svo5vqb6JuczUqQGFJYiycY`
It's valid for base64, although the result is not ascii.
`echo mmtaSHhAsK9pLMepyFDl37UTXQT0CMltZk7+4Kaa1svo5vqb6JuczUqQGFJYiycY | base64 -d  >> key`

#### Exclusive Santa

There are 1.png and 2.png in the rar.
Use binwalk and there are some other things in the 2 pics.
`binwalk --extract --dd=".*" x.png` to extract them.

For 1.png, there are a png `0` and a ms color profile `36`and some others.
For 2.png, there are 2 png pics, `0` and `CCB6`

Look at `36` and `CCB6`, they look alike. Use stegsolve `analyse>image combiner` and you can see the reflection of the flag.

#### MountainMan

First as the hint goes, we can find two 0xffd9 in the pic.

I first save the other pic which is ended by the first 0xffd9. And use stegsolve to combine them to do XOR, ofc it will fail, because their hex are almost the seem.

Then maybe the flag is in between of the two end markers.

```
88 9F 8D A7 AE AA B9 A5 B0 9E A9 BE A5 BF BE 94 B9 FB A8 A0 FE B6
```

Use cyberchef to brute xor.
First, it's hex, so choose `From Hex`.
Then choose `magic` to brute xor.
There should be 22 chars of flag (22 hex numbers), so the depth choose 22 or more.
The flag should be a string, so the RegEx should be `^\w*{\w*}`.
Then we get the flag.

#### ShahOfGimli

First use binwalk to extract.
Look at the pic `0`, `strings 0 > 0.txt`
There is a flag and some pieces of text look like from base64.

The flag is `CTFlearn{Gimli_Was_Part_Of_The_Fellowship_Of_The_Ring}`. It's not the right flag.

The plaintxt is

```
CTFlearn{Gimli.Is.A.Dwarf}

Who is Gimli?  You can learn more about Gimli here:
https://lotr.fandom.com/wiki/Gimli
https://en.wikipedia.org/wiki/Gimli_(Middle-earth)

This challenge is based on hash algorithms and encryption.

I am using OPENSSL v1.1.1 to create this challenge.

Here is a reference for using hash calculations with OPENSSL:
https://www.openssl.org/docs/man1.1.1/man1/openssl-dgst.html

If you are a Python coder, Python provides a hashing library you might find useful:
https://docs.python.org/3/library/hashlib.html

If this challenge has you wondering what to do next, please try my other challenges
that are worth fewer points.  The more points, the more difficult the challenge.

If you are new to CTF and/or not quite sure how to solve this challenge,
you should probably try these other challenges first in this order:
RubberDuck
Snowboard
PikesPeak
GandalfTheWise

After solving this ShahOfGimli challenge, then try:
HailCaesar
MountainMan
KeyMaker
VargasIsland

My Twitter DM's are open @kcbowhunter.

----------------------------

The third comment block is encrypted with AES CBC encryption using the following key:
sha256 hash of the string "CTFlearn"

Note that the comment block is also base64 encoded
There is no iv but you need to determine how to express this mathematically

If you are new to encryption and hash algorithms here is a good place to start:
openssl enc -help
openssl dgst -help
sha256sum

Of course Google is your friend (if you don't mind them recording all your online activity)

https://wiki.openssl.org/index.php/Enc is a good reference for openssl encryption algorithms
https://docs.python.org/3/library/hashlib.html
```

`CTFlearn{Gimli.Is.A.Dwarf}` is also not the right flag.

We notice that `This challenge is based on hash algorithms and encryption. I am using OPENSSL v1.1.1 to create this challenge.`

`file 20517` it is a tar. So `tar -xvf 20517`
Then we can find Another pic and an enc.

> The third comment block is encrypted with AES CBC encryption using the following key:
> sha256 hash of the string "CTFlearn"

sha256 of CTFlearn is `B18EF1351FC0DF641ABBE56DCD4928A8BB98452B1B43D8C1C13F1874C8B35056`

Then decode the third block.

```
CTFlearn{The_Shah_Of_Gimli_Is_The_Key}
CTFlearn{Gimli_Has_256_Gemstones}
CTFlearn{Breakfast_Hash_Is_The_Best}
```

`sha256sum Gimli04Base.jpg` and get `e26db845ae634c7d774f8924a565e34e215b659a97c7e1d01a401fea7c5f6d8`

`openssl enc -d -aes-256-cbc -iv 00000000000000000000000000000000 -K e26db845ae634c7d774f8924a565e34e215b659a97c7e1d01a401fea7c5f6d87 -in flag.enc -out flag -nopad`

#### Exif

`strings Computer-Password-Security-Hacker\ -\ Copy.jpg` and get the flag.
(Use vim or gedit is also ok)

#### Rubber Duck

Vim and `?CTF`

#### Snowboard

`strings Snowboard.jpg` and base64 decode.

#### PikesPeak

`strings` and flag is one of them

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

#### Milk's Best Friend

*Medium*

Discription:
There's nothing I love more than oreos, lions, and winning. https://mega.nz/#!DC5F2KgR!P8UotyST_6n2iW5BS1yYnum8KnU0-2Amw2nq3UoMq0Y Have Fun :)

`binwalk oreo.jpg`, we can find that there is a jpeg, a rar.
`binwalk --extract --dd=".*" oreo.jpg` to extract the rar.
Open the rar, you can find `a` , an ASCII text, `cat a` but it is not the flag.
So 'vim b.jpg' and '?flag', so we can get the flag.

#### Digital Camouflage

*Medium*

Discription:We need to gain access to some routers. Let's try and see if we can find the password in the captured network data: https://mega.nz/#!XDBDRAQD!4jRcJvAhMkaVaZCOT3z3zkyHre2KHfmkbCN5lYpiEoY
Hint 1: It looks like someone logged in with their password earlier. Where would log in data be located in a network capture?
Hint 2: If you think you found the flag, but it doesn't work, consider that the data may be encrypted.


As the hint goes, we know it's the traffic of a router and we need to find the password on it's web page.
So track the HTTP stream, we can the a POST request, and

```
0000   08 00 27 3d 47 5d 08 00 27 38 2c 5c 08 00 45 00   ..'=G]..'8,\..E.
0010   00 5f 2f 71 40 00 40 06 f7 22 0a 00 00 05 0a 00   ._/q@.@.÷"......
0020   00 01 e7 47 1f 90 89 7d 28 cc 77 ab 43 98 80 18   ..çG...}(Ìw«C...
0030   01 c9 03 3a 00 00 01 01 08 0a 00 0f 08 27 00 0f   .É.:.........'..
0040   26 52 75 73 65 72 69 64 3d 68 61 72 64 61 77 61   &Ruserid=hardawa
0050   79 6e 26 70 73 77 72 64 3d 55 45 46 77 5a 48 4e   yn&pswrd=UEFwZHN
0060   71 55 6c 52 68 5a 51 25 33 44 25 33 44            qUlRhZQ%3D%3D
```
Here we get the password which is URL encoded `UEFwZHNqUlRhZQ%3D%3D`
Decode it we can get `UEFwZHNqUlRhZQ==` (Actually, I get the all the chars in lower case, but it should be case sensitive, so replace the `%3D` with `=`)
Decode it with base64, we can get `PApdsjRTae`, that is the flag

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

### POST Practice
*medium* (actually it's *easy*)

Click the link and we can see the hint, which means we have to submit POST data.
Check the source you can see `<!-- username: admin | password: 71urlkufpsdnlkadsf -->`

So open burpsuite and capture the package and send a POST request by yourself.

```HTTP
POST http://165.227.106.113/post.php HTTP/1.1
Host: 165.227.106.113
...

username=admin&password=71urlkufpsdnlkadsf
```
The flag is in the Response

```
HTTP/1.1 200 OK
Connection: close
Content-Type: text/html
Date: Wed, 25 Mar 2020 08:24:14 GMT
Server: nginx/1.4.6 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.22
Content-Length: 32

<h1>flag{p0st_d4t4_4ll_d4y}</h1>
```

### Prehashbrown

*medium*

Discription:
I created a database of all known types of hashbrowns! Try to see if you can find a way to authenticate as an admin and retrieve the flag. Hashbrown Database

Yes, the aim is clear, SQL injection.

By checking the source code, we can find that the password is encrypted bt md5

```javascript
function hash() {
            document.form.password.value = md5(document.form.password.value);

            return true
        }
```

But ok, we have another choice, register.
So register a new account and login. Now we can see there is a search bar. And a hint under the bar.
> No hashbrowns came up for that search

Seems the search bar is vulnerable. Let's try to run sqlmap.

***
There are two ways to do POST injection via sqlmap

1. `sqlmap -r xxx.txt` <font color="blue">The xxx.txt is the POST request</font>
2. `sqlmap -u url  --data="name=value"`
***

Save the POST request as 1.txt and run sqlmap `sqlmap -r 1.txt --dbs --batch`
<font color="grey">For some users like me, the param --proxy is necessary.</font>
```
sqlmap -r 1.txt -D prehashbrown --table --batch
sqlmap -r 1.txt -D prehashbrown -T hashbrown --column  --batch --dump
```
And you can find the flag.

### Don't Bump Your Head(er)
*hard* (actually it's medium)

Discription:Try to bypass my security measure on this site! http://165.227.106.113/header.php

Click the link and you will find that your user-agent isn't right. Type `F12` to view the source code and you can find `<!-- Sup3rS3cr3tAg3nt  -->`

So change the value of user-agent as `Sup3rS3cr3tAg3nt`
And send the request
```HTTP
GET http://165.227.106.113/header.php HTTP/1.1
Host: 165.227.106.113
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Sup3rS3cr3tAg3nt
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en,zh-TW;q=0.9,zh-CN;q=0.8,zh;q=0.7,fr;q=0.6
Connection: close
```

In the response, you can find `Sorry, it seems as if you did not just come from the site, "awesomesauce.com".`
Referer identifies the address of the webpage which is linked to the resource being requested. By checking referer, the new webpage can see where the request originated.
Referer should be `awesomesauce.com`
```HTTP
GET http://165.227.106.113/header.php HTTP/1.1
Host: 165.227.106.113
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Sup3rS3cr3tAg3nt
Referer: awesomesauce.com
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en,zh-TW;q=0.9,zh-CN;q=0.8,zh;q=0.7,fr;q=0.6
Connection: close`
```

The flag is in the response.
```HTTP
HTTP/1.1 200 OK
Connection: close
Content-Type: text/html
Date: Wed, 25 Mar 2020 09:39:44 GMT
Server: nginx/1.4.6 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.22
Content-Length: 81

Here is your flag: flag{did_this_m3ss_with_y0ur_h34d}
<!-- Sup3rS3cr3tAg3nt  -->
```

### Inj3ction Time

*Hard*

Discription:I stumbled upon this website: http://web.ctflearn.com/web8/ and I think they have the flag in their somewhere. UNION might be a helpful command

## Binary

### Lazy Game Challenge

*easy*

Discription:
I found an interesting game made by some guy named "John_123". It is some betting game. I made some small fixes to the game; see if you can still pwn this and steal $1000000 from me!

To get flag, pwn the server at `nc thekidofarcrania.com 10001`

The key point is that it's hard to win, so when you place a bet, input a negative number (for example: -1000000000) and then you can loose the game as you like it. Each time you loose a game, you gain some money. And when the game ends, you will get the flag.

## Misc

### Help Bity

*Middle*

Discription:
Bity had the flag for his problem. Unfortunately, his negative friend Noty corrupted it. Help Bity retrieve his flag. He only remembers the first 4 characters of the flag: CTFL. Flag: BUGMdsozc0osx^0r^`vdr1ld|

The plain text: CTFL
The cipher text: BUGM
The order is "BC" "TU" "FG" "LM", so maybe it's xor.
Write a simple python program help_bity.py to solve it, then get `CTFLern{b1nry_1s_awes0me}`
But the flag isn't right, someone said that it is because the HTML show it in a wrong way. The ciphertext should be 

```
BUGMd`sozc0o`sx^0r^`vdr1ld|
```

Using this, finally I got the right flag.

## Programming

#### Simple Programming

Look at simple_programming.py
