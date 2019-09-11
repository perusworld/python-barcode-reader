from imutils.video import VideoStream
import argparse
import datetime
import time
from barcode import BarCodeDecoder
 
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

found = set()
decode = BarCodeDecoder()
while True:
	for decoded in decode.decode(vs.read()):
		text = "{} - {} ({})".format(datetime.datetime.now(), decoded['data'], decoded['type'])
		print(text)
		if decoded['data'] not in found:
			found.add(decoded['data'])
 
vs.stop()