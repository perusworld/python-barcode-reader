from imutils.video import VideoStream
import argparse
import datetime
import time
from barcode import BarCodeDecoder
import cv2
 
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

found = set()
decode = BarCodeDecoder()
while True:
	frame = vs.read()
	for decoded in decode.decode(frame):
		(x, y, w, h) = decoded['rect']
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
		text = "{} ({})".format(decoded['data'], decoded['type'])
		cv2.putText(frame, text, (x, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
		if decoded['data'] not in found:
			found.add(decoded['data'])
	cv2.imshow("Barcode Scanner", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break

vs.stop()