__author__ = 'amine'

def tri_algorithm(table) :
    i = 0
    while i < len(table) :
        j=i+1
        while j < len(table):
            if table[i] > table[j]:
               temporalValue = table[i]
               table[i] = table[j]
               table[j] = temporalValue
            j=j+1
        i=i+1

integerTable = [1,8,6,9,2]
tri_algorithm(integerTable)
print(integerTable)



