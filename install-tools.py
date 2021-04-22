import subprocess
import os

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

tools = {}
tool_names = []
directory = "tools/"

for filename in os.listdir("tools/"):
    path = os.path.join(directory, filename)
    with open(path, "r") as f:
        category = filename.rsplit('.', 1)[0]
        tool_names.append(category)
        tools[category] = []
        for line in f:
            line = line.strip()
            tools[category].append(line)

print(tools.keys())
print(tool_names)


choice = input(f"""
======================
{BOLD}HackTools Menu{ENDC}
======================
{BOLD}
{OKCYAN}i{ENDC}: Install tools
{OKCYAN}s{ENDC}: Show categories
{OKCYAN}l{ENDC}: List tools & categories
{ENDC}
======================>

> {OKCYAN}""").lower()

print(ENDC)

if choice == 'i':
    i = 1
    for category in tool_names:
        print(OKCYAN + "[" + str(i) + "] " + ENDC + category)
        i += 1
    
    print()
    numbers = input("Type the numbers of the categories you would like to install.\nExample: 2143\n> ")
    print()
    numbers = str(numbers)

    tools_to_install = []
    categories_to_install = []
    
    for number in numbers:
        current_category = tool_names[int(number) - 1]
        categories_to_install.append(current_category)
        category_tools = tools[current_category]
        for tool in category_tools:
            tools_to_install.append(tool)

    print("Ready to install " + str(len(categories_to_install)) + " categories (" + str(len(tools_to_install)) + " tools).")
    choice = input("Continue? [Y/n]: ").lower()
    if choice == "y" or choice == '':
        for tool in tools_to_install:
            try:
                print("RUNNING: " + OKGREEN + tool + ENDC)
                command = tool.split(" ")
                subprocess.run(command, check = True, stdout=subprocess.DEVNULL)
            except subprocess.CalledProcessError:
                print(WARNING + "[ERROR] Command failed:   '" + ENDC + OKGREEN + tool + "'" + ENDC)


elif choice == "l":
    i = 1
    for category, category_tools in tools.items():
        print(OKCYAN + "\n[" + str(i)+ "] " + ENDC + category)
        for tool in category_tools:
            print("|  " + tool)
        i += 1
    print()

elif choice == "s":
    i = 1
    for category in tools.keys():
        print("[" + str(i) + "]  " + category)
        i += 1