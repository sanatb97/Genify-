import eyed3
import os

def createSpectrogram(fileName):
	files = os.listDir()

	for file in files:
		if file.endswith('.mp3'):
			path = "'"+file
	
	try:
		os.system("sox "+path+"' -n spectrogram -Y 130 -l -r -o "+path[:len(path)-3]+"png'")
	except:
		print(path)
		print('Error')
	return