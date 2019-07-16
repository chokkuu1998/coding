ss=input()
chee=True
if '@' not in ss:
	che=False
if ss.count('@')>1 or ss.count('.')>1 and chee==True:
	chee=False
if len(ss[ss.index('@')+1:ss.index('.')])<4 or ss[ss.index('@')+1:ss.index('.')]!="gmail" and chee==True:
	chee=False
if len(ss[:ss.index('@')])<3 and chee==True:
	chee=False
if ss.endswith('.com')==False and chee==True:
	chee=False
if chee:
	print("YES")
else:
	print("NO")
