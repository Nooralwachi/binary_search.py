def binary_search(arr, nums, key):
	if len(nums)==1 and key!=nums[0]:
		print(f'The index of the key {key} is -1')
		return
	mid= len(nums)//2
	l=nums[:mid]
	r=nums[mid:]
	if key < nums[mid]:
		binary_search(arr,l, key)
	elif key > nums[mid]:
		binary_search(arr,r, key)
	elif key==nums[mid]:
		print(f'The index of the key {key} is {arr.index(nums[mid])}')
		return


arr = [1, 10, 20, 47, 59, 63, 75, 88, 99]
binary_search(arr,arr, 47)
binary_search(arr,arr, 77)