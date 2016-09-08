def merge(arr,low,mid,high):
	# left is arr[low,mid]
	# right is arr[mid+1,high] inclusive notation for both
	nleft = mid - low + 1
	nright = high - mid 
	left = [0]*nleft
	right = [0]*nright

	for i in range(low,mid+1):
		left[i-low] = arr[i]
	for j in range(mid+1,high+1):
		right[j-mid-1]=arr[j]

	k=low
	lit = 0
	rit = 0

	while k<=high and lit<nleft and rit <nright:
		if left[lit]<=right[rit]:
			arr[k]=left[lit]
			lit+=1

		elif left[lit] > right[rit]:
			arr[k]=right[rit]
			rit+=1
		k+=1

	while lit<nleft:
		arr[k]=left[lit]
		k+=1
		lit+=1

	while rit<nright:
		arr[k]=right[rit]
		k+=1
		rit+=1







def mergesort(arr,low,high):
	if low < high:
		mid = (low + high)/2
		mergesort(arr,low,mid)
		mergesort(arr,mid+1,high)
		merge(arr,low,mid,high)

def sort(arr):
	print arr
	mergesort(arr,0,len(arr)-1)
	print arr





def main():
	arrs=[
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
