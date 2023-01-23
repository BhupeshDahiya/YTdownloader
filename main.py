import sys
import pafy
import requests
from pathlib import Path
downloads_path = str(Path.home() / "Downloads")

def get_inp():
	url = input('Enter a YouTube video link: ')
	try:
		if (url[:24] != 'https://www.youtube.com/') or requests.get(url).status_code != 200:
			sys.exit()
	except:
		print("Enter a valid link, make sure it starts with 'https://www.youtube.com/'\nTerminating Program.")
		sys.exit()
	return url

def show_details(url):
	global vid
	global best
	vid = pafy.new(url)
	best = vid.getbest(preftype='mp4')
	print(f'Title: {vid.title}\nChannel: {vid.author}\nDuration: {vid.duration}\nBest Resolution: {best.resolution}')

def save_vid():
	print('Downloading video in your downloads folder...')
	vid.download(downloads_path)

def save_audio():
	print('Downloading audio in your downloads folder...')
	vid.getbestaudio().download(downloads_path)

def save():
	task = input('\nSave Video, Audio or None(v,a,n): ')
	if task == 'v':
		save_vid()
	elif task == 'a':
		save_audio()
	elif task != 'n':
		print('Incorrect input')

if __name__ == '__main__':
	show_details(get_inp())
	save()
