transform bg_fit:
    xysize(1920,1080)
default [main_character] = "Robin"
default day_num = 0
default suspicion = 0
label start:
    scene black
    with dissolve 
    with fade 
    "The listing does not say much."
    "\"Live-in Caretaker needed. Immediate start, pay well above market rate.\""
    "No interview. No photo of the house, just an address, and a time to arrive."
    $ main_character = renpy.input("What is your name?", default = main_character)
    $ main_character = main_character.strip() or "Robin"
    "You told yourself it did not matter when the pay was that good. You needed the work."
    scene house_exterior_dark at bg_fit
    with dissolve
    with fade
    "It was already late when you arrived because of the long journey."
    "No one came to greet you. The door opened on it's own after you knocked it two times."
    show simon at truecenter
    with dissolve
    s "Oh, you must be [main_character], Right on time. So glad that you came."
    s "I am Simon. I handle... well a bit of everything around here."
    s "Come in, you must be very tired from the trip."
    hide simon
    m "Is the owner around? I should be reporting to them directly."
    show simon at truecenter
    s "Ah, about that."
    s "Mr.Ashworth does not really recieve guests. Not anyone, really. Not in person." 
    s "But do not worry. He always leaves instructions."
    hide simon
    "Simon presses a folded note inside your hands before you could say anything."
    mn "Welcome. I believe Simon has made you comfortable."
    mn "You will find your duties simple, as long as you keep to them."
    mn "There are just three simple rules here."
    mn "Do not remove anything from the study."
    mn "Do not go to the west wing."
    mn "Do not go looking for me."
    mn "I will know if you do."
    "You looked up. Simon was still smiling."
    show simoon at truecenter
    s "He is very particular. But it's all right, he is fair if you follow the rules."
    s "Come, I will show you to your room. Tomorrow starts early, it is already late."
    $ day_num = 1
    jump day_1
label day_1:
    scene bedroom at bg_fit
    with fade
    with dissolve
    "Morning came early, as Simon had warned you."
    "The room was small but tidy, and the bed was made up beforeyou even chose it."
    "A schedule was already written on the nightstand, written in the same hand as last night's note."
    mn "6:30 : Breakfast tray to the study room, do not knock it. Just leave it and go."
    mn "8:00 : Mrs. Voss will show you around the house."
    mn "All the other hours are yours, being your first day."
    mn "Within the rules that I have already given."
    "You got dresses up and went to find the kitchen."
    scene kitchen_room at bg_fit
    with dissolve
    with fade
    show voss at truecenter
    with dissolve
    v "So you are the new hire. Good, the tray is ready to go."
    v "Do not dance around, he does not like sitting it out."
    hide voss
    m "Nobody has ever mentioned his real name."
    m "Not even what he looks like."
    show voss at truecenter
    with dissolve
    v "That is because none of us know that either."
    v "Not anymore."
    hide voss
    menu:
        m "Anymore?"
        "Ask what she means by \"Anymore\"":
            m "What do you mean by Anymore?"
            show voss at truecenter
            with dissolve
            v "I meant that it has been a long, long time since anyone has laid their eyes on him."
            v "Long before me, you or Simon were even here."
            v "And Simon has been here longer than me."
            v "Take the tray. West hallway, last door. And do not knock."
            hide voss
            $ suspicion = 1
        "Just take the tray.":
            show voss
            with dissolve
            v "Go on, then. West hallway last door."
            v "Just leave the tray there. Do not knock."
            $ suspicion = 1
    scene upstairs_hall at bg_fit
    with dissolve
    with fade        
    "You carried the tray up the stairs which creaked in places even where it looked fine."
    "The study room's door looked heavier than the other doors."
    "You set the tray down as you were told, and did not knock."
    "As you turned around to leave, you thought you heard the floor shift on the other side of the door."
    "Like someone standing slowly, after sitting alone for a long time."
    "You told yourself that it was the house settling."
    scene main_hall at bg_fit
    with fade
    with dissolve
    show voss at truecenter
    with dissolve
    v "This is the main hall. Dining room is there and the drawing room is just through there."
    v "You do not want to take either much. He takes his meals alone."
    v "I think you might already know, but the west wing is off limits."
    v "Study, his private rooms. Only Simon has ever gone past, and that is only when called for."
    hide voss
    m "Called for? I heard that he does not see anyone."
    show voss at truecenter
    with dissolve
    v "He does not. He only ever writes and Simon reads."
    hide voss
    "She said it so plainly that it did not sound so much strange at all."
    menu:
        "Should you push a little further?"
        "Push a little further.":
            m "That does not seem odd to you?"
            m "Running a house for someone that has not shown himself in ages?"
            show voss at truecenter
            with dissolve
            v "Odd is not the word that I would use anymore."
            v "That is just how it is over here."
            v "You will get used to it and stop wondering eventually."
            v "That is just how it is for everyone over here."
            v "You will stop asking eventually, everyone does."
            $ suspicion += 1
        "Let it go.":
            mc "Right.... noted."
            show voss at truecenter
            v "Good. The kitchen is back that way if you need anything."
            v "Mind the rules and then you will be fine here."
    scene garden at bg_fit
    with dissolve
    with fade
    show hale at truecenter
    with dissolve
    h "Yo are the new one? I figured. No one else would be out here anyways."
    h "What are you doing here"
    hide hale
    m "Just getting my bearings. You work the grounds?"
    show hale at truecenter
    with dissolve
    h "Grounds. Yeah not the house."
    h "Have not set foot past the back door in 3 years."
    h "I do not plan to either."
    hide hale 
    menu:
        "That is surprising. Should I ask why?"
        "Ask why.":
            m "Is there a reason for that?"
            show hale at truecenter
            with dissolve
            h "No... I just prefer it out here."
            hide hale
            "He did not look at you when he said that."
            $ suspicion += 1
        "Leave it alone.":
            m "Fair enough."
            show hale at truecenter
            with dissolve
            "He went back to the hedges without any other word, and did not stop until you had walked away."
    "That evening, you went back to get the tray that you had put there in the morning."
    scene upstairs_hall at bg_fit
    with dissolve
    with fade
    "The food was untouched. Every bit of it was arranged as exactly how you left it."
    "But there was a change, the note was replaced with the new one. You pick it up."
    mn "You spoke to Voss and Hale about me today."
    mn "I do not mind some curiosity. I mind repitition."
    mn "Ask them again, and I will know that you did not the first time."
    "You had not told anyone that you asked."
    scene bedroom at truecenter
    with dissolve
    with fade
    "Your first day as a caretaker of that place was over."
    "You laid awoke for a while, to a house that everyone insisted, was just settling."
    $ day_num = 2
    jump day_2
label day_2:
            
        
        
        