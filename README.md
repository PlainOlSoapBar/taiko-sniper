# ▄︻デ══━一
太鼓 (たいこ) の 狙撃 (そげき)  
Taiko meaning drum, sogeki meaning sniping.
## About
> Don-chan quit his job as a Taiko Master and became the ultimate sniper.  
> As a side-hustle, he helps Collegiate Taiko groups keep track of sniping statistics for each member.

Within my Taiko group, we have a tradition of taking pictures (sniping) of other members without their knowledge whenever we see them in public (obviously with consent). This Discord bot allows members to snipe each other while having their statistics tracked!  
## Example Features / Previews
[ ] indicates argument, * indicates optional
<details>
<summary> Snipe </summary>

‎ 
  - `/snipe [user] [image]`
    - Requires an image as proof of the snipe.

<img width="507" alt="Sniped Message" src="https://github.com/user-attachments/assets/c67996ec-46e1-49c5-9bf2-0e635be73045" />

  - `/unsnipe [user]`
    - Undos an accidental snipe.
</details>
<details>
<summary> Statistics </summary>

 ‎ 
  - `/stats [user*] [private*]`
    - Displays how many times a member has sniped or has been sniped.
    - Calculates kill/death ratio (more like snipes/sniped ratio but we're still calling it k/d).

<img width="309" alt="Statistics Message" src="https://github.com/user-attachments/assets/2960b3bc-bb92-4ead-a3d1-3095f86c49c4" />

  - By default, it is an ephemeral response, but the private argument can toggle it.
</details>
<details>
<summary> Leaderboards *WIP* </summary>

 ‎ 
  - haven't started working on this
</details>
<details>
<summary> Consent </summary>

 ‎ 
  - Technically will grant immunity to sniping, but I hope that by honor code people won't abuse this.
  - `/consent`
    - Before participating, members need to "opt-in" by running this command. Otherwise, they will not be able to use the bot or be sniped.
  - `/unconsent`
    - Revokes consent.
  - `/checkconsent [user*]`
    - Checks a user's consent status.
</details>

## Setup / Deployment
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
python main.py
```
2. Alternatively, run the bot in the background.
```bash
nohup python main.py &
```
3. If you use the 2nd option, stop the bot by killing its process ID.
```bash
ps aux | grep main.py
```
```bash
kill [process id]
```

