import subprocess

subprocess.call(['pyinstaller', '--onefile', '--icon', 'icon.ico', '--console', '--name', 'NN-Downloader', '--upx-dir', 'Z:/Projects/Python/### UPX ###', '--add-data=Z:/Projects/Python/NN-Downloader/.nn-d/Lib/site-packages/grapheme/data/*;grapheme/data/', 'main.py'])
