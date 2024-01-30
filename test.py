stats = ['HP', 'ATK', 'DEF', 'SPATK', 'SPDEF', 'SPE']

correct = 1

while correct:
  your_stats = input('? ')
  your_stats = your_stats.split()
  
  correct = 0

  for i in your_stats:
    print('in for loop' + str(i))
    if i not in stats:
      correct = 1
  
print('out of loop')

# TEST RIGHT:
# HP ATK DEF

# TEST WRONG:
# Hp ATK DEF
# H P ATK DEF
# HP ATKK DEF
# HP ATK DEEF
# HP ATK DE EF

# https://realpython.com/how-to-make-a-discord-bot-python/#connecting-a-bot