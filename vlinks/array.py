infile=open("vlinks.txt","r");
ofile=open("output","w");

ofile.write("[");
for x in infile:
    ofile.write("\""+x[:-1]+"\",\n");
ofile.seek(ofile.tell()-3);
ofile.write("]");
