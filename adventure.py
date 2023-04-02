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
    for exit in room['exits']:
        if exit not in temp:
            temp[exit] = room['exits'][exit]
        else:
            if temp[exit] == room['exits'][exit]:
                raise ValueError('Invalid map')
        temp[exit] = room['exits'][exit]
print(f"> {data[0]['name']}\n\n{data[0]['desc']}\n\nExits: {' '.join(list(data[0]['exits'].keys())).lower()}\n")
index = 0
inventory = []
# go大小写还未区分，get只能一次捡一个东西
while True:
    try:
        user_input = input("What would you like to do? ")
        if re.fullmatch(r'^quit$',user_input,re.IGNORECASE):
            print('Goodbye!')
            break
        if re.fullmatch(r'^go(\s*|\s+\w*)',user_input,re.IGNORECASE):
            match = re.search(r'go\s+(\S+)',user_input,re.IGNORECASE)
            if match:
                direction = str(match.group(1)).lower()
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

        if re.fullmatch(r'^look$',user_input,re.IGNORECASE):
            if 'items' not in data[index].keys() or len(data[index]['items'])==0:
                print(f"> {data[index]['name']}\n\n{data[index]['desc']}\n\nExits: {' '.join(list(data[index]['exits'].keys())).lower()}\n")
            else:
                print(f"> {data[index]['name']}\n\n{data[index]['desc']}\n\nItems: {', '.join(data[index]['items']).lower()}\n\nExits: {' '.join(list(data[index]['exits'].keys())).lower()}\n")

        if re.match(r'^get(\s*|\s+\w*)',user_input,re.IGNORECASE):
            match = re.search(r'get\s+(\S+)',user_input,re.IGNORECASE)
            if match:
                item = re.sub(r"^get\s+","",user_input.rstrip(),re.IGNORECASE)
                if 'items' in data[index].keys() and item in data[index]['items']:
                    print(f"You pick up the {item}.")
                    inventory.append(item)
                else:
                    print(f"There's no {item} anywhere.")
            else:
                print(f"Sorry, you need to 'get' something.")
        
        if re.fullmatch(r'^inventory$',user_input,re.IGNORECASE):
            if(len(inventory)==0):
                print(f"You're not carrying anything.")
            else:
                print(f"Inventory:")
                for x in inventory:
                    print(f" {x}")

    except EOFError:
        print("\nUse 'quit' to exit.")
