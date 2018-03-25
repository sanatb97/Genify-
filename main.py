# -*- coding: utf-8 -*-
import random
import string
import os
import sys
import numpy as np
from PIL import Image
from model import createModel
from datasetTools import getDataset
from config import slicesPath
from config import batchSize
from config import filesPerGenre
from config import nbEpoch
from config import validationRatio, testRatio
from config import sliceSize

from songToData import createSlicesFromAudio
def getProcessedData(img,imageSize):
    img = img.resize((imageSize,imageSize), resample=Image.ANTIALIAS)
    imgData = np.asarray(img, dtype=np.uint8).reshape(imageSize,imageSize,1)
    imgData = imgData/255.
    return imgData

def getImageData(filename,imageSize):
    img = Image.open(filename)
    imgData = getProcessedData(img, imageSize)
    return imgData
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("mode", help="Trains or tests the CNN", nargs='+', choices=["train","test","slice"])
args = parser.parse_args()
genre_list=['Rock', 'Pop', 'EDM', 'Jazz', 'Metal']
print("--------------------------")
print("| ** Config ** ")
print("| Validation ratio: {}".format(validationRatio))
print("| Test ratio: {}".format(testRatio))
print("| Slices per genre: {}".format(filesPerGenre))
print("| Slice size: {}".format(sliceSize))
print("--------------------------")

if "slice" in args.mode:
	createSlicesFromAudio()
	sys.exit()

#List genres
genres = os.listdir(slicesPath)
genres = [filename for filename in genres if os.path.isdir(slicesPath+filename)]
print(genres)
nbClasses = len(genres)

#Create model 
model = createModel(nbClasses, sliceSize)

if "train" in args.mode:

	#Create or load new dataset
	train_X, train_y, validation_X, validation_y = getDataset(filesPerGenre, genres, sliceSize, validationRatio, testRatio, mode="train")

	#Define run id for graphs
	run_id = "MusicGenres - "+str(batchSize)+" "+''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(10))

	#Train the model
	print("[+] Training the model...")
	
	model.fit(train_X, train_y, n_epoch=nbEpoch, batch_size=batchSize, shuffle=True, validation_set=(validation_X, validation_y), snapshot_step=100, show_metric=True, run_id=run_id)

		
	print("    Model trained! ✅")

	#Save trained model
	print("[+] Saving the weights...")
	model.save('musicDNN.tflearn')
	print("[+] Weights saved! ✅💾")


if "test" in args.mode:

	#Create or load new dataset
	test_X, test_y = getDataset(filesPerGenre, genres, sliceSize, validationRatio, testRatio, mode="test")
	#Load weights
	print("[+] Loading weights...")
	model.load('musicDNN.tflearn')
	print("    Weights loaded! ✅")

	testAccuracy = model.evaluate(test_X, test_y)[0]
	results=model.predict_label(test_X)
	glist=[]
	l=model.predict(test_X)
	for i in results:
		g=[]
		for j in i:
			g.append(genre_list[j])
		glist.append(g[0])
		
"""img = Image.open('Data/Slices/Jazz/Jazz_Spectro(2)_4.png')
print(img)
imgData = getProcessedData(img,128)
X=imgData
#print(X)
test_X = np.array(X[:1]).reshape([-1, 128, 128, 1])
print(test_X)

#print(img)


testarr=[]
imgarr=[]
for i in range(6):
	imgData = getImageData('Data/Slices/Jazz/Jazz_Spectro(2)_'+str(i+1)+'.png', sliceSize)
	imgarr.append(imgData)


	





testarr.append(test_X)
results=model.predict_label(testarr)
glist=[]
l=model.predict(testarr)
print(results)
'''for i in results:
	g=[]
	for j in i:
			
		g.append(genre_list[j])
		glist.append(g[0])
print(glist[0])'''
"""
	#train_X, train_y, validation_X, validation_y = getDataset(filesPerGenre, genres, sliceSize, validationRatio, testRatio, mode="train")
"""
"""

print(glist)
print("[+] Test accuracy: {} ".format(testAccuracy))
	







