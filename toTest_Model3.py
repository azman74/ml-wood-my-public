import cv2
import numpy as np
import os
from imutils import paths

# in machine 3, to deploy in server

def setClassifierFromFolder(string1):
  
  string2 = 'ml-wood-my/' + string1
  imagePaths = paths.list_images(string2)
  
  labels = []
  for imagePath in imagePaths:
    label = imagePath.split(os.path.sep)[-2]
    labels.append(label)
  
  labels.sort()
  #print(labels)
  labels = list(dict.fromkeys(labels))
  return labels
  
def getAllImagesSorted(folder_name):

  folder_list = []
	
  for i in folder_name:
    folder_list += setClassifierFromFolder(i)
  
  folder_list.sort()
  return folder_list

def getImagePredict(image, folder, model):
  
  image = cv2.resize(cv2.imread(image), (50, 50))
  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  
  image = image.astype('float32')
  image /= 255
  
  image = (np.expand_dims(image,0))
  
  pred1 = model.predict(image)
  pred1 = pred1.ravel()
  
  labels = setClassifierFromFolder(folder)
  
  #print(pred1)
  #print(pred1.max())
  return labels[pred1.argmax(axis=0)]
  
def getListInsideFolder(string1):

	string2 = 'ml-wood-my/' + string1
	imagePaths = paths.list_images(string2)
	
	labels = []
	for imagePath in imagePaths:
		label = imagePath.split(os.path.sep)[0]
		label += '/'
		label += imagePath.split(os.path.sep)[1]
		#label += '/'
		#label += imagePath.split(os.path.sep)[2]
    
		labels.append(label)
    
	labels = list(dict.fromkeys(labels))
	return labels
	
def getAllImages(folder_name):

	folder_list = []
	
	for i in folder_name:
		folder_list += getListInsideFolder(i)
		
	return folder_list
