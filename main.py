from argparse import ArgumentParser

import qrcode
from qrcode.image.svg import SvgImage

import wifi_qrcode_generator as qr

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--url", type=str, required=True)
    parser.add_argument("--out_file", type=str, required=True)
    return vars(parser.parse_args())


def save_qr_code(qr_img, f_name="qr.svg"):
    with open(f_name, "wb") as qr_file:
        qr_img.save(qr_file)

        
 def generate_wifi_pass_qr():
    qr.wifi_qrcode("WiFi_Name", False, "WPA", "PASSWORD")

if __name__ == "__main__":
    args = parse_args()
    img = qrcode.make(args["url"], image_factory=SvgImage)
    save_qr_code(img, f_name=f'{args["out_file"]}.svg')
