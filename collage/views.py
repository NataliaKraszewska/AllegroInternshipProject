from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
from urllib.request import urlopen
from urllib import request
import random
import requests
from io import BytesIO
# Create your views here.

def collage_view(request):

	
	ordered = int(request.GET.get('ordered',1))
	rozdzielczosc = str(request.GET.get('rozdzielczosc','2480x2480'))
	zdjecia= str(request.GET.get('zdjecia',None))
	size = rozdzielczosc.split('x')
	x = int(size[0])
	y = int(size[1])

	listofimages = zdjecia.split(',')

	if ordered != 1:
		random.shuffle(listofimages) 
	
	response = HttpResponse(content_type="image/png")
	image = create_collage(x,y, listofimages)
	image.save(response, "PNG")
	return response

def create_collage(width, height, listofimages):
	if len(listofimages) == 1:
		image = Image.open(urlopen(listofimages[0]))
		return image

	if len(listofimages) % 2 == 0:
		x = ImageSetDivisibleByTwo(width,height,listofimages)
		return x
	else:
		x = ImageSetIndivisibleByTwo(width, height, listofimages)
		return x


def ImageSetDivisibleByTwo(width, height, listofimages):
	if len(listofimages) == 6:
		cols = 3
		rows = 2
	elif len(listofimages) == 2:
		cols = 1
		rows = 2
	elif len(listofimages) == 4:
		cols = 2
		rows = 2
	elif len(listofimages) == 8:
		cols = 4
		rows = 2
	elif len(listofimages) == 3:
		cols = 1
		rows = 3

	thumbnail_width = width//cols
	thumbnail_height = height//rows
	size = thumbnail_width, thumbnail_height

	new_im = Image.new('RGB', (width, height))
	ims = []
	for p in listofimages:
		im = Image.open(urlopen(p))
		im = im.resize(size)

		ims.append(im)
	i = 0
	x = 0
	y = 0
	for col in range(cols):
		for row in range(rows):
			new_im.paste(ims[i], (x, y))
			i += 1
			y += thumbnail_height
		x += thumbnail_width
		y = 0

	return new_im
	

def ImageSetIndivisibleByTwo(width, height, listofimages):
	if len(listofimages)==3:
		image=[]
		image.append(listofimages[0])
		image.append(listofimages[1])
		im2 = ImageSetDivisibleByTwo(width//3,height,image)
		im = Image.open(urlopen(listofimages[2]))
		im = im.resize((int(width*2/3),height))
		new_im = Image.new('RGB', (width, height))
		new_im.paste(im2,(0,0))
		new_im.paste(im,(int(width*1/3),0))
		return new_im

	if len(listofimages) == 5:
		image = []
		for i in range(0,4):
			image.append(listofimages[i])
		im4 = ImageSetDivisibleByTwo(width//2,height,image)
		im = Image.open(urlopen(listofimages[4]))
		im = im.resize((int(width*1/2),height))
		new_im = Image.new('RGB', (width, height))
		new_im.paste(im4,(0,0))
		new_im.paste(im,(int(width*1/2),0))
		return new_im

	if len(listofimages) == 7:
		image = []
		image2 =[]
		for i in range(0,4):
			image.append(listofimages[i])
		im4 = ImageSetDivisibleByTwo(width*2//3,height,image)
		for i in range(4,7):
			image2.append(listofimages[i])
		im3 = ImageSetDivisibleByTwo(width//3,height,image2)
		new_im = Image.new('RGB', (width, height))
		new_im.paste(im4,(0,0))
		new_im.paste(im3,(int(width*2/3),0))
		return(new_im)

