def reverse(text):
	if(len(text) == 0):
		return
	
	reverse(text[1:])
	print(text[0], end='')

reverse('PYTHON')
