#input phase
fix = float(input(" Enter fixed cost"))
ppu = float(input(" Enter price per unit"))
cpu = float(input(" Enter cost per unit"))
#process phase
bep = fix / (ppu - cpu  )
#output phase
print("The break even point is ", bep)