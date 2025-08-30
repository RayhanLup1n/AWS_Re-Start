myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

# Akses values menggunakan looping
for x in myMixedTypeList:
    print(x)
    
print('\t')

# Akses segala hal tentang values dengan looping
for a in myMixedTypeList:
    print("{} is of the data type {}".format(a,type(a)))