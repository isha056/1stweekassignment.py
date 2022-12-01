name="    Isha    "
dots=".........."
# lstrip() method
print(name +dots)
print(name.lstrip()+dots)
print(name.rstrip()+dots)
print(name.strip()+dots)
name="     Simran     kaur     "
dots="............"
print(name.replace(" ","")+dots)
#replace() method
string="She is beautiful and She is good Dancer"
print(string.replace("is","was"))
print(string.replace("is","was",1))
# find() method
string="She is beautiful and She is good Dancer"
is_pos1=string.find("")
is_pos2=string.find("is",is_pos1+1)
print(is_pos2)
#center method
name="Simran"
print(name.center(11,"*"))
