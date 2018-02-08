height = 126
width = 125

count = 0
unitCells = height * width
fullWidth = height
fullHeight = width

hPartials = 0
pwidth = width - 1
for i in range(pwidth,1,-1):
    hPartials += (i * height)
    
vPartials = 0
pheight = height - 1
for i in range(pheight,1,-1):
    vPartials += (i * width)
    
#print hPartials, vPartials    
    
mysum = unitCells + hPartials + vPartials + height + width + ((height - 1) * (width - 1)) + 1

print mysum
    
