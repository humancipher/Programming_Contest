from math import sqrt

xa,ya,xb,yb,xc,yc = map(int,input().split())

ab = sqrt((xa-xb)**2+(ya-yb)**2)
bc = sqrt((xb-xc)**2+(yb-yc)**2)
ca = sqrt((xc-xa)**2+(yc-ya)**2)
s = (ab+bc+ca)/2

S = sqrt(s*(s-ab)*(s-bc)*(s-ca))

print(S)
