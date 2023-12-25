def selectionSort(list, key=lambda sortBasedOn: sortBasedOn, reversed=False, cmp=lambda x, y: x < y, startIndex = 0):
	
	if startIndex == len(list) - 1:
		return list
	indexToChange = startIndex
	for index in range(startIndex, len(list)):
		if not reversed:
			if cmp(key(list[index]), key(list[indexToChange])):
				indexToChange = index
		else:
			if not cmp(key(list[index]), key(list[indexToChange])):
				indexToChange = index
	list[startIndex], list[indexToChange] = list[indexToChange], list[startIndex]
	startIndex += 1
	return selectionSort(list, key, reversed, cmp, startIndex)
			
def shakeSort(list, key=lambda sortBasedOn: sortBasedOn, reversed=False, cmp=lambda x, y: x < y, start=True):
	sorted = True
	if not reversed:
		if start == True:
			for index in range(0, len(list) - 1):
				if cmp(key(list[index]), key(list[index + 1])):
						list[index], list[index + 1] = list[index + 1], list[index]
						sorted = False
		else:
			for index in (range(0, len(list) - 1)):
				if cmp(key(reversed(list)[index]), key(reversed(list)[index + 1])):
					list[index], list[index + 1] = list[index + 1], list[index]
					sorted = False
	else:
		if start == 0:
			for index in range(0, len(list) - 1):
				if not cmp(key(list[index]) < key(list[index + 1])):
					list[index], list[index + 1] = list[index + 1], list[index]
					sorted = False
		else:
			for index in (range(0, len(list) - 1)):
				if not cmp(key(reversed(list)[index]), key(reversed(list)[index + 1])):
					list[index], list[index + 1] = list[index + 1], list[index]
					sorted = False
	if sorted:
		return list
	else:
		return shakeSort(list, key, reversed, cmp, not start)



list = [2, 3, 4, 5, 8, 3, 1, 45, 23]
list1 = ["dsad", "dsads", "gfgfd", "Hfghgf"]
print(shakeSort(list))