import pickle
import requests

# pickling a python object

# NBA = ["warriors", "maverics", "suns", "lakers", "celtics"]
# file = "myteams.pkl"
# with open(file, 'wb') as teams:
#  pickle.dump(NBA,teams)


"""
file = 'myteams.pkl'
fileobj = open(file, 'rb')
myteams = pickle.load(fileobj)
print(myteams)

"""
# print(pickle.HIGHEST_PROTOCOL)
# print(pickle.DEFAULT_PROTOCOL)

# Players = ["Kobe", "Curry", "Thompson", "James"]
# filename = "players.pkl"
# with open("players.pkl", "wb") as f:
#  pickle.dump(Players, f)
#
# opening = "Players.pkl"
# openfile = open(opening,"rb")
# printdata = pickle.load(openfile)
# print(printdata)


# ----------EXERCISE-10---------

r =  requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
# with open("filename.txt" ,"wb") as f:
#  f.write(r.content)

read = r.text.split("\n")
ls = [[i] for i in read if len(i) != 0]


newfile = "names.pkl"
with open("names.pkl", 'wb') as k:
 pickle.dump(ls, k)

final = open("names.pkl", "rb")
myfile = pickle.load(final)
print(myfile)
