d={}
res={}
d["name"]=input('Enter your name : ')
d["assignment"]=list(map(float, input('Enter the assignment marks : ').split()))
d["test"]=list(map(float, input('Enter the test marks : ').split()))
d["lab"]=list(map(float, input('Enter the lab marks : ').split()))

avg = 0.1*(sum(d["assignment"])/len(d["assignment"]))+0.7*(sum(d["test"])/len(d["test"]))+0.2*(sum(d["lab"])/len(d["lab"]))

if avg>=90:
	ch="A"
elif avg>=80:
	ch="B"
elif avg>=70:
	ch="C"
elif avg>=60:
	ch="D"
else:
	ch='Fail'
	
print('Average marks of',d["name"],'is',avg)
print('Letter Grade of',d["name"],'is',ch)


