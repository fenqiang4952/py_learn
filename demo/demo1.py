s =  {11,22,33,44,55,66,77,88,99,90}
d = {'k1': [],'k2': []}
for i in s:
    if i > 66:
        d['k2'].append(i)
    else:
        d['k1'].append(i)

print(d)
