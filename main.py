print('''

               \.   \.      __,-"-.__      ./   ./
           \.   \`.  \`.-'"" _,="=._ ""`-.'/  .'/   ./
            \`.  \_`-''      _,="=._      ``-'_/  .'/
             \ `-',-._   _.  _,="=._  ,_   _.-,`-' /
          \. /`,-',-._"""  \ _,="=._ /  """_.-,`-,'\ ./
           \`-'  /    `-._  "       "  _.-'    \  `-'/
           /)   (         \    ,-.    /         )   (\
        ,-'"     `-.       \  /   \  /       .-'     "`-,
      ,'_._         `-.____/ /  _  \ \____.-'         _._`,
     /,'   `.                \_/ \_/                .'   `,\
    /'       )                  _             (       `\
            /   _,-'"`-.  ,++|T|||T|++.  .-'"`-,_   \
           / ,-'        \/|`|`|`|'|'|'|\/        `-, \
          /,'             | | | | | | |             `,\
         /'               ` | | | | | '               `\
                            ` | | | '
                              ` | '
''')
print("Welcome to Galaxy Uprising!")
print("Your mission is to save the Galaxy.")

choice1 = input('you are piloting your starship in space and you see a blackhole on the right side, What do you do? Type "right" or "left".').lower()

if choice1 == "left":
  choice2 = input('you survived, but there is a space squid ready to devour your ship,you can try to lose it in the asteroid field. Type "asteroid" or "fly"').lower()
  if choice2 == "asteroid":
    choice3 = input("phew, that was close. you have now arrived to HQ but see Krogg the destroyer about to destroy HQ. Type 'warn others' or 'fly away' or 'save them' ").lower()
    if choice3 == "save them":
      print("You saved the day, Krogg is destroyed and everyone in HQ was saved. Thank you for your sacrifice, Hero")
    elif choice3 == "fly away":
      print("You have only saved yourself, coward. Game Over")
    elif choice3 == "warn others":
      print("you wasted too much time. HQ was blown to dust. Game Over")
    else:   
      print("you chose an option that does not exist")
  else:
    print("you are squid food. Game Over")
else:
  print("You were sucked in the black hole. Game Over")

