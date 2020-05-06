import numpy as np
import requests
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import cv2

def read_img_from_url():
    img = cv2.imread("ori.jpg")
    img = cv2.resize(img, (300,300))
    img_matrix = np.array(img)
    return img_matrix

def read_txt_from_url(url, * size):
    text = requests.get(url).text
    wc = WordCloud(background_color="white", max_words=100, max_font_size=100,
                   width=size[0], height=size[1],
                   random_state=42)
    wc.generate(text)
    return wc.to_array()

img_matrix = read_img_from_url()
txt_url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
txt_matrix = read_txt_from_url(txt_url, *img_matrix.shape)

img_matrix[txt_matrix == 255] = 0

plt.figure(figsize= (10, 10), dpi=300)
plt.imshow(img_matrix)
plt.axis('off')
plt.show()

