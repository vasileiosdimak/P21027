from collections import Counter
from random import sample
with open('two_cities_ascii.txt', 'r') as fileinput:
   for line in fileinput:
       line = line.rstrip().lower()
       with open ('newfile_p21027','a') as f:
            f.write(line)
with open ('newfile_p21027','r') as f:
    listl=[]
    for line in f:
        strip_lines=line. strip()
        listli=strip_lines. split()
        m=listl. append(listli)
c = Counter(listl[0])
print (len(c.keys()), "Συνολικά αντικείμενα")
sorted_values = sorted(c.values()) # Sort by values
sorted_dict = {}
for i in sorted_values:
    for k in c.keys():
        if c[k] == i:
            sorted_dict[k] = c[k]
            break
print("Ταξινομημένο dictionary")
print(sorted_dict)
dict_items = sorted_dict.items()
last_10 = list(dict_items)[-10:]
print("ΟΙ ΔΕΚΑ ΔΗΜΟΦΙΛΕΣΤΕΡΕΣ ΛΕΞΕΙΣ ΕΙΝΑΙ:")
print(last_10)
#syndiasmos 2 prwtwn grammatwn
first2 = []
for i in range (len(listl[0])):
    sample_str = listl[0][i]
    first2.append(sample_str[0:2])
count = Counter(first2)
print (len(count.keys()), "Συνολικά αντικείμενα")
sorted_values = sorted(count.values()) # Sort by values
sorted_first2_dict = {}
for i in sorted_values:
    for k in count.keys():
        if count[k] == i:
            sorted_first2_dict[k] = count[k]
            break
#print(sorted_first2_dict, "Ολο το dictiοnary ταξινομημενο")
dict_first2_items = sorted_first2_dict.items()
last_3 = list(dict_first2_items)[-3:]
print(" οι τρεις πρώτοι συνδυασμοί ,των ΔΥΟ πρώτων γραμμάτων ,που αρχίζουν οι περισσότερες λέξεις είναι:")
#ekypwnw ta 3 teleutaia gt to dictionary einai sorted me au3ousa seira sta values
print(last_3)
#syndiasmos 3 prwtwn grammatwn
first3 = []
for i in range (len(listl[0])):
    sample_str = listl[0][i]
    first3.append(sample_str[0:3])
count = Counter(first3)
print (len(count.keys()), "Συνολικά αντικείμενα")
sorted_values = sorted(count.values()) # Sort by values
sorted_first3_dict = {}
for i in sorted_values:
    for k in count.keys():
        if count[k] == i:
            sorted_first3_dict[k] = count[k]
            break
#print(sorted_first3_dict,"Ολο το dictiοnary ταξινομημενο")
dict_first3_items = sorted_first3_dict.items()
last_3 = list(dict_first3_items)[-3:]
print(" οι τρεις πρώτοι συνδυασμοί ,των ΤΡΙΩΝ πρώτων γραμμάτων ,που αρχίζουν οι περισσότερες λέξεις είναι:")
#ekypwnw ta 3 teleutaia gt to dictionary einai sorted me au3ousa seira sta values
print(last_3)

   




        
        
           
           
       
          