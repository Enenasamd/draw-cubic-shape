import numpy as np
printer=lambda s:print(' ' if s==0 else '*',end='' )
def cubic(hight):
	 ones=[]
	 up=int((2**-0.5)*hight)
	 cube=np.zeros((2*up+hight+1,2*up+hight+1))
	 for j in range(hight):
	 	ones.append((j+up,0))
	 	ones.append((j+up,2*up))
	 	ones.append((j+2*up,up))
	 for j in range(up):
	 	ones.append((j+up,j))#
	 	ones.append((j,up-j))#
	 	ones.append((j+up+hight,j))#
	 	ones.append((j,up+j))#
	 	ones.append((2*up+hight-j,up+j))
	 	ones.append((j+up,2*up-j))
	 	ones.append((j+up,0))
	 	ones.append((j+up,2*up))
	 for index in ones:	 	
	 	cube[*index]=1
	 for row in cube:
	 	for val in row:
	 		printer(val)
	 	print('')
cubic(10)