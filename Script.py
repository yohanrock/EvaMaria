class script(object):
    START_TXT = """𝗛𝗲𝗹𝗹𝗼 <b>{}</b>,
𝗠𝗬 𝗡𝗔𝗠𝗘 <a href=https://t.me/infinity_movies2bot>𝗜𝗡𝗙𝗜𝗡𝗜𝗧𝗬 𝗠𝗢𝗩𝗜𝗘𝗦</a>, ✨ 𝗜 𝗖𝗔𝗡 𝗣𝗥𝗢𝗩𝗜𝗗𝗘 𝗠𝗢𝗩𝗜𝗘𝗦 & 𝗦𝗘𝗥𝗜𝗘𝗦, 𝗝𝗨𝗦𝗧 𝗔𝗗𝗗 𝗠𝗘 𝗧𝗢 𝗬𝗢𝗨𝗥 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 & 𝗚𝗥𝗢𝗨𝗣 ✨ 𝗜𝗙 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧 𝗨𝗦𝗘 𝗠𝗘 𝗧𝗛𝗘𝗡 𝗝𝗢𝗜𝗡 𝗠𝗬 𝗨𝗣𝗗𝗔𝗧𝗘𝗦 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 & 𝗖𝗟𝗜𝗖𝗞 𝗢𝗡 𝗦𝗘𝗔𝗥𝗖𝗛 ⚡✨

𝙋𝙊𝙒𝙀𝙍𝙀𝘿 𝘽𝙔 - <a href=https://t.me/infinity_movies2>𝗜𝗡𝗙𝗜𝗡𝗜𝗧𝗬 𝗠𝗢𝗩𝗜𝗘𝗦</a>"""
    HELP_TXT = """𝗛𝗘𝗬 <b>{}</b>
𝗛𝗘𝗥𝗘 𝗜𝗦 𝗧𝗛𝗘 𝗛𝗘𝗟𝗣 𝗙𝗢𝗥 𝗠𝗬 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦."""
    ABOUT_TXT = """✯ 𝗠𝗬 𝗡𝗔𝗠𝗘 : <a href=https://t.me/infinity_movies2bot>𝗜𝗡𝗙𝗜𝗡𝗜𝗧𝗬 𝗠𝗢𝗩𝗜𝗘𝗦</a>
✯ 𝗖𝗥𝗘𝗔𝗧𝗢𝗥: <a href=https://t.me/infinity_movies2>𝗜𝗡𝗙𝗜𝗡𝗜𝗧𝗬 𝗠𝗢𝗩𝗜𝗘𝗦</a>
✯ 𝗟𝗜𝗕𝗥𝗔𝗥𝗬: 𝗣𝗬𝗥𝗢𝗚𝗥𝗔𝗠
✯ 𝗟𝗔𝗡𝗚𝗨𝗔𝗚𝗘: 𝗣𝗬𝗧𝗛𝗢𝗡
✯ 𝗗𝗔𝗧𝗔 𝗕𝗔𝗦𝗘: 𝗜𝗡𝗙𝗜𝗡𝗜𝗧𝗬 𝗠𝗢𝗩𝗜𝗘𝗦
✯ 𝗕𝗢𝗧 𝗦𝗘𝗥𝗩𝗘𝗥: 𝗩𝗣𝗦
✯ 𝗕𝗨𝗜𝗟𝗗 𝗦𝗧𝗔𝗧𝗨𝗦: 𝗩𝟭.𝟮.𝟰"""
    SOURCE_TXT = """<b>𝗡𝗢𝗧𝗘:</b>
- Its not an open Source bot. 
- 𝗠𝗔𝗗𝗘 𝗕𝗬 - <a href=https://t.me/infinity_movies2>𝗜𝗡𝗙𝗜𝗡𝗜𝗧𝗬 𝗠𝗢𝗩𝗜𝗘𝗦</a>

<b>𝗗𝗘𝗩𝗦:</b>
- <a href=https://t.me/infinity_movies2>𝗜𝗡𝗙𝗜𝗡𝗜𝗧𝗬 𝗠𝗢𝗩𝗜𝗘𝗦</a>"""
    MANUELFILTER_TXT = """Help: <b>𝗙𝗜𝗟𝗧𝗘𝗥𝗦</b>

- Filter is the feature were users can set automated replies for a particular keyword and Bot will respond whenever a keyword is found the message

<b>𝗡𝗢𝗧𝗘:</b>
1. Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 𝗔𝗡𝗗 𝗨𝗦𝗔𝗚𝗘:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>𝗕𝗨𝗧𝗧𝗢𝗡𝗦</b>

- Bot Supports both url and alert inline buttons.

<b>𝗡𝗢𝗧𝗘:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>𝗨𝗥𝗟 𝗕𝗨𝗧𝗧𝗢𝗡𝗦:</b>
<code>[Button Text](buttonurl:https://t.me/infinity_movies2)</code>

<b>𝗔𝗟𝗘𝗥𝗧 𝗕𝗨𝗧𝗧𝗢𝗡𝗦:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>𝗔𝗨𝗧𝗢 𝗙𝗜𝗟𝗧𝗘𝗥</b>

<b>𝗡𝗢𝗧𝗘:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to Bot with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>𝗖𝗢𝗡𝗡𝗘𝗖𝗧𝗜𝗢𝗡</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>𝗡𝗢𝗧𝗘:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 𝗔𝗡𝗗 𝗨𝗦𝗔𝗚𝗘:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>𝗘𝗫𝗧𝗥𝗔 𝗠𝗢𝗗𝗨𝗟𝗘𝗦</b>

<b>𝗡𝗢𝗧𝗘:</b>
These are the extra features of Bot

<b>𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 𝗔𝗡𝗗 𝗨𝗦𝗔𝗚𝗘:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>𝗔𝗗𝗠𝗜𝗡 𝗠𝗢𝗗𝗦</b>

<b>𝗡𝗢𝗧𝗘:</b>
This Commands Only Works For My Admins

<b>𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 𝗔𝗡𝗗 𝗨𝗦𝗔𝗚𝗘:</b>
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
    STATUS_TXT = """🗃 𝗧𝗢𝗧𝗔𝗟 𝗙𝗜𝗟𝗘𝗦: <code>{}</code>
👤 𝗧𝗢𝗧𝗔𝗟 𝗨𝗦𝗘𝗥𝗦: <code>{}</code>
👥 𝗧𝗢𝗧𝗔𝗟 𝗖𝗛𝗔𝗧𝗦: <code>{}</code>
💾 𝗨𝗦𝗘𝗗 𝗦𝗣𝗔𝗖𝗘: <code>{}</code> GB
💽 𝗙𝗥𝗘𝗘 𝗦𝗣𝗔𝗖𝗘: <code>{}</code> GB"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
