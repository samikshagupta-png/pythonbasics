import random;


nature = [
    "🌸 Beautiful", "❄️ Cool", "🧠 Smart", "🌞 Bright", "🌿 Fresh",
    "🔥 Energetic", "🌊 Calm", "🌟 Creative", "🍃 Pure", "🌈 Cheerful",
    "😡 Angry", "👿 Evil", "🥶 Cold-hearted", "💤 Lazy", "🤥 Dishonest",
    "🤣 Funny", "🤪 Silly", "😜 Playful", "😂 Joker", "🙃 Goofy"
]
willing =True
while willing:
    NAME = input("Enter  names(comma separated) : ").split(",")
    for name in NAME:
        name = name.strip()
        n =random.randint(0,len(nature)-1)
        print(name, " :> ", nature[n])
    print("are you want to continue ")
    print("type y to continue & n to break")
    q=input()
    if q.lower() == 'y':
        willing=True
    else:
        willing=False
