import eyed3
import os

path = "'/media/nishant/Seagate Expansion Drive/Stuff/NISHANT/Music/Songs/Rock"
l = os.listdir('/media/nishant/Seagate Expansion Drive/Stuff/NISHANT/Music/Songs/Rock')

for i in l:
	try:
		os.system("sox "+path+"/"+i+"' -n spectrogram -Y 130 -l -r -o '"+i[:len(i)-3]+"png'")
	except:
		print(path+i)
		print('Error')