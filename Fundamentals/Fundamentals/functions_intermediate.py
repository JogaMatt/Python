x = [ [5,2,3], [10,8,9] ] 

x[1][0] = 15
print(x)


students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)


z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)


mkfighters = [
        {'first_name': 'Liu', 'last_name': 'Kang'},
        {'first_name': 'Kung', 'last_name': 'Lao'},
        {'first_name': 'Sonya', 'last_name': 'Blade'},
        {'first_name': 'Jax', 'last_name': 'Briggs'}
    ]

def iterateDictionary(listInput):
    # print(listInput)
    for kombatant in listInput:
        for key, val in kombatant.items():
            print(f"{key}-{val}")

iterateDictionary(mkfighters)


def iterateDictionary2(keyInput ,listInput):
    for kombatant in listInput:
        print(kombatant[keyInput])

iterateDictionary2('first_name' ,mkfighters)
iterateDictionary2('last_name' ,mkfighters)


pokemon = {
    'generation': ['One', 'Two', 'Three', 'Four', 'Five'],
    'region': ['Kanto', 'Johto', 'Hoenn', 'Sinnoh', 'Unova']
}

def printInfo(dictionaryInput):
    for key, val in dictionaryInput.items():
        print(len(val),key.upper())
        for name in val:
            print(name)


printInfo(pokemon)