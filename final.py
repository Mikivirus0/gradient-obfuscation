import cv2
import numpy as np
import urllib.request
import os
import bm3d
import argparse

def download_model(url, model_path):
    if not os.path.exists(model_path):
        urllib.request.urlretrieve(url, model_path)

def apply_denoising(image, denoising_strength=1.0):
    image_float = image.astype(np.float32) / 255.0
    denoised_image_float = bm3d.bm3d(image_float, sigma_psd=np.std(image_float) * denoising_strength, stage_arg=bm3d.BM3DStages.ALL_STAGES)
    denoised_image = (denoised_image_float * 255).astype(np.uint8)
    return denoised_image

def apply_style_transfer(image, style='the_wave'):
    styles = {
        'the_wave': 'https://github.com/linhlinhle997/style-transfer/blob/master/models/eccv16/the_wave.t7',
        'starry_night': 'https://github.com/linhlinhle997/style-transfer/blob/master/models/eccv16/starry_night.t7',
        'la_muse': 'https://github.com/linhlinhle997/style-transfer/blob/master/models/eccv16/la_muse.t7'
    }
    model_url = styles[style]
    model_path = f'{style}.t7'
    #download_model(model_url, model_path) To Download the model 
    net = cv2.dnn.readNetFromTorch(model_path)
    blob = cv2.dnn.blobFromImage(image, 1.0, (224, 224), (104, 117, 123), False, False)
    net.setInput(blob)
    styled_image = net.forward()
    styled_image = styled_image.reshape((3, 224, 224))
    styled_image = styled_image.transpose(1, 2, 0)
    styled_image = cv2.resize(styled_image, (image.shape[1], image.shape[0]))
    return styled_image

def enhance_image(image):
    ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    channels = cv2.split(ycrcb)
    cv2.equalizeHist(channels[0], channels[0])
    enhanced_ycrcb = cv2.merge(channels)
    enhanced_image = cv2.cvtColor(enhanced_ycrcb, cv2.COLOR_YCrCb2BGR)
    return enhanced_image

def obfuscate_image(image_path, style='the_wave', denoising_strength=1.0):
    image = cv2.imread(image_path)
    denoised_image = apply_denoising(image, denoising_strength)
    enhanced_image = enhance_image(denoised_image)
    obfuscated_image = apply_style_transfer(enhanced_image, style)
    return obfuscated_image


parser = argparse.ArgumentParser(description='Image Obfuscation')
parser.add_argument('-F', '--filename', type=str, help='Input image filename')
parser.add_argument('-S', '--style', type=str, choices=['s', 't', 'l'], help='Style name (s=starry_night, t=the_wave, l=la_muse)')
parser.add_argument('-st', '--strength', type=float, help='Denoising strength')
parser.add_argument('-o', '--output', type=str, help='Output image filename')
args = parser.parse_args()


if not all([args.filename, args.style, args.strength, args.output]):
    parser.error('Please provide the filename, style, and strength arguments.')

style_map = {
    's': 'starry_night',
    't': 'the_wave',
    'l': 'la_muse'
}


style = style_map[args.style]
strength= args.strength
input_image_path = args.filename
output_image_path = args.output
input_image = cv2.imread(input_image_path)


obfuscated = obfuscate_image(input_image_path, style, strength)
cv2.imwrite(output_image_path, obfuscated)