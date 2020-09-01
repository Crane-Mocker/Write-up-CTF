# We chall


<!-- vim-markdown-toc GFM -->

* [Training: Get Sourced](#training-get-sourced)
* [Training: Stegano 1](#training-stegano-1)
* [Crypto - Caesar I](#crypto---caesar-i)
* [Training: Crypto - Caesar II](#training-crypto---caesar-ii)
* [Training: MySQL I (MySQL, Exploit, Training)](#training-mysql-i-mysql-exploit-training)
* [PHP My Admin (Research)](#php-my-admin-research)
* [Training: MySQL II](#training-mysql-ii)
* [Excute `SELECT * FROM students where id='' union select null, 'admin', 'password';` We can see one row, 3 cols, `NULL admin password`](#excute-select--from-students-where-id-union-select-null-admin-password-we-can-see-one-row-3-cols-null-admin-password)
* [Training: WWW-Robots](#training-www-robots)
* [Training: ASCII](#training-ascii)
* [Encodings: URL](#encodings-url)
* [Training: Encodings I](#training-encodings-i)
* [Prime Factory (Math)](#prime-factory-math)
* [Training: Regex (Training, Regex)](#training-regex-training-regex)
* [Training: PHP LFI (Exploit, PHP, Training)](#training-php-lfi-exploit-php-training)
* [Here we know it has `include()`, <font color="blue">The include statement includes and evaluates the specified file.</font> and `eval() the line 1`](#here-we-know-it-has-include-font-colorbluethe-include-statement-includes-and-evaluates-the-specified-filefont-and-eval-the-line-1)
* [PHP 0817 (PHP, Exploit)](#php-0817-php-exploit)
* [Crypto - Transposition I (Crypto, Training)](#crypto---transposition-i-crypto-training)
* [Crypto - Substitution I (Crypto, Training)](#crypto---substitution-i-crypto-training)
* [Auth me(HTTP, Training)](#auth-mehttp-training)
* [Training: Baconian (Stegano, Encoding, Crypto, Training)](#training-baconian-stegano-encoding-crypto-training)

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
Payload is `admin' or '1'='1`

## PHP My Admin (Research)

Using Google advanced search, all these words "phpmyadmin wechall.net", still didn't find the phpmyadmin. But found an interesting fact that the provider himself called it "pma".

Searching about: pma wechall.net
We can find `pma.wechall.net`

## Training: MySQL II

```PHP
function auth2_onLogin(WC_Challenge $chall, $username, $password)
{
        $db = auth2_db();
        
        $password = md5($password);
        
        $query = "SELECT * FROM users WHERE username='$username'";
        
        if (false === ($result = $db->queryFirst($query))) {
                echo GWF_HTML::error('Auth2', $chall->lang('err_unknown'), false);
                return false;
        }
        
        
        #############################
        ### This is the new check ###
        if ($result['password'] !== $password) {
                echo GWF_HTML::error('Auth2', $chall->lang('err_password'), false);
                return false;
        } #  End of the new code  ###
        #############################
        
        
        echo GWF_HTML::message('Auth2', $chall->lang('msg_welcome_back', array(htmlspecialchars($result['username']))), false);
        
        if (strtolower($result['username']) === 'admin') {
                $chall->onChallengeSolved(GWF_Session::getUserID());
        }
        
        return true;
}
```

We can know that it uses `select` to get the all info from the table `users` and then check if the password is right. And the password is encrypted by md5.
So we can use `union select` to create a password.

----
I will show you an example at first.
We have a table `student`, and have cols like 'id' and so on.
When we run `select * from students where id=1` We can see the info where id=1.
If we run `select * from students where id=1 union select null, 'hello', 'world'`, we can see there are two rows of result, 3 columns. The first row is `NULL hello world`
Excute `SELECT * FROM students where id='' union select null, 'admin', 'password';` We can see one row, 3 cols, `NULL admin password`
----

So it can be `select * from users where username='' union select null, 'admin', md5('123')`
Payload will be `'union select null, 'admin', md5('123')#` and `123`
So the result will be NULL, admin, 123. Thus, when it checks for the password, it's a right one.

## Training: WWW-Robots

As the discription goes "Sometimes these files reveal the directory structure instead protecting the content from being crawled."
We need to visit the robots.txt to see the directory structure. We can see this:
```
User-agent: *
Disallow: /challenge/training/www/robots/T0PS3CR3T
```
The we visit this url.

## Training: ASCII 

There are lots of ways to represent ascii, for example chars, dec(1-3 digits), bin(7bit) and so on. Here the ascii ciphertext is dec(1-3 digits).
So the answer is `The solution is: gfsfsgbmibdl`.

## Encodings: URL

Just decode it `Yippeh! Your URL is challenge/training/encodings/url/saw_lotion.php?p=glhhgieapsac&cid=52#password=fibre_optics Very well done!
`
Then, visit this url

## Training: Encodings I

There are lots of 1 and 0. And the answer should be a string in English. So there are large possibility it should be bin to ascii.
For ascii, there are 7 or 8 digits to represent 127 or 255 chars.
First, use the jar to put the message in binary format, BitsPerBlock: 7.
And then bin to ascii.

## Prime Factory (Math)
To find the two numbers, I wrote a little python3 program, `prime_factory.py`	
It's inside this dir too. Run it and get the results:

> one result is:1000033
> one result is:1000037

## Training: Regex (Training, Regex)

The delimiter is `/`

Check the [syntax](https://www.rexegg.com/regex-quickstart.html).

level 1: The empty string should be `/^$/`. Because there is nothing between ^ and $.
level 2: A regular expression that matches only the string 'wechall' without quotes `/^wechall$/`
level 3: Your pattern shall match all images with the name wechall.ext or wechall4.ext and a valid image extension.Valid image extensions are .jpg, .gif, .tiff, .bmp and .png.
`/^wechall4?\.(?:jpg|gif|tiff|bmp|png)$/` Because wechall or wechall4 can be expressed as `wechall4?`,`.` is expressed as `\.` and choose one from the extension can be expressed as `?: |`
<font color="red">`(...)` means match and capture,`(?:...)`means match but not capture. </font>
level 4: Capture the filename, without extension `/^(wechall4?)\.(?:jpg|gif|tiff|bmp|png)$/`, because the only difference between level 3 and level 4 is that, in level 3 you should capture.

## Training: PHP LFI (Exploit, PHP, Training)

Here we know there is an LFI vuln. But in real world pentest, we can often test like this

----
fist, using `../`to check if there is LFI vuln. We use `?file=..`here and we got 
```
PHP Warning(2): include(pages/../.html): failed to open stream: No such file or directory in /home/wechall/www/wc5/www/challenge/training/php/lfi/up/index.php(54) : eval()'d code line 1
PHP Warning(2): include(): Failed opening 'pages/../.html' for inclusion (include_path='.:/usr/share/php') in /home/wechall/www/wc5/www/challenge/training/php/lfi/up/index.php(54) : eval()'d code line 1
```
Here we know it has `include()`, <font color="blue">The include statement includes and evaluates the specified file.</font> and `eval() the line 1`
----

```php
$code = '$filename = \'pages/\'.(isset($_GET["file"])?$_GET["file"]:"welcome").\'.html\';';
$code_emulate_pnb = '$filename = Common::substrUntil($filename, "\\0");'; # Emulate Poison Null Byte for PHP>=5.3.4
$code2 = 'include $filename;';
```

As the highlight code shows, it includes and evaluates the $filename, whether the thing after `?file=` or `welcome`. And it adds `'.html'`.
(So as you can see, the defualt page `index.php` actually shows `?file=welcome`, the `welcome.html`)
As the hint goes, we should run `../solution.php`, `../` means the parent directory of `pages/`(The path should be like `lfi/up/pages/`, the `welcome.html`and so on is under the dir `pages/`). So when using `?file=`, it should be `?file=../../solution.php`. And it adds `.html`, so using `%00`to end the statement.(Because the PHP core is implement by C. When connectiong strings, null byte `\x00` will be used as the end of string.)
The payload should be `?file=../../solution.php%00`

## PHP 0817 (PHP, Exploit)

In PHP, `echo (int)"string";`, will return `0`. And there is no `break;` in case 0 and 1 so it will execute case 2.

Payload: `?which=solution`

## Crypto - Transposition I (Crypto, Training)

oWdnreuf.lY uoc nar ae dht eemssga eaw yebttrew eh nht eelttre sra enic roertco drre . Ihtni koy uowlu dilekt  oes eoyrup sawsro don:wh nfhdccmibh.r

You can see, it looks like "wonderful..."
The two characters near each other change the position.
Using `transposition_1.py` to decode, and you can see:
> Wonderful. You can read the message way better when the letters are in correct order. I think you would like to see your password now: hfndhccimhbr.

## Crypto - Substitution I (Crypto, Training)

As the hint goes, it will be a kind of monoalphabetic cipher.
Caesar cipher is also a kind of monoalphabetic cipher.It is a substitution cipher in which for a given key, the cipher alphabet for each plain alphabet is fixed throughout the encryption process. 
So the letters will have the certain frequency.(But truely, I failed by doing so)

QH ZSP RABFLSZH LEO HEG DRU TPRO ZSFY BH VTFPUO F RB FBKTPYYPO CPTH JPAA OEUP HEGT YEAGZFEU WPH FY RTBBQDOAFOAV ZSFY AFZZAP DSRAAPULP JRY UEZ ZEE SRTO JRY FZ
`F RB`,the format looks like `I AM`
Using quipquip.com and `RB=AM`as clue
The plaintext is `BY THE ALMIGHTY GOD YOU CAN READ THIS MY FRIEND I AM IMPRESSED VERY WELL DONE YOUR SOLUTION KEY IS ARMMBCDLIDLF THIS LITTLE CHALLENGE WAS NOT TOO HARD WAS IT`

Here is a detailed [wp](http://m.blog.naver.com/dual5651/60131688181) by a korean.

## Auth me(HTTP, Training)

Look at the apache.conf

```
<VirtualHost *:443>
        ServerName authme.wechall.net #the domain
        DocumentRoot /home/wechall/www/wc5/www
        GnuTLSEnable on #TLS, so here are some certifications needed
        GnuTLSCertificateFile /etc/pki_jungle/authme/certs/server.crt
        GnuTLSKeyFile /etc/pki_jungle/authme/private/server.key
        GnuTLSClientCAFile /etc/pki_jungle/authme/certs/client_bundle.crt
        GnuTLSPriorities NORMAL:!AES-256-CBC:%COMPAT
        GnuTLSClientVerify require
        <Directory "/home/wechall/www/wc5/www">
                GnuTLSClientVerify require
                Options Indexes FollowSymLinks
                AllowOverride All
        </Directory>
        <Directory "/home/wechall/www/wc5/www/challenge/space">
                GnuTLSClientVerify require
                Options Indexes FollowSymLinks
                AllowOverride None
        </Directory>
        AssignUserID wechall wechall
        ErrorLog /home/wechall/www/auth_me.errors.log
        CustomLog /home/wechall/www/auth_me.access.log combined
</VirtualHost>
```

So as we can see, the conf is about the virtual host whose domain is `authme.wechall.net`. It uses TLS, some certifications are needed.

Then visit https://authme.wechall.net/challenge/space/auth_me/www/index.php, and you can see `ERR_BAD_SSL_CLIENT_AUTH_CERT`, certs are needed.

Then go back at the conf, we notice that the url looks interesting `http://www.wechall.net/challenge/space/auth_me/find_me/apache.conf`
Click `http://www.wechall.net/challenge/space/auth_me/find_me/`
Then we can find the things we need.
Download them. Try to import it to Chrome, only client.p12 can be imported. Then visit the box again.

## Training: Baconian (Stegano, Encoding, Crypto, Training)

There are only 2 kinds of chars in Bacon cipher. In the message, it should be the lower and upper case.

There result is (the programs `baconian.py` are in the wechall_material dir)
> bababaabaabaaabbbaaababbbbabbaaabaaababbababbbabbbaaabbabbbaabbabaabaababbbaababaabaaababbababbabbbababbababbbaabbbaaaaaaaabaababaaabaabaaabbabbbbaabbaabbbaabaababbbbaabaaabaaaaababaaabaabaabaabbbabbbababaaabaabbaaababbaabbbabaaabaaabbbabbbabaaabaabababbbbaaababbbbababbabaaabaaabaabaaaaaaaabbbaaaaaaabbabaabbaabbabbabbbbabbbabababababaabababababbababaabababaabbababbbababaababbbababaababbabbabaababababbababbababaabaaababbabbabbabbababababaabababbabaababbabbaabaababababaababababaabaababbabababababbababababbbababbabababbabaabaababbababaabbabababbaabaabbabbaabaabbaabaabababababbababababaababababaabaababababaabbababababbaabaabaababaabababbabaabababbaabaababaabababaababbaababababaabbabbabababababbababababababababbaabababaabbababaabaabbbaaabaabababbabbababababaabababaabababbaababababababababababababaabbabbababbabababbaababababbabaabbbabbababababababababaabbabababaababbbabaababababbabababaabbabaababbaabababaabaababababbababababaabababbaabababaabaabababaababbababaabaababababbabababababababbabbabaababababaabaabbabaabaabaababaabababababaabababaababababbbababababbabababababbabababababbabababbabbababbabababbabaababbababaabaabababababaababababbaabbabaabbbabbabbababbaababaabaababababaabbaabababababaababaabbabbaababababaabababababababbabababababbaababababbabababbabbabababbaabaababaabababbabbaababbaababaabaabababababaabababbabababbaabababababaabababbaababaababababbababbabababbabbaabbabbababbabbabaabaababababbbababaabababaabbabaabaababbababab

But using a bacon-cipher decoder, it cannot give a right answer.
As the hint goes, the decode method should be given by wiki, so write another short program.(baconian1.py)

As you run my program, you can find that there are some unit not fit the chart. That's why you can't decode the ciphertext directly by a decoder.

> veryxwellxdonexfellowxhackerxthexecretxkeywordxixrplireaoangnxxkvfkujouwkwwurnwvfnfwjkvewvlkxlkjnjvmtmtevlkuvjfknkzeuvuvkkzktnkwvkvuoevwvjkkzkvkvjwwvvuvkvjvjovvjuwkkwvjlfjfjnjflkvlnfkjukkvfjkkvnkwvwwvuwuvjkzuwwkjktfktmvjkvnkwkwvwvkkfkvfnlfkwkkwwvwnvwkxkktjfv

Here are some extra x, so delete it by changing `text+='x'` to `text+=" "` and run it again.

Then you can get
> very well done fellow hacker the ecret keyword i rplireaoangn  kvfkujouwkwwurnwvfnfwjkvewvlk lkjnjvmtmtevlkuvjfknkzeuvuvkkzktnkwvkvuoevwvjkkzkvkvjwwvvuvkvjvjovvjuwkkwvjlfjfjnjflkvlnfkjukkvfjkkvnkwvwwvuwuvjkzuwwkjktfktmvjkvnkwkwvwvkkfkvfnlfkwkkwwvwnvwk kktjfv

So the flag for me is "rplireaoangn"
