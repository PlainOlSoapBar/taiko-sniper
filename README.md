# 太鼓の狙撃 - Taiko Sniper Discord Bot
太鼓（たいこ）の　狙撃（そげき）  
Taiko meaning drum, sogeki meaning sniping.  
## 🎯 About
Don-chan quit his job as a Taiko Master and became the ultimate sniper. As a side-hustle, he helps Collegiate Taiko groups keep track of sniping statistics for each member.

Within my Taiko group, we have a tradition of taking pictures _(sniping)_ of other members without their knowledge whenever we see them in public _(don't worry, we all consent to this)_. Introducing Taiko Sniper, a Discord bot that allows members to snipe each other while having their statistics tracked!  
## 🔧 Features / Previews
[ ] indicates argument, * indicates optional
<details>
<summary> Snipe </summary>

‎ 
  - Command: `/snipe [user] [image]`
  - Requires an image as proof of the snipe.

<img width="507" alt="Sniped Message" src="https://github.com/user-attachments/assets/c67996ec-46e1-49c5-9bf2-0e635be73045" />

  - `/unsnipe [user]` command for accidental snipes.
    - Currently admin-only and unsnipes from the command user's perspective, but I will likely adjust this in the future.
</details>
<details>
<summary> Statistics </summary>

 ‎ 
  - Command: `/stats [user*] [private*]`
  - Displays how many times a member has sniped or has been sniped.
  - Calculates kill/death ratio (more like snipes/sniped ratio but we're still calling it k/d).

<img width="309" alt="Statistics Message" src="https://github.com/user-attachments/assets/2960b3bc-bb92-4ead-a3d1-3095f86c49c4" />

  - By default, it is an ephemeral response, but the private argument can toggle it.
</details>

## 🚀 Setup / Deployment
### Prerequisites
- Discord Bot Token (Refer to this [guide](https://discordpy.readthedocs.io/en/stable/discord.html))
- Python (Tested on 3.11.3)
### Installation
1. Clone repo and cd into the folder.
2. Create virtual environment (MacOS version).
```bash
python -m venv venv
source venv/bin/activate
```
3. Install dependencies.
```bash
pip install -r requirements.txt
```
4. Populate the `.env` file. 
### Running the bot
1. Run the bot directly.
```bash
python3 main.py
```
2. Alternatively, run the bot in the background.
```bash
nohup python main.py &
```
3. Stop the bot via killing its process ID.
```bash
ps aux | grep main.py
kill [process id]
```

