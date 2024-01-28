di = {
  "s": { "Name": "Henry",
          "Poke": "Rattata",
          "Lv":"50",
          "Ntr":"Hasty",
          "Tra1":"HP",
          "Tra2": "Spd",
          "Ab": "Runaway",
          "Mv1": "Acid Spray",
          "Mv2": "Aromatherapy",
          "Mv3": "Burning Jealousy",
          "Mv4": "Behemoth Bash",
          "IVs":
        ["10","11","12","13","14"]
       }
}
#p = input("Person?")

print(di["s"]["Poke"])
print("Level:", di["s"]["Lv"])
print(di["s"]["Ntr"],"Nature")
print("Ability:",di["s"]["Ab"])
print("EVs: 252",di["s"]["Tra1"],"/","252",di["s"]["Tra2"])
print("IVs:",di["s"]["IVs"][0],"HP /",di["s"]["IVs"][1],"Atk /",di["s"]["IVs"][2],"Def /",di["s"]["IVs"][3],"SpA /",di["s"]["IVs"][4],"SpD")
print("-",di["s"]["Mv1"])
print("-",di["s"]["Mv2"])
print("-",di["s"]["Mv3"])
print("-",di["s"]["Mv4"])

'''
Example of what we're trying to get: 
Rattata
Level: 50
Hasty Nature
Ability: Run Away
EVs: 252 HP / 252 SpD
IVs: 10 HP / 11 Atk / 12 Def / 13 SpA / 14 SpD / 15 Spe
- Acid Spray
- Aromatherapy
- Burning Jealousy
- Behemoth Bash


print(Dict['Dict1'][<key>])
print(Dict['Dict2'][<key>])

d.get(<key>[, <default>])

d.clear()
d.items() Returns a list of key-value pairs in a dictionary.
d.pop(<key>[, <default>]) Removes a key from a dictionary, if it is present, and returns its value.



'''