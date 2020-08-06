#!/usr/bin/python3
import requests

url_visit = "http://www.wechall.net/challenge/training/programming1/index.php?action=request"
url_send = "http://www.wechall.net/challenge/training/programming1/index.php?answer="
cookie = {"WC" : "12800984-54632-qPJeo3bgCJnSRMo0f"}
key = requests.get(url_visit, cookies = cookie)
ans = requests.get(url_send + key.text, cookies = cookie)
