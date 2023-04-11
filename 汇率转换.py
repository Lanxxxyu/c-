m=input()
if m[0:3] in ["RMB"]:
   m=eval(m[3:])/6.78
   print("USD{:.2f}".format(m))
elif m[0:3] in ["USD"]:
   m=eval(m[3:])*6.78
   print("RMB{:.2f}".format(m))
else:
   print()