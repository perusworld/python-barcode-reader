from pyzbar import pyzbar
import datetime

class BarCodeDecoder:
    def decode(self, frame):
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            yield {
                'data': barcode.data.decode("utf-8"),
                'type': barcode.type,
                'rect': barcode.rect
            }
