def abbrev_name(name):
   parts=name.split(" ") 
   return (parts[0][0].upper()+ '.'+parts[1][0].upper())

print(abbrev_name("sam harris"))
print(abbrev_name("patrick feneey"))

   
