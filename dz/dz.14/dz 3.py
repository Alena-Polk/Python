s = "012345363738494"
a = "3"
print("s = " + str(s))
s2 = "".join([i for i in s if i != a])
print("s2 = " + str(s2))