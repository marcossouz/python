fout = open('in.txt', 'w')
print (fout)

line1 = 'This here\'s the wattle,\n'
line2 = 'the emblem of our land.\n'
fout.write(line1) 
fout.write(line2)
fout.close()