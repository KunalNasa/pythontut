"""
dict = {"kannu":"wings", "akash":"mutton", "mummy":"kc", "papa":{"breakfast":"chicken", "lunch":"mutton", "dinner":"fish"}}
dict["mama"] = "kfc"
print(type(dict))
print(dict["papa"]["lunch"])
del dict["mama"]
d2 = dict.copy()
d2 = dict.keys()
d2 = dict.get("kannu")
d2 = dict.values()
dict.clear()
print(d2)
"""
dict = {"set":"collection of well defined objects", "locus":"path traced by given points under a given condition", "tiger":"an animal", "dove":"a bird"}
print("search the meaning of your word")
search = input()
print(dict[search])

