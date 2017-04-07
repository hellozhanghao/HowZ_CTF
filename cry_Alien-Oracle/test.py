knownBytes=[84,104,101,83,104,97,114,107,125,60,45,45,102,108,97,103]
knownBytes2=[45,45,62,107,111,112,105,67,84,70,123,82,101,121,111,110]
result=''
for k in knownBytes2:
    result+=chr(k)
for k in knownBytes:
    result+=chr(k)

print(result)
