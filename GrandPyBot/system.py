#!/usr/bin/python3
# -*- coding: utf-8 -*-q

from GrandPyBot.api_google import Api_google
from GrandPyBot.api_wiki import Api_wiki
import requests, json, random

class System:
    """Core class."""

    def __init__(self, question):
        self.data = {"question": question,
        "wiki_call": "",
        "wiki_answ": {},
        "maps_call": [],
        "maps_answ": {}}

    def questionning(self):
        #Main function. Actived from view.py
        self.parse_question()
        self.google_caller()
        self.wiki_caller()
        data = self.data
        return data

    def parse_question(self):
        #Change string to list.
        stop_word = ["a","abord","absolument","afin","ah","ai","aie","ailleurs","ainsi","ait","allaient","allo","allons","allô","alors","anterieur","anterieure","anterieures","apres","après","as","assez","attendu","au","aucun","aucune","aujourd","aujourd'hui","aupres","auquel","aura","auraient","aurait","auront","aussi","autre","autrefois","autrement","autres","autrui","aux","auxquelles","auxquels","avaient","avais","avait","avant","avec","avoir","avons","ayant","b","bah","bas","basee","bat","beau","beaucoup","bien","bigre","boum","bravo","brrr","c","car","ce","ceci","cela","celle","celle-ci","celle-là","celles","celles-ci","celles-là","celui","celui-ci","celui-là","cent","cependant","certain","certaine","certaines","certains","certes","ces","cet","cette","ceux","ceux-ci","ceux-là","chacun","chacune","chaque","cher","chers","chez","chiche","chut","chère","chères","ci","cinq","cinquantaine","cinquante","cinquantième","cinquième","clac","clic","combien","comme","comment","comparable","comparables","compris","concernant","contre","couic","crac","d","da","dans","de","debout","dedans","dehors","deja","delà","depuis","dernier","derniere","derriere","derrière","des","desormais","desquelles","desquels","dessous","dessus","deux","deuxième","deuxièmement","devant","devers","devra","different","differentes","differents","différent","différente","différentes","différents","dire","directe","directement","dit","dite","dits","divers","diverse","diverses","dix","dix-huit","dix-neuf","dix-sept","dixième","doit","doivent","donc","dont","douze","douzième","dring","du","duquel","durant","dès","désormais","e","effet","egale","egalement","egales","eh","elle","elle-même","elles","elles-mêmes","en","encore","enfin","entre","envers","environ","es","est","et","etant","etc","etre","eu","euh","eux","eux-mêmes","exactement","excepté","extenso","exterieur","f","fais","faisaient","faisant","fait","façon","feront","fi","flac","floc","font","g","gens","h","ha","hein","hem","hep","hi","ho","holà","hop","hormis","hors","hou","houp","hue","hui","huit","huitième","hum","hurrah","hé","hélas","i","il","ils","importe","j","je","jusqu","jusque","juste","k","l","la","laisser","laquelle","las","le","lequel","les","lesquelles","lesquels","leur","leurs","longtemps","lors","lorsque","lui","lui-meme","lui-même","là","lès","m","ma","maint","maintenant","mais","malgre","malgré","maximale","me","meme","memes","merci","mes","mien","mienne","miennes","miens","mille","mince","minimale","moi","moi-meme","moi-même","moindres","moins","mon","moyennant","multiple","multiples","même","mêmes","n","na","naturel","naturelle","naturelles","ne","neanmoins","necessaire","necessairement","neuf","neuvième","ni","nombreuses","nombreux","non","nos","notamment","notre","nous","nous-mêmes","nouveau","nul","néanmoins","nôtre","nôtres","o","oh","ohé","ollé","olé","on","ont","onze","onzième","ore","ou","ouf","ouias","oust","ouste","outre","ouvert","ouverte","ouverts","o|","où","p","paf","pan","par","parce","parfois","parle","parlent","parler","parmi","parseme","partant","particulier","particulière","particulièrement","pas","passé","pendant","pense","permet","personne","peu","peut","peuvent","peux","pff","pfft","pfut","pif","pire","plein","plouf","plus","plusieurs","plutôt","possessif","possessifs","possible","possibles","pouah","pour","pourquoi","pourrais","pourrait","pouvait","prealable","precisement","premier","première","premièrement","pres","probable","probante","procedant","proche","près","psitt","pu","puis","puisque","pur","pure","q","qu","quand","quant","quant-à-soi","quanta","quarante","quatorze","quatre","quatre-vingt","quatrième","quatrièmement","que","quel","quelconque","quelle","quelles","quelqu'un","quelque","quelques","quels","qui","quiconque","quinze","quoi","quoique","r","rare","rarement","rares","relative","relativement","remarquable","rend","rendre","restant","reste","restent","restrictif","retour","revoici","revoilà","rien","s","sa","sacrebleu","sait","sans","sapristi","sauf","se","sein","seize","selon","semblable","semblaient","semble","semblent","sent","sept","septième","sera","seraient","serait","seront","ses","seul","seule","seulement","si","sien","sienne","siennes","siens","sinon","six","sixième","soi","soi-même","soit","soixante","son","sont","sous","souvent","specifique","specifiques","speculatif","stop","strictement","subtiles","suffisant","suffisante","suffit","suis","suit","suivant","suivante","suivantes","suivants","suivre","superpose","sur","surtout","t","ta","tac","tant","tardive","te","tel","telle","tellement","telles","tels","tenant","tend","tenir","tente","tes","tic","tien","tienne","tiennes","tiens","toc","toi","toi-même","ton","touchant","toujours","tous","tout","toute","toutefois","toutes","treize","trente","tres","trois","troisième","troisièmement","trop","très","tsoin","tsouin","tu","té","u","un","une","unes","uniformement","unique","uniques","uns","v","va","vais","vas","vers","via","vif","vifs","vingt","vivat","vive","vives","vlan","voici","voilà","vont","vos","votre","vous","vous-mêmes","vu","vé","vôtre","vôtres","w","x","y","z","zut","à","â","ça","ès","étaient","étais","était","étant","été","être","ô"]
        maps_call = self.data["question"].replace("\'", " ").replace("?", "").replace(".", "").replace("!", "")
        maps_call = maps_call.split(" ", -1)
        for el in maps_call:
            if el == '':
               maps_call.remove(el)
        maps_call = self.cut_from_last(maps_call, stop_word)
        for el in stop_word:
            maps_call = self.clean_list(el, maps_call)
        maps_call = " ".join(maps_call)
        self.data["maps_call"] = maps_call

    def cut_from_last(self, list1, list2):
        #Keep end from last stop word.
        index = 0
        count = 0
        stop_words = 0
        for el1 in list1:
            for el2 in list2:
                if el1 == el2:
                    stop_words += 1
        if stop_words > 1:
            for el1 in list1:
                for el2 in list2:
                    if el1 == el2:
                        index += 1
                        if index + 1 == stop_words:
                            del list1[0: count]
                            return list1
            count += 1
        else:
            return list1

    def clean_list(self, mot, list_old):
        #Remove stop word from list.
        list_new = []
        for el in list_old:
            if el != mot:
                list_new.append(el)
        return list_new

    def google_caller(self):
        #Call Api_google class.
        memory = ["Je connais bien cet endroit mon petit chat. Il se situe au ", \
                    "GrandPy à toujours la solution! Tu trouveras l'objet de tes désirs au, ", \
                    "Ne t'inquiète pas ma caille, je sais où c'est... "]
        data = Api_google.search(self.data["maps_call"])
        if data["status"] == "OK":
            del data["status"]
            self.data["wiki_call"] = data["wiki_call"]
            del data["wiki_call"]
            data["formatted_address"] = memory[random.randrange(3)] + data["formatted_address"]
            self.data["maps_answ"] = data
            self.data["maps_call"] = 1
        elif data["status"] == "ZERO_RESULTS":
            self.data["maps_answ"] = "Oula! Je ne connais pas l'adresse de cet\
                                        établissement. Quelle déception !!!"
            self.data["maps_call"] = 2
        else:
            self.data["maps_answ"] = "Que me demandes tu mon petit? Tu sais avec\
                                        papy il faut bien expliquer!"
            self.data["maps_call"] = 3

    def wiki_caller(self):
        #Call Api_wiki class
        if self.data["maps_call"] == 1:
            data = Api_wiki.find_pageid(self.data["wiki_call"])
            self.data["wiki_answ"] = Api_wiki.page_info(data)