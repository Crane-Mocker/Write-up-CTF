# 蓝牙


<!-- vim-markdown-toc GFM -->

* [BLE](#ble)
	* [bluepy](#bluepy)
	* [bleah](#bleah)

<!-- vim-markdown-toc -->

## BLE

https://www.anquanke.com/post/id/168116

### bluepy

bluepy只能在linux上用，可以用py2.7可以用3.4
`sudo apt-get install git build-essential libglib2.0-dev`
`sudo -H pip2 install bluepy`或`sudo -H pip3 install bluepy`

### bleah

https://hackersgrid.com/2017/09/bleah.html

bleah基于bluepy.

安装方法：

```bash
git clone https://github.com/evilsocket/bleah.git
cd bleah
python setup.py build
sudo python setup.py install
```
