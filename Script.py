class script(object):
    START_TXT = """𝙃𝙀𝙇𝙇𝙊 {},
𝙈𝙔 𝙉𝘼𝙈𝙀 𝙄𝙎 <a href=https://t.me/{}>{}</a>, ✨ 𝙄 𝘾𝘼𝙉 𝙋𝙍𝙊𝙑𝙄𝘿𝙀 𝙈𝙊𝙑𝙄𝙀𝙎 & 𝙎𝙀𝙍𝙄𝙀𝙎, 𝙅𝙐𝙎𝙏 𝘼𝘿𝘿 𝙈𝙀 𝙏𝙊 𝙔𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋 & 𝙀𝙉𝙅𝙊𝙔 ✨ 𝙄𝙁 𝙔𝙊𝙐 𝙒𝘼𝙉𝙏 𝙐𝙎𝙀 𝙈𝙀 𝙏𝙃𝙀𝙉 𝙅𝙊𝙄𝙉 𝙈𝙔 𝙐𝙋𝘿𝘼𝙏𝙀𝙎 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 & 𝙐𝙎𝙀 

𝙋𝙊𝙒𝙀𝙍𝙀𝘿 𝘽𝙔 - @Infinity_movies2"""
    HELP_TXT = """𝙃𝙀𝙔 {}
𝙃𝙀𝙍𝙀 𝙄𝙎 𝙏𝙃𝙄𝙎 𝙏𝙃𝙀 𝙃𝙀𝙇𝙋 𝙁𝙊𝙍 𝙈𝙔 𝘾𝙊𝙉𝙈𝘼𝙉𝘿𝙎."""
    ABOUT_TXT = """✯ 𝙈𝙔 𝙉𝘼𝙈𝙀: {}
✯ 𝘾𝙍𝙀𝘼𝙏𝙊𝙍: <a href=https://t.me/infinity_novies2>𝙄𝙉𝙁𝙄𝙉𝙄𝙏𝙔 𝙈𝙊𝙑𝙄𝙀𝙎</a>
✯ 𝙇𝙄𝘽𝙍𝘼𝙍𝙔: 𝙋𝙔𝙍𝙊𝙂𝙍𝘼𝙈
✯ 𝙇𝘼𝙉𝙂𝙐𝘼𝙂𝙀: 𝙋𝙔𝙏𝙃𝙊𝙉 
✯ 𝘿𝘼𝙏𝘼 𝘽𝘼𝙎𝙀: 𝙄𝙉𝙁𝙄𝙉𝙄𝙏𝙔 𝙈𝙊𝙑𝙄𝙀𝙎
✯ 𝘽𝙊𝙏 𝙎𝙀𝙍𝙑𝙀𝙍: 𝙊𝘾𝙀𝘼𝙉 𝙑𝙋𝙎
✯ 𝘽𝙐𝙄𝙇𝘿 𝙎𝙏𝘼𝙏𝙐𝙎: v4.3.9"""
    SOURCE_TXT = """<b>NOTE:</b>
- Its not an open Source bot. 
- Made By - @INFIINITY_MOVIES2

<b>DEVS:</b>
- <a href=https://t.me/infinity_movies2>INFINITY MOVIES</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/infinity_movies2)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to Bot with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
These are the extra features of Bot

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This Commands Only Works For My Admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """🗃 𝙏𝙊𝙏𝘼𝙇 𝙁𝙄𝙇𝙀𝙎: <code>{}</code>
👤 𝙏𝙊𝙏𝘼𝙇 𝙐𝙎𝙀𝙍𝙎: <code>{}</code>
👥 𝙏𝙊𝙏𝘼𝙇 𝘾𝙃𝘼𝙏𝙎: <code>{}</code>
💾 𝙐𝙎𝙀𝘿 𝙎𝙋𝘼𝘾𝙀: <code>{}</code> 𝙼𝚒𝙱
💽 𝙁𝙍𝙀𝙀 𝙎𝙋𝘼𝘾𝙀: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
