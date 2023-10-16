p = float(input("Enter principle"))
r = float(input("Enter rate of interest"))
totint = 0.0
print("Year    Beginning Bal      End Bal")

for x in range (1, 6, 1):
    i = p * r
    totint = totint + i
    endbal = p + i
    print (x,"", p, "      ",endbal)
    p = endbal

print(" Total interest earned", totint)