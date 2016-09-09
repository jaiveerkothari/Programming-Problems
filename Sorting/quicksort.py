def partition(arr,left,right):
	pivot=left
	lptr=left+1
	rptr=right

	done=False
	while not done:

		while lptr<=rptr and arr[lptr]<=arr[pivot]:
				lptr+=1

		while lptr<=rptr and arr[rptr]>=arr[pivot]:
				rptr-=1

		if rptr < lptr:
			done = True
		else:
			temp=arr[lptr]
			arr[lptr]=arr[rptr]
			arr[rptr]=temp

	temp=arr[rptr]
	arr[rptr]=arr[pivot]
	arr[pivot]=temp

	return rptr

def quicksort(arr,left,right):
	if left < right:
		mid = partition(arr,left,right)
		quicksort(arr,left,mid-1)
		quicksort(arr,mid+1,right)


def sort(arr):
	print arr
	quicksort(arr,0,len(arr)-1)
	print arr



def main():
	arrs=[
		[1,2,3,4,5,6,7],
		[1,4,56,3,7,8],
		[],
		[1],
		[2,1],
		[9,8,7],
		[1,1,1,1,1,1],
		[4,4]
		]

	for a in arrs:
		sort(a)



main()