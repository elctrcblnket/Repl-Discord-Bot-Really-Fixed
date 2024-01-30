# dictionary of AREAS with values of lists (todo lists)
AREAS = {
  "route 1" : [
    "1. ev train starter, level to 10",
    "2. input item cheat",
    "3. get leftovers from PC"
  ],
  "route 2" : [
    "1. catch route 2 mon"
  ],
  "first town" : [
    "1. get heal balls",
    "2. get egg from old guy",
    "3. go to mart",
    "4. TEST"
  ]
}

# should be put in loop with a FUNCTION START and FUNCTION END....no
# should be called by $areas first town
# should be edited by $areas first town done 4

# what is the function that takes input from discord message/post?
POST = input("Area name/Route #? ")

# checks if key is in dictionary
if POST in AREAS:
  # prints key (just what the user input cuz its gonna be correct) and each entry in value list
  print(' - ' + POST.title())
  for i in range(len(AREAS[POST])):
      print('\t' + AREAS[POST][i])

else: print('area name not found')

# if command includes "done" and number then
# change todo list item in list by appending (COMPLETED)
# to that list item



"""

input route 1
display todo list like:
1. ev train starter, level to 10
2. input item cheat
3. get leftovers from PC

input route 1 done 1
display route 1, item 1 DONE

input route 1
display:
1. ev train starter, level to 10     (COMPLETE)
2. input item cheat
3. get leftovers from PC

input route 1 done all
display route 1, ALL DONE

inpute route 1
display:
1. ev train starter, level to 10     (COMPLETE)
2. input item cheat                  (COMPLETE)
3. get leftovers from PC             (COMPLETE)

"""
