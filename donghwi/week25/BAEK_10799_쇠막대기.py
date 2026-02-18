S = list(input())
st = []
count = 0

for i in range(len(S)):
	if S[i] == '(':
		st.append('(')
	else:
		if S[i-1] == '(':
			st.pop()
			count += len(st)
		
		else:
			st.pop()
			count += 1

print(count)