print('''          
                             888     d8b         
                             888     Y8P         
                             888                 
88888888 .d88b. 88888b.d88b. 88888b. 888 .d88b.  
   d88P d88""88b888 "888 "88b888 "88b888d8P  Y8b 
  d88P  888  888888  888  888888  88888888888888 
 d88P   Y88..88P888  888  888888 d88P888Y8b.     
88888888 "Y88P" 888  888  88888888P" 888 "Y8888  
''')

# The Intro:
print("Welcome to The Apocalypse!\nCan you make it to camp?")
print("There is crashing outside of your apartment, when you look out the window, you notice people attacking "
      "each other.\nYou know there is only one thing you can do...")

choice1 = input("You:\n(a) lock your door\n(b) run to your car\n(c) scream\n")
if choice1 == "b":
    print("""You bolt to the garage, grabbing your keys on the way, you make it to your car and pull onto the street. It
is pure chaos. You notice an alley way and continue down until you come to a fork at the end...""")
    choice2 = input("Do you continue\n(a) right or\n(b) left?\n")
    if choice2 == "b":
        print("""You turn left and continue down the road, avoiding crashes already on the road.
You hit several zombies in your way. Another car comes speeding towards you, not slowing down...""")
        choice3 = input("You:\n(a) Speed up and play chicken\n(b) Quickly turn and drift out of the way\n"
                        "(c) freeze, they'll stop\n")
        if choice3 == "b":
            print("""Quick thinking! You manage to swerve out of the way of the oncoming vehicle just in time. You pull 
over to take a breath after that near accident. After calming down for a few seconds (that's all you have, come on it's 
the end of the world here!), you pull back onto the road. You continue down the road eventually reaching nothing but 
corn fields. The road is deserted, no people or zombies seem to be around and you feel like you can finally think 
clearly. Lost in thought about everything that has happened, you almost miss the house along the right. There are lights
on inside... """)
            choice4 = input("You:\n(a) Walk up to the house and knock on the door\n"
                            "(b) sneak around the house and look in the windows, scoping it out\n"
                            "(c) decide it's too risky and continue down the road\n")
            if choice4 == "a":
                print("""A sweet old lady named Norma answers the door, \"Oh come on in dear. Let's get a look, doesn't 
look like you have had any run-ins with those eaters. Please, let me grab you some water and grab the others.\" You sit 
yourself at the dinning table as a large group comes in to meet you. The group introduces themselves and soon after you 
are invited to join their camp. They have plenty of resources and they are making plans for supply runs, started to put 
up barriers, and have plans to create a full survival camp on the land. You have made it and just maybe you will 
actually survive this!\nYOU'VE WON!!!!!!!!!""")
            elif choice4 == "b":
                print("""You probably thought this was a swell idea, making sure no zombies were lurking inside.Instead
you have caught the attention of the group inside. A man named Marshall has had enough of the zombies and in a rage he 
fires his shotgun through the window. It's a headshot; You go down immediately! Marshall peers out the window, checking 
for other zombies and looks down at his handiwork. A body with no head, but he notices no dark veins in your hands and 
realizes he shot a fellow human. He freaks out and goes outside to collect your body \"Shoot, I'm sorry, I thought you 
were one of them zombies or something. Never can be too careful, but I'll give ya a proper burial.\" He spends the night
digging a shallow grave and plops you in. Soon you are devoured by creatures in the soil, but hey, at least you didn't 
become a zombie?\nGAME OVER!!""")
                exit()
            else:
                print("""Sometimes, playing it safe isn't actually safe. As you continue down the road, the car's fuel 
tank alert pops up, you are running on E! You stop the car, the house can't be too far back and maybe you can find some
help. As you are walking back, about a mile away from the car now, you can see the house. Suddenly you hear rustling in
the fields, something big is coming! You pick up the pace running to the house, so close. Behind you a heard of zombies 
rush out of the fields, your adrenaline peaks and you run faster, but zombies come pouring out from the field in front 
of you. You are surrounded, they close in. Bit by bit, bite by bite, they tear you limb from limb.\nGAME OVER!!""")
                exit()
        elif choice3 == "a":
            print("""Maybe not the brightest idea here, but hey let's find out what happens anyway?; You are closing in
on the car fast, you can see the driver of the other car is already dead, it's too late to slam on the brakes as you 
both crash into each other at 120mph. Suddenly you are flying, feeling free, soaring, until you realize you were thrown 
from the windshield and you can feel the cuts all over your face, blood dripping to the ground, suddenly before you can 
fully panic, you slam into a road sign and die instantly...Well, I guess neither of you chickened out? So perhaps you 
count that as a win, but you still got...\nGAME OVER!!""")
            exit()
        else:
            print("""You know, maybe you just weren't cut out to survive in a world like this? That's okay. You freeze 
up and your car beings to slow without pressure on the accelerator. The other car isn't slowing down, you notice through
the windshield the other driver is already dead. Still in freeze mode, you are internally panicking. Unable to move,the 
car slam into you head first...you awake a few minutes later with a raging headache and blood dripping in your eyes. You
hear a shuffling as someone comes close. You can't turn your head but you feel someone put their arm through the window,
they try to grab you backwards but you are stuck. The car is crushed around your legs. You hear a light snarl and 
suddenly feel a deep pain in your neck. The other driver has turned and is feeding on you, you can do nothing about it 
but scream...the screaming goes on for what feels like forever until the zombie bites deeper into your neck. Suddenly 
blood is spurting and within minutes you feel nothing, you drift off into the darkness until your heart beats it's final
beat...\nGAME OVER!!""")
            exit()
    else:
        print("""You turn right and continue down the road. Out of nowhere a semi comes speeding towards you, you slam 
on your brakes hoping to avoid the crash but it's too late. The semi collides into the side of your car, causing the car
to crash in around you, you feel your bones crush and crack as you fade out of consciousness, never to awake again!
GAME OVER!!""")
        exit()

elif choice1 == "a":
    print("""Just as you reach your door, it slams open. Your neighbor attacks you violently shoving you against the 
wall; Your breath is knocked out of your lungs as you struggle to push them back. You grab their collar holding them 
back as they attempt to bite you, your hand slips from the collar and you lose your grip as their teeth sink into your 
neck. You push back but it's too late, you can feel yourself turning already, black making its way up your veins. You've
become a zombie and go on attacking others in the vicinity.\nGAME OVER!!""")
    exit()

else:
    print("""Really? This was your bright idea? You stand completely still and scream at the horrors outside:
\"AHHHHHHHH!!!\" Your scream attracts a horde of outside that comes rushing into your apartment. You are too stunned
to move. The horde runs into you, pushing you down as they tear into you, hungry and insatiable they devour you down to 
your bones. You've become nothing more than a pile of bones on your living room floor.\nGAME OVER!!""")
    exit()
