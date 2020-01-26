import os
import time
import serial
import pickle
import cv2 as cv
import datetime as dt
import face_recognition
from collections import Counter

timer = 3
ser = serial.Serial('com7', 9600)

data_dir = r'.\data\train'
data = pickle.loads(open(os.path.join(data_dir, 'encodings.pickle'), 'rb').read())

ch = input('1. Laptop Webcam\n2. WiFi Webcam\n')
if ch == '2':
	url = input('Enter webcam IP: ')  # URL of your webcam. Eg- 'http://192.168.0.7:8080/video'
	cap = cv.VideoCapture(url)
else:
	cap = cv.VideoCapture(0)

face_encodings, face_names, final_name, name = [], [], [], ''


def _get_frame():
	ret, frame = cap.read()
	frame = cv.flip(frame, 1)
	rgb_frame = frame[:, :, ::-1]
	face_locations = face_recognition.face_locations(rgb_frame, model='cnn')
	return rgb_frame, face_locations


while True:
	rgb_frame_1, face_locations_1 = _get_frame()[0], _get_frame()[-1]
	face_encodings = face_recognition.face_encodings(rgb_frame_1, face_locations_1)

	if len(face_locations_1) == 0:
		ser.write(str.encode('0'))
		print('Nothing to see')

	if face_locations_1:
		end_time = dt.datetime.now() + dt.timedelta(seconds=timer)

		while dt.datetime.now() <= end_time:
			for face_encoding in face_encodings:
				match = face_recognition.compare_faces(data['encodings'], face_encoding, tolerance=0.5)

				if True in match:
					match_idxs = [data['names'][i] for i in [i for (i, j) in enumerate(match) if j]]
					cntr = Counter(match_idxs)
					name = max(match_idxs, key=cntr.get)
				else:
					name = 'Unknown'

				print(name)
				face_names.append(name)
				final_name.append(name)

			face_encodings = face_recognition.face_encodings(_get_frame()[0], _get_frame()[-1])

		if len(final_name) > 9:  # The no. of matches = 9
			final_count = Counter(final_name)
			name = max(final_name, key=final_count.get)

			if name != 'Unknown':
				ser.write(str.encode('1'))
				print('Id matched: {}'.format(name))
				time.sleep(3)  # Wait for the door to open
				ser.write(str.encode('0'))  # Switch off the motor
				time.sleep(5)
			else:
				ser.write(str.encode('0'))
				print('No match found')

		final_name = []

	if cv.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv.destroyAllWindows()
