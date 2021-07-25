![Image of AI Arena](https://raw.githubusercontent.com/kurtjd/ai-arena/master/screenshot.png)

A.I. Arena: Deathmatch
=======================
A.I. Arena is a battleground where programmed bots fight to the death to earn the title of most intelligent unintelligent-agent in all of Computerdom! With few rules, there is a large degree of creativity and outside-the-box thinking required to be successful. However, with some wits and a wee bit o' luck, your potential is virtually unlimited!


How to Participate
===================
It's quite simple, really. The entire framework and engine has already been designed. All you need to do is program a bot to compete, which can be as basic or as complex as you'd like. You will find a few different script files here, however the only ones you really need to concern yourself with are main.py and BotSkeleton.py (found in the bots folder). These files have instructions in them, but to recap some of the basics:

-BotSkeleton.py contains the skeleton class which your bot will be written with. You need to save this as a new file in the bots subfolder and give it a unique filename. In the class, you will find the method do_action(). This is where a bulk of your code will go. Essentially, your bot gets to perform one of multiple actions per frame. do_action() is where you decide which action to perform.

-Your bot also needs an image to go with it. Make a 50x50 image and save it as YourBotName.jpg (yes, must be .jpg) in the bots/images folder. Make sure the filename and the bot name in the class match exactly.

-In main.py, at the top of the file, you will find some import statements. This is where you import your bot, by adding 'import bots.BotFileName'. Currently there are four pre-written test bots being imported. You can remove these, but make sure there are always exactly four bots being imported. Any more or any less will cause errors.

-Once you've written your bot's class file and and tested it in main.py, go ahead and send it to me along with your bot's image file. Remember, once the battles start, you will no longer be able to modify your bot! Make sure it's good to go before the competition begins.


Actions
=======
A.I. Arena involves a lot of tactical decision making. As previously mentioned, your bot gets to take one action per frame. It is up to you and your bot to decide on which action that might be. Below is a list of the different possible actions and a brief explanation:

MOVE:       Move one step in the x and y direction by amount specified (see BotSkeleton.py for more details).
SHOOT:      Shoot a bullet at the coordinates specified (again, see BotSkeleton.py for more details).
HEAL:       Heals one point of health every other frame. This slows down the rate of healing, otherwise bots could be invincible.
RELOAD:     Reloads one bullet every other frame. Again, this is done to slow the rate of reloading, or else taking time to reload would be negligible.
PLACE MINE: Place a mine underneath the bot. A bot will not detonate its own mines. Remember, mines can not be renewed. Once you're out, you're out!

So although you can only perform a few actions, you are free to go about in deciding how your bot chooses actions. The main rule is you just can't modify any variables besides the few I will specify next.


Modifiable Variables
====================
You are limited in which variables you may modify directly. Besides variables you create yourself, you may only modify:

self.action - The action your bot will take for the frame.
self.moveX - The percentage of move speed the bot will move in the x direction.
self.moveY - The percentage of move speed the bot will move in the y direction.
self.shootAtX - The x coordinate the bot will fire a bullet at.
self.shootAtY - The y coordinate the bot will fire a bullet at.

Please see BotSkeleton.py and bot.py for more details on the purpose of these variables.


Rules
=====
Besides the fact that you may not modify variables besides the few mentioned, there are a few other minor rules that need to be mentioned.

-If your bot is determined to cause considerable lag, it will be returned for modification. Optimization is important here.
-Any 'randomness' or any use of information that can cause the same battle to have differing outcomes, is not allowed. However, a 'pseudo-pseudo-RNG' is fine, if you use a seed that remains fixed at all times (so that means no using the time as a seed, which is commonly done).
-Generating new data into the battle, such as generating a copy of your bot to fight alongside the original.
-Using external modules. Built-in modules are okay.
-If desired, I will allow conservative use of the pygame library for the occasional special effect. Though use common sense here.

There are most likely things I'm forgetting or haven't though of. Really just use your brain here. If what you want to do seems like it may be obnoxious or boderline cheating, it probably is. If in doubt, just ask me first. I reserve the right to return a bot if I feel it is playing unfairly, even if it doesn't specifically break one of the above mentioned rules.


Frequently Asked Questions
==========================
Q: What do I need to participate?
A: Besides the files I've provided, you need Python 2.7 installed (preferrably 2.7.4) as well as the latest version of Pygame (v1.9.1)

Q: Why Python?
A: Why not? Although I'm not all that fluent in Python myself, it's a great language for this kind of thing. This competition isn't to see who can deal with memory management and segfaults the quickest, it's to see who can develop the best battle bot.

Q: Why not Python 3?
A: Honestly, I'm just more familiar with Python 2.

Q: Do I need to know how to use Pygame to participate?
A: Not at all! Pygame is just used for the back-end of the framework. However you still need to install it in order to test your bot.

Q: Where can I get Pygame?
A: http://www.pygame.org/download.shtml (Download the 1.9.1 release). The installation process is pretty straight-forward.

Q: How does this differ from other battle bot type games?
A: Those games either offer a very strict set of instructions to work with, or offer a very limited API. A.I. Arena restricts you to a few actions, however there is no 'API' and the means of deciding which action to take are only as limited as the Python language itself.

Q: How will the tournament work?
A: It will be a double elimination tournament. Each match will have four bots. The top two bots will stay in the winners bracket, while the losers will move to the losers bracket. Once the finalist of the winners bracket has been determined, the losers bracket will play out. The finalist from the losers bracket will go onto face the other finalist in a 1v1 championship series. The winners' bracket finalist must only win one match, while the losers' bracket finalist must win two to be declared champion.

Q: What is the deadline?
A: No deadline yet. I want to see how much interest there is first then decide.

Q: What do I get for winning?
A: This tournament is mainly meant for fun, but I'll throw in a $20 Amazon gift-card to the champion.

Q: How can I watch battles play out?
A: I will screen capture the battle and upload the videos to Youtube. I will also provide the source so you can run it yourself.

Q: What if my bot accidentally breaks the rules?
A: If you send me a bot that breaks the rules and I find out before the tournament begins, I will let you know so you can fix it. If I find out during the tournament, unfortunately it will be disqualified.

Q: Can I modify my bot in-between matches?
A: No. Once the tournament starts, your submission is final. Make sure you thoroughly test it before the tournament begins.

Q: Can I submit more than one bot?
A: No. One bot per participant.

Q: How will my starting position be determined?
A: You will randomly be placed in one of the four corners of the arena.

Q: How do I locate other bots, bullets, and mines on the screen?
A: Use lists specified in arena_globals.py

Q: Can I 'spy' on other bots? Can I read their variables?
A: Yes. You may read any and all variables. There are no secrets in this arena!

Q: My bot is lagging! What do I do?
A: A bit of lag is expected in something like this, and I'll admit my framework probably isn't as well designed as it could be, but excessive lag is a no-go. You'll need to either do without the code that is causing lag, or find a way to optimize it.

Q: Do I have to reveal my source code?
A: During the development phase, no. I'll be the only one seeing the source code. However, once the tournament begins, sources will be released by me with each match so people can run the battle on their own. If you aren't okay with that, then sorry, you won't be able to participate.

Q: I still don't understand what's going on here, or how to begin writing my bot...
A: Ask, ask, ask! I realize this is probably pretty confusing, so if you need clarification, just ask.

Q: My question isn't answered here!
A: Feel free to ask me. I have a feeling there will be a lot of questions at first, so I'll add to this as I go.

