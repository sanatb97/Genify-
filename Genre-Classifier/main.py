from flask import Flask,render_template,request
from werkzeug import secure_filename
from PIL import Image
import os

app = Flask(__name__)

@app.route('/home')
def home():
	return render_template('main.html')

@app.route('/uploader',methods =['GET','POST'])
def uploader():
	if request.method == 'POST':
		f = request.files['file']
		f.save(secure_filename(f.filename))
		files = os.listdir()
		for file in files:
			if file.endswith('.mp3'):
				path = "'"+file
		try:
			os.system("sox "+path+"' -n spectrogram -Y 130 -l -r -o "+path[:len(path)-3]+"png'")
			image_file_name = path[1:len(path)-3]+"png";
			img = Image.open(image_file_name)
			width, height = img.size
			desiredSize = 128
			nbSamples = int(width/desiredSize)
			width - desiredSize
			for i in range(nbSamples):
				startPixel = i*desiredSize
				imgTmp = img.crop((startPixel, 1, startPixel + desiredSize, desiredSize + 1))
				imgTmp.save("F_"+str(i)+".png")
			
		except:
			print(path)
			print('Error')

		return render_template('main.html')

if __name__ == '__main__':
   app.run(debug = True)