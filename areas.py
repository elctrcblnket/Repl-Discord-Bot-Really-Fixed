# using json library to write dictionary to json file
import json

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


# opens here and closes line 85
#the_file = open('areas.json', 'r+', encoding="utf-8")

def area_checklist(area_name):
  # remove "$area" from area_name
  # split area_name with "," as sep
  # expecting first part of area_name split to have area name (remove comma)
  # expecting second part of resonse split to be either done x or done all or undo x or undo all (remove comma)
  # expecting third and ongoing parts of area_name split to be numbers separated by commas, corresponding to list  items

  # all the lines will be put into one value to return to get_response
  output = ''
  # remove function call
  area_name = area_name.removeprefix("$area ")
  # split to read parts of command
  area_name = area_name.split(sep=", ")

  # empty list for each argument like item list 1, 2, 4, 5
  area_com_args = []

  the_dict = {}
  
  if area_name[0] in AREAS:
    # prints key (just what the user input cuz its gonna be correct) and each entry in value list
    output += ' - ' + area_name[0].title() + '\n\t'
    for i in range(len(AREAS[area_name[0]])):
        output += '\t' + AREAS[area_name[0]][i] + '\n'

    if len(area_name) > 1:
      if area_name[1] == 'done':
        if area_name[2] != 'all':
          for s in area_name[2:]:
            print(s)
        elif area_name[2] == 'all':
          print(area_name[0] + 'ALL DONE\n')
  
      elif area_name[1] == 'undo':
        print(area_name[0] + 'ALL UNDO\n')

  elif area_name[0] == 'print':
    print(area_name[0])
    
    output = 'check console'

    # this works.
    with open('areas.json', 'r+', encoding="utf+8") as the_file:
      # the_dict = json.load(the_file)

      # if area name given after 'print'
      if len(area_name) > 1:
        # go through each line in the file and
        # if the area name matches the line in the file, load the line
        # into a dictionary to use it... requires loads() cuz it
        # can take string literals
        for line in the_file:
          if line.startswith("{\"" + area_name[1]):
            the_dict = json.loads(line)
            print(the_dict[area_name[1]])
            the_dict[area_name[1][0]] = '1. TEST' # how to change value of a list in a dict
            print(the_dict[area_name[1]])

      
    
    '''
    the_dict = json.load(the_file)
    print(type(the_dict))
    output = 'check console'
    '''
  
  else:
    output = 'area name/list item not found'
  
    

  return output

# close the file
#the_file.close()


"""
---pseudocode---
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


---notes---

# should be put in loop with a FUNCTION START and FUNCTION END....no
# should be called by $areas first town
# should be edited by $areas first town done 4

# if command includes "done" and number then
# change todo list item in list by appending (COMPLETED)
# to that list item

# first town done 3, 1
# CHANGES MADE: list item 1, 3 completed
# --- prints list ---
# first town undo 1
# CHANGES MADE: list item 1 undone
# --- prints list ---

json dictionary file io stuff...
so i want these functions to work with dictionaries. either each route will have its own
dictionary, or we will write each route to one single dictionary in the file.
then we will pull the dictionar(y/ies) from the file, and hold it in a variable that we
work with and are able to run the area display and edit functions

maybe smarter to use individual dictionaries for each route. or maybe lists instead....
multiple dictionaries with one value each lol hmmmm fuck it. yeah.
then we can read the beginning of each line and find if it matches the name.. like route1, firsttown, etc
then once it finds the line that starts with that, the line can be loaded into a variable as a dictionary
it'll be edited then written back to the same line

route1 = {'route 1':["1. ev train starter, level to 10","2. input item cheat","3. get leftovers from PC"]}

"""
