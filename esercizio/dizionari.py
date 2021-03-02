libro_cinzia = {'autore' : 'cinzia', 'titolo': 'python per tutti' }
libro_marco = {'autore' : 'marco', 'titolo': 'bash per tutti' }
libro_sophia = {'autore' : 'sophia', 'titolo': 'biologia per tutti' }
libro_ben = {'autore' : 'ben', 'titolo': 'mille shape di pupu', 'editore' : 'MIT Press', 'pages': {'first':1, 'last':115} }


print(type(libro_cinzia))
print(libro_cinzia['titolo'])
print(libro_ben['autore'])
libro_ben['autore'] = 'Irene'

for key, val in libro_ben.items():
   print("La chiave` {} e il valore e` {}".format(key,val))

print(libro_ben['pages']['first'])