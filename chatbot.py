#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 09:34:40 2020

@author: lucas
"""

import random 
import time

intro = ["Comment allez-vous ?", "Pourquoi venez-vous me voir ?", "Comment s'est passée votre journée ?"]
familly = ["père", "mère", "copain", "copine", "maman", "papa", "ami", "amie"]
responses = ["Comment va votre {}", "La relation avec votre {} vous pose t'elle problème?", "Pourquoi pensez vous en ce moment à votre {}?"]
interogations = ["Pourquoi me posez-vous cette question ?", "Oseriez-vous poser cette question à un humain ?", "Je ne peux malheureusement pas répondre à cette question"]
vague = ["J'entends bien", "je sens une pointe de regret", "Est-ce une bonne nouvelle ?", "Oui, c'est ça le problème", "Pensez-vous ce que vous dites ?", "Hum... Il se peut"]
introReponse = ["Je vais bien merci", "un peu fatigué mais ça va", "la pêche frère"]
humeur = ["fatigué", "forme", "joyeux", "triste", "excité", "colère", "ennuyé", "pas top", "pas bien", "bien", "mal"]
inter = ["ne soyez pas si enervé", "calme-toi frère", "je pense que vous devriez plus prendre de temps pour vous"]



print(intro[random.randint(0, len(intro)-1)])
response = input()
if "toi" in response or "vous" in response:
    print(introReponse[random.randint(0, len(introReponse)-1)]) 
    

time.sleep(1.5)    
print("comment vous sentez-vous ?")
response = input()


while response:

    x = random.randint(1, 5)

    
    for i in humeur:
        if i in response:
            time.sleep(1.5)  
            print("Pourquoi vous sentez vous {} ?".format(i))
            response= input()

    for i in familly:
        if i in response:
            time.sleep(1.5)  
            print(responses[random.randint(0, len(responses)-1)].format(i))
            response = input()
            time.sleep(1.5)
            print("expliquez moi la relation que vous avez avec votre {}".format(i))
            response = input()
            
    if "?" in response:
        time.sleep(1.5)  
        print(interogations[random.randint(0, len(interogations)-1)])
        response = input()
        
    else:
        time.sleep(1.5)  
        print(vague[random.randint(0, len(vague)-1)])
        response = input()
   
        if x == 1:
            time.sleep(1.5)  
            print("Voulez vous arrêter notre conversation ?")
            response = input()
            if response == "oui":
                response = False
            else:
                time.sleep(1.5)  
                print("très bien continuons notre conversation alors, de quoi voulez vous parler ?")
                response = input()
            
    if "!" in response:
        time.sleep(0.5)
        print(inter[random.randint(0, len(inter)-1)])
        response = input()
            
    
    
    
    
    