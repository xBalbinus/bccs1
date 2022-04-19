import pickle
 

def get_title_dict():
    f=open('./moviedict.pickled','rb')
    d=pickle.load(f)
    return d

d = get_title_dict()

def reverseDict(d):
    actorsdict = {}
    for movie in d.keys():
        for actor in d[movie]:
            actorsdict.setdefault(actor, [])
    for movie in d.keys():
        for actor in d[movie]:
            actorsdict[actor].append(movie)
    return actorsdict

a = reverseDict(d)

command = input()
if command == "owen_wilson":
        #Search if key contains value, if not move on
        for i in a["Owen Wilson"]:
            print(i)
if command == "num_actors":
        print(len(a.keys()))
if command == "bradley_and_jennifer":
        bjlist = []
        for i in a["Bradley Cooper"]:
            for j in a["Jennifer Lawrence"]:
                if j == i:
                    bjlist.append(j)
        for i in bjlist:
            print(i)
if command == "most_productive_actors":
        #Find the largest amount of films any actor has appeared in
        #Print actor names
        maxcounter = 0
        for actor in a.keys():
            if len(a[actor]) > maxcounter:
                maxcounter = len(a[actor])
        for actor in a.keys():
            if len(a[actor]) == maxcounter:
                print(actor) 
                
    
