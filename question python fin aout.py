#!/usr/bin/env python
# coding: utf-8

# In[7]:


def polynome(x):
    x2 = x*x
    return x2 + x - 5


# In[8]:


polynome(10)


# In[9]:


from math import log
def log_base (x, base=10) :
    return log (x) / log(base)

y = log_base (1000)     # identique à y = log_base (1000, 10)
z = log_base (1000, 2)  # logarithme en base deux
y,z


# In[13]:


def calcul(x) :
    y = x**2
    z = x + y
    return a

print(a) # déclenche une exeption


# In[18]:


a = 2

def test() :
    global a
    a = 3
    return print("intérieur de test", a)
    
test()
print("après test", a)


# In[22]:


def recursive(x) :
    if x / 2 < 1 :
        print("je ne m'appelle pas pour x =",x)
        return 1
    else :
        print("je m'appelle pour x =",x)
        return recursive (x/2) + 1

recursive(10)


# In[28]:


s1 = "Du passe faisons table rase"
l1 = [i for i in s1]
l2 = s1.split("as")
l3 = s1.split()
print(l1[0], l1[1], l1[2], l1[3])
print(l2)
print(l3)


# In[30]:


l1 = ['H', 'e', 'l', 'l', 'o', ' ', 'W']
l2 = ['Du', 'passe', 'faisons', 'table', 'rase']
s1 = "".join(l1)
s2 = " ".join(l2)

print(s1)
print(s2)


# In[31]:


s1 = "Faisons table rase"
s2 = s1[:8].lower() + s1[8:13].upper()
print(s2)


# In[33]:


s1 = "Ce texte contient deux fois le mot texte."
print(s1.find('texte', 0))
print(s1.find('texte', 4))
print(s1.find('texte', 36))

s1 = "Ce texte contient deux fois le mot texte"
max = 0
while max > -1:
    max = s1.find('texte', max+1)
    print(max)


# In[43]:


s1 = "Le prix est de deux euros." #Partie complète
if 'euros' in s1: 
    i = s1.index('euros')
    s2 = s1[:i-5] + '$' + s1[i-5:i]
    j  = s2.find('deux')
    s3 = s2[:j] + '2.15' + s2[j+4:]
    print(s3)


# In[45]:


i = s1.index('euros')            #Partie décomposée
s2 = s1[:i-5] + '$' + s1[i-5:i]
j  = s2.find('deux')
s3 = s2[:j] + '2.15' + s2[j+4:]
print(i)
print(s2)
print(j)
print(s3)


# In[48]:


s1 = 'Le prix est de deux euros'
s2 = s1.replace('deux euros', '$2.15')
print(s2)


# In[49]:


s = '300 seulement ?'
l = s.split()
for mot in l:
    if mot.isalpha():
        print('mot')
    if mot.isnumeric():
        print('nombre')
    if not mot.isalnum():
        print('?')


# In[50]:


from re import findall
s = "Le PIB de l'Argentine baisse depuis 3 ans"
l1 = findall('[A-Z][a-z]+',s)
l2 = findall('[a-zA-Z]*[iI][a-zA-Z]*',s)
print(l1)
print(l2)


# In[51]:


from re import findall
motif = '0[1-9](?:[\s\.]?[0-9]{2}){4}'
n1 = "0678828383"
n2 = "09.34.67.12.11"
n3 = "03 11 23 20 38,"
n4 = "03 11 23 20,"
n5 = "03.11 23 2038"
n6 = "03-23-20-20-38"
s = n1+n2+n3+n4+n5+n6
print(findall(motif, s))


# In[55]:


from re import sub
s = 'Un texte <strong>HTML<strong/>avec des balises'
s += ' et même<script type="text/javascript">'
s += 'var i = 5 ;</script> du javascript dedans.'
s1 = sub('<[a-z]*>', '', s)
print(s1)


# In[56]:


from re import sub
s = 'Un texte <strong>HTML<strong/>avec des balises'
s += ' et même<script type="text/javascript">'
s += 'var i = 5 ;</script> du javascript dedans.'
s1 = sub('<.*>', '', s)
s2 = sub('<[a-z\\/"=\s]*>', '', s)
s3 = sub('<[^>]*>', '', s)
print(s1)
print(s2)
print(s3)


# In[4]:


# 1. Ecrire une fonction hascap(s) qui renvoie tout les mots de la chaîne
# s commençant par une majuscule.
# ØPour ce faire utiliser la fonction ord() pour obtenir le code ASCII des lettres
# (Les lettres majuscule ont un code allant de 65 à 90).
s = "Vive la Vie de Rêve que je mène à Simplon"
l = s.split()
def hascap(a) :
    for mot in a :
        if ord(mot[0])>=65 and ord(mot[0])<=90:
            print(mot)

hascap(l)


# In[23]:


# 2. Proposer une fonction inflation(s) qui va doubler la valeur de tout
# les nombre dans la chaine s. Exemple : « Le prix est de 27 euros »
# devient « Le prix est de 54 euros ».
# ØUtiliser la fonction enumerate() pour lancer une boucle for (Taper dans
# Google « enumerate boucle for ».)
list1 = "Le prix est de 27 euros"
list2 = list1.split()

def inflation(list1) :
    for x,mot in enumerate(list2):
        if mot.isnumeric():
             list2[list1]=str(int(mot)*2)
result = " ".join(list2)
                
return print(result)
             
  
        


# s = "Onze ans déjà que cela passe vite Vous "
# s += "vous étiez servis simplement de vos armes la "
# s += "mort n‘éblouit pas les yeux des partisans Vous "
# s += "aviez vos portraits sur les murs de nos villes "
# l = s.split()
# for mot in l:
# if len(mot)
# print(len(mot))

# In[13]:


s = "Onze ans déjà que cela passe vite Vous "
s += "vous étiez servis simplement de vos armes la "
s += "mort n‘éblouit pas les yeux des partisans Vous " 
s += "aviez vos portraits sur les murs de nos villes" 
l =[]
LEL=""
T=s.split()
for mot in T:
    if len(mot) + len(LEL) >24:
        l.append(LEL)
        LEL = mot + " "
    else:
        LEL+=mot + " "

l.append(LEL)
print(l)


# In[37]:


#4.Proposer un programme qui renvoie la liste de tout les nombres 
#(ycompris décimaux et négatifs) d’une chaîne de caractères.
#A tester sur la chaîne :
#Les 2 maquereaux valent 6.50 euros »

import re

a = "Les 2 marquereaux valent 6,50 euros"
x1 = '[\d+.,]*\d+'

print(re.findall(x1,a))


# In[2]:


#5 Proposer une fonction arrondi(s) qui dans la chaîne s troncature et tout les nombre décimaux.
# On autorise les nombres négatifs.
# Pour ce faire, vous avez la possibilité d’utiliser 
#: Ødes () pour désigner des blocs de données dans l’expression rationnelle.
# Øpour remplacer chacun des blocs l’expression est r’\1_\2_’
import re 

p = "il a 4.25 euros sur son compte 5.98"

def test(s):
    s= re.sub("[.,][0-9]+", "",s)
    print(s)


test(p)


# In[ ]:




