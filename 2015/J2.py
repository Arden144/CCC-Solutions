input = input("How are you :-) doing :-( today :-)?")

def Happy_or_Sad(input):
    if input.count(":-)") > input.count(":-("):
        return "happy"
    elif input.count(":-(") > input.count(":-)"):
        return "sad"
    elif input.count(":-(") == 0 and input.count(":-)") == 0:
        return "none"
    elif input.count(":-(") == input.count(":-)"):
        return "unsure"

print Happy_or_Sad(input)
#  Created by Alpha on 2019-12-14.
#  Copyright © 2019 Alpha. All rights reserved.