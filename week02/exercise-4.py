
source = open('source.txt','r')
destination = open('destination.txt','w')

for line in source:
   destination.write(line)


source.close()
destination.close()
