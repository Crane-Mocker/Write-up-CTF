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
