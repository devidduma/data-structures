def countSubString(to_find, text):
	if(len(to_find) > len(text)):
		return 0
	
	is_equal = to_find == text[0:len(to_find)]
	return is_equal + countSubString(to_find, text[1:])

print(countSubString('ab', 'abcdabab'))
# print(countSubString('a', 'abcdababa'))
