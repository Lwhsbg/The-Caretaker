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
    show simon at truecenter
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
    scene bedroom at bg_fit
    with fade
    with dissolve
    "You woke up before the note did, for once."
    "It caught up with you when you made it at the kitchen table instead."
    scene kitchen_room at bg_fit
    with dissolve
    with fade
    mn "6:30 : Breakfast tray, as before."
    mn "10:00 : The library needs dusting. Simon will show where the good clothes are kept."
    mn "Leave anything that you find as it is."
    "you noticed, for the first time, that the handwriting slanted differently at the end of each note than at the start."
    "Like two different moods, or two different hands that tried to match each other."
    menu:
        "Dwell on the handwriting.":
            "You told herself that you were overthinking it."
            "Grief did some strange things to a person's hands, maybe."
            "You did not know anything about him yet, really."
            $ suspicion += 1
        "Do not think too hard about it.":
            "You folded the note and got moving."
            "No sense reading too much into paper."
    scene upstairs_hall at bg_fit
    with dissolve
    with fade
    "You brought the tray up."
    "Just the cup that you left there yesterday seemed to have mooved a little bit."
    "Just the cup. Nothing else."
    menu:
        "Look closer at the cup.":
            "It had now exactly been turned ninety degrees, handle now facing the door instead of out of it."
            "Like someone wanted you to notice it had been touched, without actually drinking anything."
            $ suspicion += 1
        "Do not overthink it, just keep moving.":
            "You told yourself that people move cups. That is what cups are for."
            "You set the new tray down, did not knock, same as yesterday."
            "Same as you had been told to."
    scene bg main_hall at bg_fit
    with dissolve
    with fade
    show simon at truecenter
    with dissolve
    s "There you are. Sheep alright?"
    s "First nights in a new place are never easy, they say."
    hide simon
    m "It was fine. Very quiet though."
    show simon at truecenter
    with dissolve
    s "Quiet. Quiet is good. Come on, the cloths are in the hall closet."
    s "I will walk you into the library, it is a bit of a maze if you do not know about it."
    "He talked the entire way there. About the weather and a leak in the east gutter."
    "He kept meaning to mention to Hale. About nothing, really, filling every silence before it even had a chance to start."
    hide simon 
    menu optional_name:
        "Ask him directly how long he has worked here.":
            m "How long have you been here, exactly?"
            m "Mrs. Voss made it sound like it was a long time."
            show simon at truecenter
            with dissolve
            s "Oh, longer than I can properly say. Time gets away from you in a house like this."
            hide simon
            "He smiled when he said it. The smile did not change at all, which was the strange part."
            $ suspicion += 1            
        "Ask if he has ever seen Mr. Ashworth.":
            m "Have you ever actually seen him? Face to face?"
            show simon at truecenter
            with dissolve
            s "Once... a long time ago."
            hide simon
            "For the first time since you had met him, Simon did not fill the silence that immediately followed."
            $ suspicion += 2
        "Do not push. Just get to work.":
            jump after_scene
label after_scene:            
    show simon at truecenter
    with dissolve
    s "Here is the library. Cloths are on the shelf by the door."
    s "Mind the top one, it sticks."
    scene library at bg_fit
    with dissolve
    with fade
    "The library smelled something like old paper and something faintly like candle smoke, though there was not any candle around."
    "Dusting was slow, methodical work. Most of the books were just very, very old."
    "On the third shelf, wedged down, you found a small framed photograph, face down."
    menu:
        "Turn it over and look.":
            "A man in his sixties, silvered hair and standing infront of the same house."
            "Someone had written in the back in pencil, faded to nothing."
            "\"Edmund Ashworth. Final photograph, taken the week before.\""
            "The week before *what*, it did not say."
            $ suspicion += 2
            "You heard footsteps somewhere above you, slow, deliberate, crossing a room directly overhead."
            "There was no room supposed to be there."
        "Leave it face down, undisturbed.":
            "You left it exactly as you found it. Some things in this house, were starting to feel, left face down on purpose."
            "Still, you could not unsee the edge of the frame, or stop wondering who turned it over to begin with, and who turned it back."
            $ suspicion += 1
    "You finished dusting faster than you had meant to."
    "You did not look back at the ceiling again."
    scene kitchen_room at bg_fit
    with dissolve
    with fade
    show voss at truecenter
    with dissolve
    v "You have got dust on your sleeve."
    v "From the library, then."
    hide voss
    m "Mrs. Voss, is his name Edmund? Edmund Ashworth?"
    "She went very still, the way people do when a name lands somewhere they did not want it to."
    show voss at truecenter
    with dissolve
    v "...Where did you hear that name?"
    hide voss
    menu:
        "Tell her about the photograph.":
            m "There was a photo in the library, face down. It said final photograph. What does final mean?"
            show voss at truecenter
            v "That is not something that I am going to discuss standing in the kitchen."
            v "Finish your work, some questions do not have good answers."
            $ suspicion += 2
            hide voss
            "She did not say the answer. But she also did not tell you that the question was wrong."
        "Say you just heard it somewhere.":
            m "I do not know. I must have heard Simon say it."
            show voss at truecenter
            with dissolve
            with fade
            v "Simon does not use that name. Nobody here does."
            hide voss 
            "She looked at you a moment longer, then went back to her work without another word."
            $ suspicion += 1
    scene bg garden at bg_fit
    with dissolve
    with fade
    show hale at truecenter
    with dissolve
    "You find Hale kneeling at a patch of overturned gradd near the wall."
    m "Planting something new?"
    h "...No"
    "He stood, brushed his knees, and did not explain any further."
    hide hale 
    "You notice, gthat the patch was the size and shape of a grave, though there was no any stone."
    scene upstairs_hall at bg_fit
    with dissolve
    with fade
    "That night's tray came back with the moved cup again. same as yesterday."
    "Besides it, a new note, longer than the others."
    mn "You found the photograph."
    mn "I do not fault you for that, curiosity is not disobedience, not yet."
    mn "But you asked Simon whether he had seen my face and Voss my name."
    mn "That is a pattern. A pattern worth watching."
    mn "Sleep well, tomorrow I have something to deliver to you personally."
    scene bedroom at bg_fit
    with dissolve
    with fade
    "You read it two times. You were sure you had not said that name too loud to anyone."
    "Only to Mrs. Voss,in a silent, empty kitchen."
    $ day_num = 3
    jump day_3
label day_3:
    scene bedroom at bg_fit
    with dissolve
    with fade
    "The note was waiting in the floor, slid in sometime during the night, probably."
    "You had not heard anything anyways."
    mn "Today, you will deliver something to me personally, not outside, but inside my desk, personaly with your own hands."
    mn "Knock once, wait for silence."
    mn "Enter only when I do not answer."
    mn "The parcel is on the kitchen table. Do not open it."
    "You read it again and again, to make sure you did not read the strange instructions wrong."
    scene kitchen_room at bg_fit
    with dissolve
    with fade
    "The parcel was small and wrapped in brown paper. It looked pretty old, but you paid no mind."
    menu:
        "Try to feel what is inside through the paper.":
            "You pressed your fingers through it."
            "You felt something rectangular with edges. Maybe it was a book, or a photograph like the one that you found in the library."
            $ suspicion += 1
        "Carry it up as told.":
            "You quickly dissociate any thoughts regarding what is inside the parcel, and proceeded to carry it upwards."
    show voss at truecenter
    with dissolvev "He has not asked for this in a very long time..."
    hide voss
    scene upstairs_hall at bg_fit
    with dissolve
    with fade
    "The heavy door looked the same as it had every other time you had stood infront of it."
    "But somehow, today, it felt taller."
    "You knocked once, like you were told, and then waited."
    "Silence."
    "You pushed the door open."
    scene study at bg_fit
    with dissolve
    with fade
    "The study was decent sized for a mansion, a desk faced the window with the chair pushed in."
    "There was no one in the room."
    "There was also, a distinct impression that someone had been, just some moments ago."
    menu:
        "Look around before setting the parcel down.":
            "Books stacked up with a precision that no living hand kept up for long."
            "A teacup on the desk's edge, the same shape of what you carried up this morning, bone dry with the faintest of steam rising through it."
            "Like it had been poured seconds before you came in."
            "You did not touch the teacup."
            $ suspicion += 2
        "Set the parcel down and then leave quickly.":
            "You crossed the room, and set the parcel in the desk gently on the desk besides a stack of ledgers."
            "You did not touch anything."
            "That did not stop you from noticing though, a table that had moved slightly, maybe 2 inches after you had come in."
            "Nothing had touched it."
            $ suspicion += 1
    "The temperature in the room had dropped hard enough that your breath fogged , once, and then it did not again."
    "You left there without looking back, and did not remember closing the door until you were three steps down the hallway."
    scene main_hall at bg_fit
    with dissolve
    with fade
    show simon at truecenter
    with dissolve
    s "There you are, how did it go? Did he say anything?"
    hide simon
    m "The room was empty."
    "Simon's smile flickered, in a way  it does right when oit decides whether to go out or not."
    show simon at truecenter
    with dissolve
    s "Well, empty. He does that, sometimes. Comes and goes. Big mansion with big doors."
    menu:
        "Point out that there is no other door out of that room.":
            m "There is only one door, Simon. I was standing right outside of it."
            show simon at truecenter
            s "...Was there? I could have sworn-"
            hide simon
            "He stopped himself and laughed once, maybe a bit too much, and proceeded to change the topic before you could have asked what he had sworn."
            $ suspicion += 2
        "Let that comment go.":
            m "Guess so."
            show simon at truecenter
            with dissolve
            s "He will get what was delivered to him one way or another. He always does."
            hide simon
            "One way or the another. You turned the phrase over for the rest of your afternoon and did not really like the shape of it."
    scene garden at bg_fit
    with dissolve
    with fade
    m "Mr.Hale, is that a grave on the patch of dirt over there?"
    "He did not answer right away. When he did, his voice changed in a way it never had before."
    show hale at truecenter
    with dissolve
    h "Ask me something else."
    hide hale 
    m "Thats a no."
    show hale at truecenter
    with dissolve
    h "Not a yes, either. Ask me something else, or nothing at all."
    $ suspicion += 2
    "You let it go, not because you wanted to, but because of Hale's face which told you not to push further."
    scene upstairs_hall at bg_fit
    with dissolve
    with fade
    "The tray was there as always, untouched."
    mn "Thank you for the delivery. Whatever Simon told, ignore it. I am not the only ones who leaves notes. Be careful whom to trust."
    "You stand cold in the hallway for a while, and then returned back to the bedroom."
    scene bedroom at bg_fit
    with dissolve
    with fade
    "Two different hands and two different notes. You start to understand Edmund was not the only one writing to you."
    $ day num = 4
    jump day_4
label day_4:
    scene bedroom at bg_fit
    with dissolve
    with fade
    if suspicion >= 9:
        mn "You are asking questions faster than I can answer them safely."
        mn "Slow down, for your own sake, not mine."
    elif suspicion >= 4:
        mn "Today, be more careful about who you ask than what you notice."
    else:
        mn "6:30 breakfast tray. That is the only thing for today."
    "You read the notes lying in bed, sunlight not fully up, and thought that the notes had been sounding less like instructions and more like a person actually watching you."
    scene upstairs_hall at bg_fit
    with dissolve
    with fade
    if suspicion >= 9:
        "You did not want to look at the cup this morning. But you did anyway." 
        "The tray had vanished. NIt had been replaced by an indentical one that you had not brought up yesterday."
        $ suspicion += 1
    elif suspicion >= 4:
        "The cup had turned again, ninety degrees. The same as always. But the handle was pointed at you this time."
        "This is strange."
    else:
        "You set the tray down and left without lingering. That is not the path that you want to go to."
    scene kitchen_room at bg_fit
    with dissolve
    with fade
    show voss at truecenter
    with dissolve
    if suspicion >= 9:
        v "I need you to listen to me, and not ask why."
        v "Whatever you have been noticing, stop writing it out, or saying it out loud, and stop asking Simon about it."
        hide voss 
        m "Why Voss specifically?"
        show voss at truecenter
        with dissolve
        v "Did i not tell you to not ask me why?"
        hide voss 
        $ suspicion += 2
    elif suspicion >= 4
        v "You have got that look again. The look of asking something that you should not."
        hide Voss
        m "Would you tell me if i did?"
        m "Depends on the question. Try me."
        menu:
            "Ask if Simon has always worked here.":
                m "Has Simon always worked here? Long before you did?"
                show voss at truecenter
                with dissolve
                v "That is a strange way to put up a question."
                v "Not always. There was someone before him."
                hide voss
                "It seemed like the sentence cost her something to finish."
                $ suspicion += 2
            "Do not push, ask something small.":
                hide voss
                m "Nevermind, is there anything you need help today with?"
                show voss at truecenter
                with dissolve
                v "No, go on then."
    else:
        v "Morning, sleep alright?"
        hide voss
        m "Better than the first night."
        show voss at truecenter
        with dissolve
        v "Give it time, or do not. Depends on who you ask."
        hide voss
        "She almost smiled. This was the first time you saw her nearly breaking one."
    scene main_hall at bg_fit
    with dissolve
    with fade
    "You were thinking of last night's note and turning it over."
    "You suddenly had a thought, to mentioned it directly and see who reacted or flinched."
    show simon at truecenter
    with dissolve    
    menu:
        "Ask Simon outright if he writes these notes.":
            if suspicion >= 9:
                s "..."
                hide simon
                "For the first time since you had come to work here, this was the first time that Simon did not have an answer."
                show simon at truecenter
                with dissolve
                s "That is a weird thing to ask to me. Get back to your work."
                hide simon
                $ suspicion += 3
            elif suspicion >= 4:
                s "No, why would you ask that?..."
                s "I only carry them."
                hide simon
                "He said carry, not deliver. Something sounds wrong with that..."
                $ suspicion += 2
            else:
                s "Ha? No. I could not forge them even if I wanted to. That is all him."
                hide simon
                "He just brushed it off that easily like it was not even that serious. Something might be wrong."
                $ suspicion += 1
        "Do not ask, just watch him instead.":
            "You watch and observe him for a while. Nothing much wrong."
            s "Something on your mind?"
            hide simon 
            m "No, just tired."
            show simon at truecenter
            with dissolve
            s "Go and take a rest then."
            $ suspicion += 1
    scene garden at bg_fit
    with dissolve
    with fade
    show hale at truecenter
    with dissolve
    if suspicion >= 9:
        h "You seem like a man who stopped sleeping right."
        hide Hale
        m "Kinda, maybe just a little bit."
        show hale at truecenter
        with dissolve
        h "Come here to sit for a bit. Not to talk about the house but just to sit for a bit."
        hide hale
        "It was not the kind of approach you wanted. But it was so far the kindest thing anyone ever offered you in this house."
        $ suspicion += 1
    elif suspicion >= 4:
        h "Still up asking questions everywhere?"
        hide hale
        m "Trying not to, but that is not helping much."
        show hale at truecenter 
        with dissolve
        h "Don't worry, it was like that for me too, for the first one or two years, at least."
        hide hale 
        "Those words did not sound comforting at all. Hale was shrouded with mysteries."
    else:
        "Today again? What are you doing here at the fields everyday??"
        hide hale 
        m "Just wandering about. Come to think of it, I always see you here."
        show hale at truecenter
        with dissolve
        h "Sure, wander around as long as you like."
    scene upstairs_hall
    with dissolve

    narrator "That night, the tray came back with only one note this time — but the handwriting wasn't the one you'd grown used to."

    if suspicion >= 9:
        master_note "I know you're close to understanding. I'm not going to stop you."
        master_note "I will tell you this much, freely: ask Simon what year he thinks it is. Watch his face when he answers."
    elif suspicion >= 4:
        master_note "Someone else has been leaving marks in this house besides me. You've started to notice. Good."
        master_note "I would rather you know slowly than not at all."
    else:
        master_note "Rest well tonight. Tomorrow will ask more of you than today did."

    scene bedroom at bg_fit
    with dissolve
    with fade

    narrator "Whoever was writing these — Ashworth, or something wearing his name — they were, for the first time, actively helping you instead of warning you off."

    narrator "You weren't sure yet if that was a good sign, or the most dangerous one so far."
    $ day_num = 5
    jump day_5
label day_5:
    scene bedroom at bg_fit
    with dissolve
    with fade
    if suspicion >= 9:
        mn "Ask him today."
        mn "I would do it myself, if i could."
    elif suspicion >= 4:
        mn "You have two days before the end of your first week. This mtter more than you think it does."
        mn "That is why use them carefully."
    else:
        mn "Bring the tray as usual. Otherwise, you have a quiet day infront of you."
    scene upstairs_hall at bg_fit
    with dissolve
    with fade
    if suspicion >= 9:
        "You knocked, like you have always had."
        "But this time, something knocked from the other side, a soft knock."
        "You did not go in. You were not supposed to."
    elif suspicion >= 4:
        "The tray from yesterday was gone entirely."
        "Not like the other times, where it had been left untouched."
    else:
        "It was the usual, the tray untouched."
        "You were starting to think of the unusual cup as usual now."
    scene main_hall at bg_fit
    with dissolve
    with hpunch
    show simon at truecenter
    with dissolve
    s "Good morning, you look like you have got something on your mind."
    menu:
        "Ask him what year it is.":
            m "What year is it right now?"
            "Simon laughed at that question, like he always did."
            s "What kind of question is that?"
            s "It is-"
            s "Why would you ask me that?"
            hide Simon
            "You could feel the switch in his tone, it had become a bit less certain."
            if suspicion += 9:
                m "Because I do not think that you know. I do not think you've known in a long time."
                show simon at truecenter
                with dissolve
                s "..."
                hide simon
                "He did not answer for several seconds, did not accept or deny, just quiet."
                $ suspicion += 4
            elif suspicion += 4:
                m "You do not know, do you?"
                show simon at truecenter
                with dissolve
                s "It has been a long week, things blur."
                hide simon
                "You could sense the uncertainty in the tone."
                $ suspicion += 2
            else:
                show simon at truecenter
                with dissolve
                m "Nevermind, forget that I asked."
                s "Alright, if you say so.."
                "He did not push more into the question."
                $ suspicion += 1
    scene kitchen_room at bg_fit
    with dissolve
    with fade
    if suspicion >= 9:
        m "Simon does not know what the year is."
        show voss at truecenter
        with dissolve
        v "Yeah, he would not."
        hide voss
        m "Mrs.Voss, how long has Simon actually been here?"
        show voss at truecenter
        with dissolve
        v "Longer than he should be, longer than any of us should be."
        v "He came in the same day as the owner of this house passed."
        v "I do not think that it is really a coincidence."
        v "Even though you have been here a short while, I do not think you think that either."
        $ suspicion += 3
    elif suspicion += 4:
        m "Mrs.Voss, I think there is something wrong with Simon."
        m "He could not tell me what year it is right now."
        show voss at truecenter
        with dissolve
        v "I wonder when you had noticed that."
        v "I will not explain, some things you have to figure out on your own."
        hide voss
        $ suspicion += 2
    else:
        show voss at truecenter
        with dissolve
        v "You are quiet today."
        hide voss
        m "I am just thinking."
        show voss at truecenter
        with dissolve
        v "That sounds dangerous, in a mansion like this."
        v "You should reconsider that habit maybe."
    scene garden at bg_fit
    with dissolve
    with fade
    if suspicion >= 9:
        "You did not have to ask this time. He was already waiting on the unmarked patch of ground."
        show hale at truecenter
        with dissolve
        h "You had a talk with Simon?"
        hide hale 
        m "A bit. Just a bit."
        show hale at truecenter
        with dissolve
        h "This is where they put him. Properly, I mean. Not the way that the house has been keeping him now."
        hide hale 
        "The way the house keeps him now. You did not ask any further."
        "You did not think that you were ready for the answer yet."
        $ suspicion += 3
    elif suspicion >= 4:
        show hale at truecenter
        with dissolve
        h "Youve got some look on your face today."
        h "Did anything interesting happen or something?"
        hide hale 
        m "Something like that."
        show hale at truecenter
        with dissolve
        h "Welcome to the club. I wish I could say that it gets easier haha."
        hide hale 
        "He went back to the hedges without waiting for a response."
        "It almost felt like he was escaping a conversation that he did not want to have."
    else:
        show hale at truecenter
        with dissolve
        h "It is a quiet day, isnt it?"
        h "Enjoy it, when you can at least."
        hide hale 
        "You did not ask what he meant. You were starting to understand that most of the things here were for you to understand yourself."
    scene upstairs_hall at bg_fit
    with dissolve
    with fade
    "You got a note this time which was shorter."
    "But it sounded like whoever was writing that, was running out of patience."
    mn "You asked him. Good."
    mn "All I can say now is, Simon was someone like you, he is what's left of someone who tried to help me, just like you."
    scene bedroom at bg_fit
    with dissolve
    with fade
    "This was the first time in five days, you had gotten any close to the truth."
    "You wonder if that has made him more trustworthy."
    $ day_num = 6
    jump day_6
label day_6:
    scene bedroom at bg_fit
    with dissolve
    with fade  
    mn "One day remains after this one."
    mn "You know what simon is now, but you dont know what I am, but i believe you will soon."
    mn "Come to the study tonight, regardless of what you hear inside the door."
    scene upstairs_hall at bg_fit
    with dissolve
    with fade
    "The tray from last night was untouched, but the teacup was missing."
    "You put down the new one and did not stop to see what else had been changed."
    scene kitchen_room at bg_fit
    with dissolve
    with fade
    show voss at truecenter
    with dissolve
    v "You are going in the study tonight, aren't you?"
    hide Voss
    m "How did you know?"
    show voss at truecenter
    with dissolve
    v "I can tell by your face."
    hide voss
    m "He asked me to."
    show voss at truecenter
    with dissolve
    v "I know, I have seen the same thing with three people before you."
    v "None that went down and returned changed for the better."
        










            
        


        
        
        