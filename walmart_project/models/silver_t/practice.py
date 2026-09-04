w1= 'listen'
w2= "silent"
Output: True
str1= {}; str2 = {}
i=j=0;
# no need to check the length of the string, as both strings needs to be of same length to be anagrams
while (i != len(w1) or j != len(w2)):
	if i < len(w1) and w1[i] in str1:
		str1[w1[i]] += 1
		i += 1
	else:
		str1[w1[i]] = 1
		i += 1
	

	if j < len(w2) and w2[j] in str2:
			str2[w2[j]] += 1
			j += 1
	else:
		str2[w2[j]] = 1
		j += 1

