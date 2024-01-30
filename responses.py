from replit import db
from cheat_moves import moves
from areas import area_checklist

#helper - Updating new mon
def update_database(new_mon, route):
    db[route] = [new_mon]
    return "new pokemon"

#Function: deleting mons in database
def delete_mons(del_mon):
  if del_mon in db.keys():
    del db[del_mon]
    return "removed"
  else:
    return "no valid pokemon"

# function calls areas.py
# def area_todo()

def get_response(user_input):
  response: str = user_input.lower()
  if response.startswith("@"):
    return "delete"
  if response == "list mons":
    return "list mons"
  if response.startswith("cheat"):
    response = response.split()
    response = " ".join(response[1:])
    code = moves(response)
    return code

  if response.startswith("key"):
    mons = response.split()
    if mons[1] in db.key():
      print(mons[1])
      new_key = mons[1]
      del db[new_key]
      return f"{new_key} deleted"
    else:
      return "No valid key"

  if response.startswith("$add"):
    add_mon = response.split()
    if add_mon[2] in db.keys():
      return "already there"
    else:
      update_database(add_mon[1], add_mon[2])
      return f'added {add_mon[1]}'

  if response.startswith("$del"):
    del_mon = response.split()[1]
    delete_mons(del_mon)

  # calling area function
  if response.startswith("$area"):
    return area_checklist(response)