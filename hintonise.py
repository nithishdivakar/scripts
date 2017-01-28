from PIL import Image
import PIL
import numpy
from itertools import product
from tqdm import tqdm
import random

I = Image.open('img.png').convert("L")

stride = 32
rprob  = 0.99
gprob  = 0.01
bprob  = 0.01

resize = True

if resize:
    s = I.size
    B = 256
    wpercent = (B/float(s[0]))
    H = int((float(s[1])*float(wpercent)))
    I = I.resize((B,H),PIL.Image.ANTIALIAS)

B,H = I.size

J = numpy.zeros((H*stride,B*stride,3))
I = numpy.asarray(I)


pbar = tqdm(list(product( range(H),range(B))))
for x,y in pbar:
    pix = I[x,y]

    k   = (pix/256.0)*stride 
    midx,midy = x*stride+int(stride/2),y*stride+int(stride/2)
    radius = int(k/2)
    
    if random.random() < rprob:
        J[midx-radius:midx+radius,midy-radius:midy+radius,0] = 255
    if random.random() < gprob:
        J[midx-radius:midx+radius,midy-radius:midy+radius,1] = 255
    if random.random() < bprob:
        J[midx-radius:midx+radius,midy-radius:midy+radius,2] = 255

J = numpy.asarray(J,dtype='uint8')

Image.fromarray(J).save("hitonised.png")
