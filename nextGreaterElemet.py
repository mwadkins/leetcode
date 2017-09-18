def nextGreaterElement (arry):
	for i in range (len(arry)):
		print arry[i]," ",
		curr=-1
		for j in range (i,len(arry)):
			if ((i!=j) and (arry[j]>arry[i])):
				if ((curr==-1) or ((curr!=-1) and (arry[j]<curr))):
					curr=j
		if (curr==-1):
			print curr
		else:
			print arry[curr]

a=[4,5,2,25]
nextGreaterElement(a)
