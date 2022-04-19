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

def extendedDict(a,d):
    #Create new dict
    extendeddict = {}
    #Set actors (first name, last name) as keys
    for actor in a.keys():
        extendeddict.setdefault(actor, [])
    #Create mapping (values) from movie to all actors in each movie
    #Iterate through all movie names per actor
    for key in extendeddict.keys():
        for movie in d.keys():
            if key in d[movie]:
                for collaborator in d[movie]:
                    if collaborator not in extendeddict[key] and collaborator != key:
                        extendeddict[key].append(collaborator)
    return extendeddict

e = extendedDict(a,d)
print(e)


command = input()
if command == "most_collaborators":
        #Search if key contains value, if not move on
        print(list(e.values()).index(max(len(e.values()))))
if command == "kate_and_cate1":
        if "Cate Blanchett" in e["Kate Winslet"]:
            print(True)
        else:
            print(False)
if command == "kate_and_cate2":
        for i in e["Kate Winslet"]:
            if "Cate Blanchett" in e[i]:
                print(True)
        else:
            print(False)