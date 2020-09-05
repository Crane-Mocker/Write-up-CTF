# Game of Hacks


<!-- vim-markdown-toc GFM -->

			* [Beginner](#beginner)
				* [SQL Injection](#sql-injection)
* [](#)
				* [Path Traversal](#path-traversal)
				* [DOS by sleep](#dos-by-sleep)
				* [CSRF(?)](#csrf)

<!-- vim-markdown-toc -->

## Beginner

### SQL Injection

```javascript
var mysql = require('db-mysql');//load module
var http = require('http');
var out;
var valTom;
//request data, append a chunk of data to valTom
var req = http.request(options, function(res)
{
	res.on('data', function(chunk)
	{
		valTom = chunk;
	}
	);
}
);
new mysql.Database(
{
	hostname: 'localhost',
	user: 'user',
	password: 'password',
	database: 'test'
}
).connect(function(error)
{
	var the_Query =
	"INSERT INTO Customers (CustomerName, ContactName) VALUES ('Tom'," +
	valTom + ")";// the sql command, no protection on vector valTom
	this.query(the_Query).execute(function(error, result)
	{
		if (error)
		{
			console.log("Error: " + error);
		}
		else
		{
			console.log('GENERATED id: ' + result.id);
		}
	}
	);
	out = resIn;
}
);
```

`require()` is not part of the standard JavaScript API. But in Node.js, it's a built-in function with a special purpose: to load modules.

###

```
class ApplicationController < ActionController::Base
protect_from_forgery with: :exception
end
class UsersController < ApplicationController
def update
con = Mysql.new 'localhost', 'user', 'pwd'
con.query 'UPDATE users set name = ' + params[:name] +
' where id = ' + params[:id]
con.close
end
end
```

### Path Traversal

```java
def path = System.console().readLine 'Enter file path:'
if (path.startsWith("/safe_dir/"))
{
	File f = new File(path);
	f.delete()
}
```

Directory traversal (also known as file path traversal) is a web security vulnerability that allows an attacker to read arbitrary files on the server that is running an application.



### DOS by sleep

```vb
Private Sub cmdRunNotePad_Click()
Dim str As String
MyVar = window.Text()
Sleep myVar+1
dblNotePadID = Sleep(myVar)
End Sub
```

The Visual Basic compiler uses the Dim statement to determine the variable's data type and other information, such as what code can access the variable. The following example declares a variable to hold an Integer value.

### CSRF(?)

```PHP
/*Redirect to a different page in the current directory that was requested*/
$host  = $_SERVER['HTTP_HOST'];
$uri   = rtrim(dirname($_SERVER['PHP_SELF']), '/');
$extra = $_GET['page']; #'mypage.php';
header("Location: http://$host$uri/$extra");
exit;
```

$_SERVER -- $HTTP_SERVER_VARS [removed] — Server and execution environment information
rtrim — Strip whitespace (or other characters) from the end of a string
header — Send a raw HTTP header
 
