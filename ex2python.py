a=0
liste = []
b=9
while b!=0:
   if b!=0:
      b=float(input(f"Donnez une valeur {a+1} "))
       liste.append(b)
       a=a+1
   else:
       break

h=0
for l in liste:
  h+=l

moyenne=h/(a-1)
print(f"MOYENNE{moyenne}")