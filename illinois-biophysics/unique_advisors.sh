grep "div class='header'>" -A 1 students.html > temp01_advisors
sed -i -e 's/--//g' temp01_advisors
sed -i -e 's/strong//g' temp01_advisors
sed -i -e 's/header//g' temp01_advisors
sed -i -e 's/class//g' temp01_advisors
sed -i -e 's/div//g' temp01_advisors
sed -i -e 's/[< =>]//g' temp01_advisors
sed -i -e 's/\(strong\|div\|class\|header\)//g' temp01_advisors

sed "s/['\"]//g" temp01_advisors > temp02_advisors

echo "
t1_ad=[]
f=open('temp02_advisors','rb')
for line in f:
	if (len(line)>2):
		t1_ad.append(line)

t2_ad=[]
for item in t1_ad:
	cols=item.strip('\n').split('/')
	if (len(cols)>1):
		for i in range(len(cols)):
			t2_ad.append(cols[i])
	else:
		t2_ad.append(cols[0])

t2_ad.remove('Nair,Satish')
t2_ad.remove('Maslov,Sergei')

ad=set(t2_ad)
for item in ad:
	print item
" > temp_ad.py

ipython temp_ad.py > unique_advisors
rm temp*
