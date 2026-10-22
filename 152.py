x1 = int(input()) 
y1 = int(input()) 
x2 = int(input()) 
y2 = int(input()) 
x = int(input()) 
y = int(input()) 
 
if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2): 
    print("Yes") 
else: 
    print("No") 