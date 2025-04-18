# 太鼓の狙撃 - Taiko Sniper Discord Bot
太鼓（たいこ）の　狙撃（そげき）  
Taiko meaning drum, sogeki meaning sniping.  
## 🎯 About
Some context: Within my Taiko group, we have a tradition of taking pictures _(sniping)_ of other members without their knowledge whenever we see them in public _(don't worry, we all consent to this)_. Thus, I am building a Discord bot that allows members to snipe each other while having their statistics tracked!  
## 🔧 Features / Previews
[ ] indicates argument, * indicates optional
<details>
<summary> Snipe </summary>

‎ 
  - Command: `/snipe [user] [image]`
  - Requires an image as proof of the snipe.

![Sniped Message](https://github.com/user-attachments/assets/d18865db-65e2-4c31-af76-00e7eb4a35a2)
</details>
<details>
<summary> Statistics </summary>

 ‎ 
  - Command: `/stats [user*]`
  - Displays how many times a member has sniped or has been sniped.

![Statistics Message](https://github.com/user-attachments/assets/cf908895-98ff-4f29-b268-b04c22abe54a)
</details>

## 📝 Plans
- /help command
- Leaderboard (maybe with charts / diagrams).
- Fun statistics such as who snipes the most and who gets sniped the most.
- Optional parameter for type of snipe (e.g. backshot--literally right behind them).
- Customizable(?) rules.
- Option to opt out.
- Shared data across different Taiko servers?
- Cleanup dependencies / requirements.txt.
## 🚀 Setup / Deployment
### Prerequisites
- Discord Bot Token (Refer to this [guide](https://discordpy.readthedocs.io/en/stable/discord.html))
- Python (Tested on 3.11.3)
### Installation
1. Clone repo and cd into the folder.
2. Install dependencies with `pip install -r requirements.txt`.
3. Run the bot with `python3 bot.py`.  
