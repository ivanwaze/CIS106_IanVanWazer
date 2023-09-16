#input phase
ppsh = float(input( "Enter the price per share"))  
csp = float(input( "Enter the current stock price"))
quant = float(input( "Enter the quantity of shares"))
#processing phase
valu = (csp - ppsh) * quant
#output phase
print("The value of the stock is", valu)