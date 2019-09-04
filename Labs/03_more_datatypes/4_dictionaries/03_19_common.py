'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. For example:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''
dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

k1 = set(dict_1.keys())
k2 = set(dict_2.keys())
k3 = k1.union(k2)

dict_3 = {}

for i in k3:
    dict_3[i] = dict_1.get(i, 0)+ dict_2.get(i, 0)
print(dict_3)

