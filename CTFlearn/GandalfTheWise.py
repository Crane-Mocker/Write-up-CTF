import base64

str1 = base64.b64decode("xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p")
str2 = base64.b64decode("h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU")

for i in range(0, 39):
    print(chr(str1[i]^str2[i]), end="")
