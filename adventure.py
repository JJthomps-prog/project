import sys
import json
import re
filename = sys.argv[1]
with open(filename, 'r') as file:
    data = json.load(file)
temp = {}
for room in data:
    if 'name' not in room:
        raise ValueError('Invalid map')
    if 'desc' not in room:
        raise ValueError('Invalid map')
    if 'exits' not in room:
        raise ValueError('Invalid map')
    if isinstance(room['name'], str) == False:
        raise ValueError('Invalid map')
    if isinstance(room['desc'], str) == False:
        raise ValueError('Invalid map')
    i = 0
    for x in data:
        for exit in x['exits']:
            if exit == 'north':
                if 'south' not in list(data[x['exits'][exit]]['exits'].keys()) or data[x['exits'][exit]]['exits']['south'] != i:
                    raise ValueError('Invalid map')
            elif exit == 'south':
                if 'north' not in list(data[x['exits'][exit]]['exits'].keys()) or data[x['exits'][exit]]['exits']['north'] != i:
                    raise ValueError('Invalid map')
            elif exit == 'east':
                if 'west' not in list(data[x['exits'][exit]]['exits'].keys()) or data[x['exits'][exit]]['exits']['west'] != i:
                    raise ValueError('Invalid map')
            elif exit == 'west':
                if 'east' not in list(data[x['exits'][exit]]['exits'].keys()) or data[x['exits'][exit]]['exits']['east'] != i:
                    raise ValueError('Invalid map')
            elif exit == 'northwest':
                if 'southeast' not in list(data[x['exits'][exit]]['exits'].keys()) or data[x['exits'][exit]]['exits']['southeast'] != i:
                    raise ValueError('Invalid map')
            elif exit == 'northeast':
                if 'southwest' not in list(data[x['exits'][exit]]['exits'].keys()) or data[x['exits'][exit]]['exits']['southwest'] != i:
                    raise ValueError('Invalid map')
            elif exit == 'southwest':
                if 'northeast' not in list(data[x['exits'][exit]]['exits'].keys()) or data[x['exits'][exit]]['exits']['northeast'] != i:
                    raise ValueError('Invalid map')
            elif exit == 'southeast':
                if 'northwest' not in list(data[x['exits'][exit]]['exits'].keys()) or data[x['exits'][exit]]['exits']['northwest'] != i:
                    raise ValueError('Invalid map')
        i = i + 1

print(f"> {data[0]['name']}\n\n{data[0]['desc']}\n\nExits: {' '.join(list(data[0]['exits'].keys())).lower()}\n")
index = 0
inventory = []
door3lock = 0
# go大小写还未区分，get只能一次捡一个东西
while True:
    try:
        user_input = input("What would you like to do? ")
        if re.fullmatch(r'^quit$',user_input,re.IGNORECASE):
            print('Goodbye!')
            break

        elif re.match(r'^\s*go\s+door3',user_input,re.IGNORECASE):
            if 'beer' not in inventory and 'weed' not in inventory and door3lock == 0:
                print(f"'Bring me my bear and weed. I won't open the door if you don't have these two things.' A hoarse voice came, accompanied by the sound of a lighter lighting a cigarette.")
            elif 'beer' in inventory and 'weed' not in inventory and door3lock == 0:
                print(f"'Where's my weed. I need weed right now.' A sound came.")
            elif 'beer' not in inventory and 'weed' in inventory and door3lock == 0:
                print(f"'Where's my beer! You know I need my beer to stay sober.'A sound came.")
            elif 'beer' in inventory and 'weed' in inventory and door3lock == 0:
                print(f"'Come on in my friend! I've been waiting you for a long time.' Roommate opened the door with a simle.")
                index = data[index]['exits']['door3']
                print(f"You go door3.\n")
                if 'items' not in data[index].keys() or len(data[index]['items'])==0:
                    print(f"> {data[index]['name']}\n\n{data[index]['desc']}\n\nExits: {' '.join(list(data[index]['exits'].keys())).lower()}\n")
                else:
                    print(f"> {data[index]['name']}\n\n{data[index]['desc']}\n\nItems: {', '.join(data[index]['items']).lower()}\n\nExits: {' '.join(list(data[index]['exits'].keys())).lower()}\n")
                door3lock = 1
            elif door3lock == 1:
                index = data[index]['exits']['door3']
                if 'items' not in data[index].keys() or len(data[index]['items'])==0:
                    print(f"> {data[index]['name']}\n\n{data[index]['desc']}\n\nExits: {' '.join(list(data[index]['exits'].keys())).lower()}\n")
                else:
                    print(f"> {data[index]['name']}\n\n{data[index]['desc']}\n\nItems: {', '.join(data[index]['items']).lower()}\n\nExits: {' '.join(list(data[index]['exits'].keys())).lower()}\n")

        elif re.match(r'^\s*go(\s*|\s+\w*)',user_input,re.IGNORECASE):
            match = re.search(r'\s*go\s+(\S+)',user_input,re.IGNORECASE)
            if match:
                direction = re.sub(r"^\s*go\s+","",user_input.rstrip(),re.IGNORECASE)
                direction = direction.lower()
                exits = list(data[index]['exits'].keys())
                if direction in list(data[index]['exits'].keys()):
                    index = data[index]['exits'][str(match.group(1)).lower()]
                    print(f"You go {direction}.\n")
                    if 'items' not in data[index].keys() or len(data[index]['items'])==0:
                        print(f"> {data[index]['name']}\n\n{data[index]['desc']}\n\nExits: {' '.join(list(data[index]['exits'].keys())).lower()}\n")
                    else:
                        print(f"> {data[index]['name']}\n\n{data[index]['desc']}\n\nItems: {', '.join(data[index]['items']).lower()}\n\nExits: {' '.join(list(data[index]['exits'].keys())).lower()}\n")
                else:
                    print(f"There's no way to go {direction}.")
            else:
                print(f"Sorry, you need to 'go' somewhere.")

        elif re.fullmatch(r'^\s*look$',user_input,re.IGNORECASE):
            if 'items' not in data[index].keys() or len(data[index]['items'])==0:
                print(f"> {data[index]['name']}\n\n{data[index]['desc']}\n\nExits: {' '.join(list(data[index]['exits'].keys())).lower()}\n")
            else:
                print(f"> {data[index]['name']}\n\n{data[index]['desc']}\n\nItems: {', '.join(data[index]['items']).lower()}\n\nExits: {' '.join(list(data[index]['exits'].keys())).lower()}\n")

        elif re.match(r'^\s*get(\s*|\s+\w*)',user_input,re.IGNORECASE):
            match = re.search(r'\s*get\s+(\S+)',user_input,re.IGNORECASE)
            if match:
                item = re.sub(r"^\s*get\s+","",user_input.rstrip(),re.IGNORECASE)
                item = item.lower()
                if 'items' in data[index].keys() and item in data[index]['items']:
                    print(f"You pick up the {item}.")
                    inventory.append(item)
                    data[index]['items'].remove(item)
                else:
                    print(f"There's no {item} anywhere.")
            else:
                print(f"Sorry, you need to 'get' something.")
        
        elif re.fullmatch(r'^\s*inventory$',user_input,re.IGNORECASE):
            if(len(inventory)==0):
                print(f"You're not carrying anything.")
            else:
                print(f"Inventory:")
                for x in inventory:
                    print(f"  {x}")
        
        elif re.match(r'^\s*drop(\s*|\s+\w*)',user_input,re.IGNORECASE):
            match = re.search(r'\s*drop\s+(\S+)',user_input,re.IGNORECASE)
            if match:
                item = re.sub(r"^\s*drop\s+","",user_input.rstrip(),re.IGNORECASE)
                item = item.lower()
                if(len(inventory)==0):
                    print(f"You have nothing to drop.")
                elif item not in inventory:
                    print(f"There's no {item} to drop.")
                else:
                    print(f"You drop the {item}.")
                    if 'items' not in data[index].keys():
                        data[index]['items'] = []
                        data[index]['items'].append(item)
                    else:
                        data[index]['items'].append(item)
                    inventory.remove(item)
            else:
                print(f"You need to drop 'something'.")

        

        

    except EOFError:
        print("\nUse 'quit' to exit.")
