dict = {}
nature = [
  "Bashful", "Docile", "Hardy", "Quirky", "Serious", "Adamant", "Brave", "Lonely", "Naughty", "Bold", "Impish", "Lax", "Relaxed", "Modest", "Mild", "Quiet", "Rash", "Calm","Careful", "Gentle", "Sassy", "Hasty", "Jolly", "Naive", "Timid",
]
stats = ["Atk", "HP","Def","SpA","SpD"]
'''
HOLD
input0 = input("Nickname?")
input1 = input("Pokemon and level?")
input1 = input1.split()
while True:
  input2 = input("Nature?")
if input2 in nature:
'''
while True: 
  input3 = input("How was it trained?")
  input3 = input3.split()
  if input3[0] in stats and input3[1] in stats:
    print("Success! ")
'''
    input3 = input3.split()

    input4 = input("Moves learned?")
    input4 = input4.split()

'''
#need to pull api of list of all moves? or file
dict["Poke"] = input1[0]
dict["Name"] = input1[1]
dict["Lv"] = input2[1]
dict["Ntr"] = input2[1]
dict["Tra1"] = input3[0]
dict["Tra2"] = input3[1]
dict["Ab"] = input2[0]

print(dict)