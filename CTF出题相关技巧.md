# CTF出题相关技巧


<!-- vim-markdown-toc GFM -->

* [Steganography](#steganography)
	* [Hidden Data into a File](#hidden-data-into-a-file)

<!-- vim-markdown-toc -->

## Steganography

### Hidden Data into a File

`apt install steghide`

Hide: `steghide embed -ef input.txt -cf input.jpg -sf output.jpg`

Extract: `steghide extract -sf output.jpg`
