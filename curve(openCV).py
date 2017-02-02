import cv2
import numpy as np
image = cv2.imread('/home/akshit/Pictures/chmod.png', 0)
stPt0 = [(220, 220), (260, 220), (220, 260), (260, 260)]
stPt1 = [(0,0)]

def square(x):

	return (cv2.rectangle(image, (x[0]-2 ,x[1]-2), (x[0]+2, x[1]+2),(255, 255, 255), -1))

def Four_out_of_One(i, Pt0, Pt1):
	#print Pt0
	oint = []
	if i==0 :
		for j in range(0,2):
			oint.append(Pt0[j]+((Pt0[j]-Pt1[j])/2))		
		return (tuple(oint))
	elif i==1 :
		for j in range(0,2):
			oint.append(Pt0[j]-(Pt0[j]-Pt1[j])/2)
		return (tuple(oint))
	elif i==2 :
		oint.append(Pt0[0]-(Pt0[0]-Pt1[0])/2)
		oint.append(Pt0[1]+(Pt0[1]-Pt1[1])/2)
		return (tuple(oint))
	else:
		oint.append(Pt0[0]+(Pt0[0]-Pt1[0])/2)
		oint.append(Pt0[1]-(Pt0[1]-Pt1[1])/2)
		return (tuple(oint))

def caller(level, Pt0, Pt1):
		points = []
		if  level==0:
			points = [i for i in Pt0]
			#print (level,points)
			return points
		elif level==1:
			for point in Pt0:
				for i in range(4):
					points.append(Four_out_of_One(i,point, Pt1[0]))
			#print (points)
			return points
		else:
			for j in range(1, len(Pt0)):
				for i in range(4):
					points.append(Four_out_of_One(i,Pt0[j-1], Pt1[j/4]))
				#print points
			return points

def main(Pt0, Pt1):
	for level in range(5):
		if (level>1):
			Pt1 = Pt0
			Pt0 = points
		points = caller(level, Pt0, Pt1)
		for oint in points:
			print (level, oint)
			image = square(oint)
			cv2.imshow('image', image)
			cv2.waitKey(200)
			cv2.destroyAllWindows()
if __name__=="__main__":
	main(stPt0, stPt1)
