import os
import pickle
import imutils
import cv2 as cv
import face_recognition
from imutils import paths


data_dir = r'.\data\train'
img_path = list(paths.list_images(data_dir))
vectors, names = [], []

for i, path in enumerate(img_path):
	name = path.split(os.path.sep)[-1]
	print('Encoding {}'.format(name))

	img = cv.imread(path)
	img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
	img = imutils.resize(img, 800)

	bbox = face_recognition.face_locations(img, model='hog')  # bbox coords
	features = face_recognition.face_encodings(img, bbox)     # list[0] = (128, ) array

	if len(features) == 1:
		vectors.append(features[0])
		names.append(name)

data = {'encodings': vectors, 'names': names}
f = open(os.path.join(data_dir, 'encodings.pickle'), 'wb')
f.write(pickle.dumps(data))
f.close()
