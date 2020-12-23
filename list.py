thislist = ["test1","test2","test3"]
print(thislist)
print(thislist[0])
for x in thislist:
	print(x)
if "test2" in thislist:
	print("Yes, test2 is in the list")

print(len(thislist))
thislist.append("Test4")
print(thislist)
