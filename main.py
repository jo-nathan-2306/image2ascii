from PIL import Image,  ImageFilter
import streamlit as st
st.set_page_config(page_title="ASCII Art Converter", page_icon=":art:")
st.write("# ASCII Art Converter")
global img
img=st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

convert = st.button("Convert to ASCII Art")
ascchars = list(" .'`^\",:;Il!i~+_-?][}{1)(|\\/*tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$") 
n = st.slider("Image width", 40, 200, 100)
def resizeimg(image,new_width=n):
    w,h=image.size
    ratio=h/w
    aspect_ratio = 0.55  
    nheight = int(new_width * ratio * aspect_ratio)

    resizedimg=image.resize((new_width,nheight))
    return(resizedimg)
def gray(image):
    grayimg=image.convert("L")
    return grayimg
def p2a(image):
    pixels = image.getdata()
    scale = len(ascchars) - 1
    def pixel_to_char(pixel):
        gamma = 2.2
        brightness = (pixel / 255) ** gamma
        index = int(brightness * (len(ascchars) - 1))
        return ascchars[index]

    chars = "".join([pixel_to_char(p) for p in pixels])
    return chars

def main(uploaded_img, new_width=n):
    resized = resizeimg(uploaded_img, new_width)
    grayscale = gray(resized)
    newimg = p2a(grayscale)
    pixelc = len(newimg)
    asciimage = "\n".join(newimg[i:i + new_width] for i in range(0, pixelc, new_width))
    st.code(asciimage, language='plaintext')

if img and convert:
    image = Image.open(img)
    main(image)
