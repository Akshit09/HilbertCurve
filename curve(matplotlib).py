import matplotlib.pyplot as plt                             #imported matplotlib with a nickname plt
import numpy as np					    #imported numpy with a nickname np
stPt0 = [(220, 220), (260, 220), (220, 260), (260, 260)]    #start point
stPt1 = [(0,0)]						    

def Four_out_of_One(i, Pt0, Pt1):  			   #self explainatory name
	#print Pt0
	oint = []
	if i==0 :                                         #MATHS
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

def caller(level, Pt0, Pt1):				#to create the list of points
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

def main(Pt0, Pt1):					#main function
	for level in range(5):
		if (level>1):
			Pt1 = Pt0
			Pt0 = points
		points = caller(level, Pt0, Pt1)
		for oint in points:
			print (level, oint)
			plt.scatter(oint[0], oint[1])
    			plt.pause(0.05)
if __name__=="__main__":
	main(stPt0, stPt1)
