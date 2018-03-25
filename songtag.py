
import eyed3

audiofile = eyed3.load("/home/sanat/Desktop/SLAC 2018/DeepAudioClassification-master/Data/Raw/The Maccabees - Grew Up At Midnight.mp3")
audiofile.tag.artist = u"the Maccabees"
audiofile.tag.album = u"ABC"
audiofile.tag.album_artist = u"Various Artists"
audiofile.tag.title = u"We grew up at midnight"
audiofile.tag.track_num = 1
audiofile.tag.genre="Classical"
audiofile.tag.save()

audiofile2 = eyed3.load("/home/sanat/Desktop/SLAC 2018/DeepAudioClassification-master/Data/Raw/03 Khalibali - Padmaavat 320Kbps.mp3")
audiofile2.tag.artist = u"Khalibali"
audiofile2.tag.album = u"ABC"
audiofile2.tag.album_artist = u"Various Artists"
audiofile2.tag.title = u"Khalibali"
audiofile2.tag.track_num = 2
audiofile2.tag.genre="Pop"
audiofile2.tag.save()

"""audiofile2 = eyed3.load("/home/sanat/Desktop/SLAC 2018/DeepAudioClassification-master/Data/Raw/Bakar Bakar-(Mr-Jatt.com).mp3")
audiofile2.tag.artist = u"Nucleya"
audiofile2.tag.album = u"ABC"
audiofile2.tag.album_artist = u"Nucleya"
audiofile2.tag.title = u"Bakar Bakar"
audiofile2.tag.track_num = 3
audiofile2.tag.genre="EDM"
audiofile2.tag.save()"""