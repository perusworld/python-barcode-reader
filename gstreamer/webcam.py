import datetime
import gstreamer
from barcode import BarCodeDecoder


def main():
    found = set()
    decode = BarCodeDecoder()
    def user_callback(image, svg_canvas):
        for decoded in decode.decode(image):
            text = "{} - {} ({})".format(datetime.datetime.now(), decoded['data'], decoded['type'])
            print(text)
            if decoded['data'] not in found:
                found.add(decoded['data'])

    gstreamer.run_pipeline(user_callback)

if __name__ == '__main__':
    main()
