from os import _exit
from discord import Client, GroupChannel

group_to_leave = None
token = ""

class BotClient(Client):
    async def on_ready(self):
        print(f"[+] Logged on as: {self.user}")
        left_groups = 0

        for channel in self.private_channels:
            if isinstance(channel, GroupChannel):
                if (group_to_leave and group_to_leave in channel.name) or not group_to_leave:
                    try:
                        await channel.leave()
                        left_groups += 1
                    except:
                        pass 

        print(f"[?] Left {left_groups:,} group chats")
        _exit(0)

if __name__ == "__main__":
    if not token:
        token = input("[*] Discord token: ").strip()
    else:
        print("[?] Discord token already exists")

    if not group_to_leave:
        print("[?] Answering no to the following question will result in leaving all groups!")
        q = input("[*] Would you like to leave group chats with a specific name? [y/N]: ").strip()

        if q and q[0].lower() == "y":
            group_to_leave = input("[*] Please enter the group name: ").strip()

    BotClient().run(token, bot=False)
