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
* [Prime Factory: Math](#prime-factory-math)

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

## Prime Factory: Math
To find the two numbers, I wrote a little python3 program, `prime_factory.py`	
It's inside this dir too. Run it and get the results:

> one result is:1000033
> one result is:1000037
