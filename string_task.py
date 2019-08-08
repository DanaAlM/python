time = input("Time: ")
item_1 = input("Noun:  ")
name = input("Name:  ")
scream = input("Sentence:  ")
action = input("Verb:  ")
name += name.title
scream += scream.upper
   print("""It was {} when I heard a knock at the door. I opened the door and there was a box full of {} with a note saying "From {}".Just as I closed the door I heard a scream "{}".I froze in place and all I could do was {}. """.format(time, item_1,name,scream,action))      
