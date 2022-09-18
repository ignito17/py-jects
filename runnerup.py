n = int(input()) 
st = list(set(map(int, input().split())))

st.sort(reverse = True)
print(st[1])