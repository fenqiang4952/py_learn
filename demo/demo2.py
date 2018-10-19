li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", "aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}

l = []

li = [x.strip() for x in li]
tu = tuple([x.strip() for x in tu])

print(tu)