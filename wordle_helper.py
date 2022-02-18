# -*- coding: utf-8 -*-
"""wordle-helper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1txUwXK91xaziTHKjVYCA5jmE1FIEeF9k
"""

import pandas as pd

words = pd.read_csv('https://raw.githubusercontent.com/atorr5555/words/main/words', header=None, names=['palabra'])
words

mantener = [len(elem) == 5 for elem in words.palabra]

words_5 = words[mantener]
words_5

def normalizar(s):
  reemplazos = (
    ("á", "a"),
    ("é", "e"),
    ("í", "i"),
    ("ó", "o"),
    ("ú", "u"),
    ("ä", "a"),
    ("ë", "e"),
    ("ï", "i"),
    ("ö", "o"),
    ("ü", "u")
  )
  for a, b in reemplazos:
    s = s.lower().replace(a, b)
  return s

words_5['palabra'] = words_5['palabra'].apply(normalizar)
words_5

frecuencias = {'a': 12.53,
               'b': 1.42,
               'c': 4.68,
               'd': 5.86,
               'e': 13.68,
               'f': 0.69,
               'g': 1.01,
               'h': 0.7,
               'i': 6.25,
               'j': 0.44,
               'k': 0.02,
               'l': 4.97,
               'm': 3.15,
               'n': 6.71,
               'ñ': 0.31,
               'o': 8.68,
               'p': 2.51,
               'q': 0.88,
               'r': 6.87,
               's': 7.98,
               't': 4.63,
               'u': 3.93,
               'v': 0.9,
               'w': 0.01,
               'x': 0.22,
               'y': 0.9,
               'z': 0.52}

def suma_frecuencias(s):
  sum = 0.0
  for car in s:
    sum += frecuencias[car]
  return sum

words_5['frecuencias'] = words_5['palabra'].apply(suma_frecuencias)

words_5 = words_5.sort_values(by=['frecuencias'], ascending=False).reset_index().drop(columns=['index'])
words_5

def verde(s, a, i):
  return s[i] == a

def amarillo(s, a):
  return a in s

def gris(s, a):
  return not (a in s)

def muestra(l):
  i = 0
  print('Recomendaciones')
  for elem in l:
    print(str(i) + '.- ' + elem)
    i += 1

def duplicado(s, a, res_parcial, res_lista):
  count_res = 0
  for c in res_parcial:
    if c == a:
      count_res += 1
  
  count_am = 0
  for tup in res_lista:
    if tup == (a, 'a'):
      count_am += 1
  
  count = 0
  for c in s:
    if c == a:
      count += 1
    if count > (count_am + count_res):
      return False
  return True

resultado_parcial = ['-', '-', '-', '-', '-']
for i in range(6):
  recomendacion = words_5['palabra'].head().tolist()
  muestra(recomendacion)
  seleccion = int(input('Seleccione una palabra: '))
  resultado = input('Ingrese el resultado (iniciales de los colores): ')
  if resultado == 'vvvvv':
    print('Palabra correcta: ' + recomendacion[seleccion])
    break
  mantener = [elem != recomendacion[seleccion] for elem in words_5.palabra]
  words_5 = words_5[mantener]
  res_lista = [
      (recomendacion[seleccion][0], resultado[0]),
      (recomendacion[seleccion][1], resultado[1]),
      (recomendacion[seleccion][2], resultado[2]),
      (recomendacion[seleccion][3], resultado[3]),
      (recomendacion[seleccion][4], resultado[4])
  ]
  
  for j in range(5):
    if res_lista[j][1].lower() == 'v':
      resultado_parcial[j] = res_lista[j][0]
      mantener = [verde(elem, res_lista[j][0], j) for elem in words_5.palabra]
    elif res_lista[j][1].lower() == 'a':
      mantener = [amarillo(elem, res_lista[j][0]) for elem in words_5.palabra]
    else:
      if not ((res_lista[j][0], 'a') in res_lista or (res_lista[j][0], 'v') in res_lista):
        mantener = [gris(elem, res_lista[j][0]) for elem in words_5.palabra]
      else:
        mantener = [duplicado(elem, res_lista[j][0], resultado_parcial, res_lista) for elem in words_5.palabra]
    words_5 = words_5[mantener]