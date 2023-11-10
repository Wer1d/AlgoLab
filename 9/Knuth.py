file_path = 'text.txt'  # Replace this with the actual file path
try:
    with open(file_path, 'r') as file:
        file_content = file.read()
        # print(file_content)
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

#file to const
Domain=[]
Thelength=""
m=0 #m=patternlength
n=0 #n=textlength
pattern=""
textinput=""
Domain,Thelength,pattern,textinput=file_content.splitlines()
m,n=(Thelength.split())
m=int(m)
n=int(n)
count=0

#delete space
pattern = pattern.replace(" ", "")
textinput=textinput.replace(" ","")

#DEBUG
# print(m)
# Python3 program for KMP Algorithm
LR=[]
RL=[]
lps=[]

sedddstring=textinput[:len(pattern):]
def KMPSearch(pat, txt,state):
	M = len(pat)
	N = len(txt)
	
	# if (m!=M):
	# 	return("PatternLength doesn't Match")
	# if (n!=N):
	# 	return("TextinputLength doesn't Match")
	# create lps[] that will hold the longest prefix suffix
	# values for pattern
	lps = [0]*M
	j = 0 # index for pat[]

	# Preprocess the pattern (calculate lps[] array)
	lps=computeLPSArray(pat, M, lps)
	if state=="LR":
		print(lps)
    
	i = 0 # index for txt[]
	while (N - i) >= (M - j):
		if pat[j] == txt[i]:
			i += 1
			j += 1

		if j == M:
			if (state=="LR"):
				if((i-j+1)>n):
					LR.append(i-j+1-n)
				else:
					LR.append(i-j+1)
				# print((i-j+1)," : LR")
			if (state=="RL"):
				if (n-(i-j)>n):
					RL.append(n-(i-j)-n)
				else:
					RL.append(n-(i-j))
				# print(n-(i-j)," : RL")
			j = lps[j-1]

		# mismatch after j matches
		elif i < N and pat[j] != txt[i]:
			# Do not match lps[0..lps[j-1]] characters,
			# they will match anyway
			if j != 0:
				j = lps[j-1]
			else:
				i += 1

#preprocessing compute the index that matching with before index
# Function to compute LPS array
def computeLPSArray(pat, M, lps):
	len = 0 # length of the previous longest prefix suffix
	lps[0] = 0 # lps[0] is always 0
	i = 1
	# the loop calculates lps[i] for i = 1 to M-1
	while i < M:
		if pat[i] == pat[len]:
			len += 1
			lps[i] = len
			i += 1
		else:
			# This is tricky. Consider the example.
			# AAACAAAA and i = 7. The idea is similar
			# to search step.
			if len != 0:
				len = lps[len-1]
				# Also, note that we do not increment i here
			else:
				lps[i] = 0
				i += 1
	return(lps)

# Driver code
KMPSearch(pattern,textinput+sedddstring,"LR")
# inversepattern=pattern[::-1]
inversetext=textinput[::-1]
KMPSearch(pattern,inversetext+sedddstring[::-1],"RL")
RL.sort()
print(len(RL)+len(LR))
for i in LR:
	print(i," LR")
for j in RL:
	print(j," RL")