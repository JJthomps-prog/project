
Yuehan Qin yqin18@stevens.edu

# URL of public Github repo
https://github.com/JJthomps-prog/project.git

# estimate hours
20 hours

# test
First I test my code with several maps and all good. Then I use my own map. With differnet directions and different items. I verify that items are correctly placed in each room and that they can be interacted with as expected. Test for scenarios in which an item is essential to completing a puzzle or progressing through the game. I check that each room has the appropriate exits leading to other rooms in the game world. Ensure that the exits are clearly labeled and that they lead to the intended destination.
My map is like:

|----------------|                             |--------------------------|
|Rocky's bathroom|                             | Rocky's Roommate bathroom|
|-----door1------|-----------------------------|-----------door4----------|
|Rocky's room  door2   Rocky's Living room   door3 Rocky's Roommate room  |
|----------------|------------door5------------|--------------------------|


The intention of the game is to get the keys before you go door5(Exit).
You need to pick the weed and beer in Living room, then your Roommate will unlock the door3. You need to drop them in your roommate room and there would be a box in your roommate bathroom. Under it and you will get the keys. Then you could leave.

# bugs and issues

No

# resolved issue
python3 adventure.py loop.map
>go door3
with error in other map
You need to specify the room's name when you go to the room , otherwise you would have error when you change the map.

#extension
drop verb:
use re.match(r'^\s*drop(\s*|\s+\w*)',user_input,re.IGNORECASE) to find the drop input
delete the drop and get the item by using re.sub(r"^\s*drop\s+","",user_input.rstrip(),re.IGNORECASE).
find the item in inventory and drop it. If there's no such thing in your inventory this will print There's no {item} to drop. If you don't input [item] it will print(f"You need to drop 'something'.")
In the game you need to drop the weed and beer in your roommate's bedroom to get the location of the keys in the bathroom.

locked doors:
If you get the weed and beer in the living room, the door3 will open. Otherwise, it will be locked. But if you have opened it. It would be always open.

Winning and losing conditions:
Once you get the keys in the Roommate bathroom and get out from door5, you would win the game. But if you don't get the keys and get out, you lose.
