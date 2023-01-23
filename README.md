# YTdownloader
Script to download video/audio files from a youtube link without going through all the hazzle.

## Prerequisites
You'll need need pafy, requests and youtube-dl 
or simple copy paste the lines below in your terminal.

```
pip install pafy
pip install requests
pip install youtube-dl
```



Due to youtube removing the dislike counter the youtube-dl library was not working as intended so i implemented a quickfix:
- Open the backend_youtube_dl.py file in the pafy folder ,  you'll find it where ever your terminal downloads your library in my case it was located at C:\Users\User_name\PycharmProjects\pythonProject\venv\Lib\site-packages\pafy\backend_youtube_dl.py
- Once you've opened the file find the line ```self._likes = self._ydl_info.get['like_count']```            
           ```self._dislikes = self._ydl_info.get['dislike_count']``` usually at line 50 and comment it out.
