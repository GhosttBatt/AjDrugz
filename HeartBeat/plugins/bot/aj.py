
from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from HeartBeat import app
from time import time
import asyncio
from HeartBeat.utils.extraction import extract_user

# Define a dictionary to track the last message timestamp for each user
user_last_message_time = {}
user_command_count = {}
# Define the threshold for command spamming (e.g., 20 commands within 60 seconds)
SPAM_THRESHOLD = 2
SPAM_WINDOW_SECONDS = 5

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

SHAYRI = [ "_°𝐈 𝐃𝐨ŋ’ʈ 𝐇ɑ𝐯ɘ αŋ 𝐀ʈʈııʈʋ𝐝 𝐉ꪊ𝐬ʈ 𝐀 ℘ɘɽ𝐬𝗼ŋ𝐀ɭıʈ𝐘 ʈhɑʈ 𝐘𝐎ʋ ɕɑn'ʈ ʜαŋdɭɘ 🍁",
"★ I Doŋ’ʈ Nɘɘd [😈] Yoʋɽ Aʈʈııʈʋdɘ 🔥 Bɘɕɑʋsɘ I Hɑvɘ Ɱɣ [🍫] Owŋ -🍁",
"ßɑbɣ Don'ʈ Bə Jəɑɭous ▁ıı'm Hoʈ ♥¹▁ıʈ's Noʈ Mɑh Fɑuɭʈ ☆|▁🐬",
"_ı'ɱ ɭııʞƏ ɑ Bʋʈʈəɽʆɭɣ🦋 Pɽəʈʈɣ ✨ʈ❍ SəƏ 🌝 Ħɑɽd ʈ❍ Cɑʈcɦ _•",
" - I 🌼🍂 Ʈɽɪd Ʈ❍ Sᴍɪɭə Bᴜʈʈ Mɣ Eɣəꜱ Caƞ'ʈ Ħɪdə Mɣ Fəəɭɪƞʛs : ) 🍁",
"💅🍁•||☆I Ɗ❍n't ŊƏƏɖ ʈ❍ Əxpɭɑıɴ Ɱɣ Sɚɭf Bəɕɑʊsɘ I Kɳ❍w I ʌɱ Ɽıʛʜʈ ☆",
"★= [ ^···^ Yoʋ Ŋəvəɽ Hʋɽʈ ❤ Ɱɘ Wııthoʋt'l Ɱɣ Pəɽɱııssııoŋ ^···^ ] *☆🍁",
"-🍁 Soməʈııməs ' 🌿 ıʈ'x Bəttəɽ ʈo sʈαɣ Sıɭəŋʈ Aŋd Smıɭə - ;))",
"𝐒𝛊‌𝅮‌ℓ𝛆ηƈ😌🤕 ɪs η𝗼𝚪‌ 𝗔፝ᥣwʌ𝚢‌𝗦 𝜩ɢ𝗼 !! 𝗦❍ɱ‌ꫀ𝚪‌ιmꫀs፝֟֟‌🥹😔 ιꪀ 𝚮ɪ∂єs፝֟֟‌_••☆★  𝗔α 𝐋𝗼𝚪‌ 𝚹ƒƒ 𝚸‌ᴀιꪀ...🥹🙂‍↕️",
"𝐈 𝗗oɴ'𝚪‌🧸🌾 །༨ɴo𝘄 𝚮o𝘄 𝚪‌o 𝚬𝐱ᴘᥣaιɴ🌸 𝚳ɣ 𝚸‌ɑıɴ 💯",
"🌺▁❥┼ßəʌuʈɣ Is Nറʈ lŋ ʈɦə Fʌ𝖼ə ßəʌuʈɣ ls Ʌ ɭıɢɦʈ Iŋ ʈɦə Ħəʌɽʈ _'🍁 🤍 🕊️",
"♥️𝆺𝅥⃝🦋 ‌⃪‌ ᷟ•×__👑°•★᪳𝗜n 𝗧he 𝗪orɭd of 𝗧emporary 𝗢ptıoηs💫 Yo𝞄⃕ 𝗔re 𝗠y Perma𝝶eηt 𝗖hoıce ━━━•°🦋",
"🌦⃝⃪⃮⃕⃔🌷➥𝐃ᴏɴT_🅑elɪᴠǝ🍃 #𝐀ɴʏonǝ🎋𝐏eo‌‌ᴘʟe 𝐂ᴀɴ #𝐂ʜange⛈️𝐀ny_time",
"_°𝐓ᴡɩŋĸɭɘ 𝐓ᴡɩŋĸɭɘ 𝐋ɩᴛᴛɭɘ 𝐒ᴛʌʀ✨𝐈 𝐃ᴏɴ'ᴛ 𝐂ᴀʀᴇ 𝐀ʙᴏᴜᴛ ᴜʀ 𝐎ᴘɪɴɪᴏɴ ɩŋ ɱƴ 𝐋ʏғ 𝐘ʀʀ_°🥀🦋",
"||°🤍 - 𝐈𝖿 𝐘❍𝗎𝗋 𝐄ɕ❍ 𝐒ρǝǝƙꜱ 𝐖𝗍𝗁 𝐌ǝ 𝐓ɦǝղ 𝐌ɣ 𝐀𝗍𝗍𝗂𝗍𝗎ɗǝ 𝐖ιʅʅ 𝐑ǝρ𝗅α¢є 𝐘❍𝗎 ❣️",
"𝘿𝙖𝙢𝙖𝙜𝙚𝙙 𝙥𝙚𝙤𝙥𝙡𝙚 𝙖𝙧𝙚 𝙢𝙤𝙧𝙚 𝙙𝙖𝙣𝙜𝙚𝙧𝙤𝙪𝙨 𝙗𝙚𝙘𝙖𝙪𝙨𝙚 𝙩𝙝𝙚𝙮 𝙠𝙣𝙤𝙬 𝙝𝙤𝙬 𝙩𝙤 𝙨𝙪𝙧𝙫𝙞𝙫𝙚 😈😈🤘💔",
"𝘾𝙤𝙢𝙚 𝙗𝙖𝙘𝙠 𝙖𝙣𝙮𝙩𝙞𝙢𝙚, 𝙀𝙫𝙚𝙣 𝙖𝙛𝙩𝙚𝙧 𝙮𝙚𝙖𝙧𝙨. 𝙄'𝙡𝙡 𝙗𝙚 𝙬𝙖𝙞𝙩𝙞𝙣𝙜 𝙛𝙤𝙧 𝙮𝙤𝙪... 𝙒𝙞𝙩𝙝 𝙩𝙝𝙚 𝙨𝙖𝙢𝙚 𝙛𝙚𝙚𝙡𝙞𝙣𝙜. 𝙉𝙤 𝙢𝙖𝙩𝙩𝙚𝙧 𝙝𝙤𝙬 𝙥𝙖𝙞𝙣𝙛𝙪𝙡 𝙞𝙩 𝙞𝙨... 💝🔥",
"Im ƞOʈ A bαd PεrsOƞ •   SıʈuαʈıOƞ Mαkes mε bαd._• 😻😈",
"᯽𖡩 𝐃❍n’ʈ 𝐇aʈə🤞𝐌ə 😈 𝐉usʈ✌️𝐆əʈ 👀 𝐓❍ ♥️ 𝐊n❍ω🤞𝐌ə 🥶 𝐅ɩɽsʈ 𖡩᯽]]••┼●",
"Smıɭə Is ʈhə Bəsʈ Mədıcın for αnɣPɽoblʋm  So αlwαɣs Kəəp smılıng",
"🍁Doŋ't sʌcʀɩʆɩcɘ ƴoʋʀ sɭɘɘp ʆoʀ soɱɘoŋɘ wʜo ĸɩɭɭɘɗ ƴoʋʀ ɗʀɘʌɱs ●─┼✪♥",
"- 𝐈 [ 𝐊noᏇ ] 𝐈 ɑɱ [ 𝐀Ꮗesome ] ♥ 𝐬o 𝐈 don’ʈ 𝐂ɑre 𝐀bouʈ 𝐘our 𝐎pinion 🦋",
"^_𝐈 𝐃𝗈𝗇'𝗍 𝐍𝖾𝖾𝖽 𝐘𝗈𝗎𝗋 𝐎𝗉𝗂𝗇𝗂𝗈𝗻 𝐂𝗈𝗓' 𝐌𝗒 𝐌𝗂𝗋𝗋𝗈𝗋 𝐒𝖺𝗒𝗌 𝐈'𝗆 𝐀𝗐𝖾𝗌𝗈𝗆𝖾 «|3",
"Focus On ThƏ Posıtıvə, Happınəss Wıll Chasə YƏw'h Around ッ_🍁",
"-♡ 𝐈 Ꮗ𝐢𝐥𝐥 ƞə𝐯ə𝐫 𝐜ʜɑƞ𝐠ə 𝐦ɣ 𝐅əə𝐥𝐢ƞ𝐠𝐬 𝐅𝐨𝐫 ɣ❍ʋ - 🤍 ★ #ɭossɘʀ <||3 𝐗‌‌‌ᴅ ♡",
"˚༊° Doη'ʈ Belıv'Ə Aηɣoη'ə ♡- Peopl'Ə Cɑη Chɑηg'Ə Aηɣtıм'ə - °🦋°",
"★☆••__[[ ɭOvə ɱə Oɽ Haʈə ɱə Bʋʈ Doŋ'ʈ Pɭaɣ Wıʈh ɱə•• ]]••☆★┼",
"_ ɱƔ aƮƮīīƮuDә is ɼәFɭә𝙲Ʈīīoƞ oF ɱƔ кƞoᏇɭәDGә ƞoƮ ɱƔ әGo 💙",
"¬‌ if Ɣou don'ʈ ɭīīke Mə , not Mɣ proßɭem , iʈ's Ɣours ßaßie'h🚶🏼‍♀️",
"シ||Smılə ıs ʈhə kəƔ, thaʈ fiʈs ʈhə ɭѳck Ѳf ƐvərɣbdƔ's hɛarʈ😘🥀",
"✨𝐈 𝐍əəɖ 𝐍əɰ 𝐇ɑʈəɽs 𝐓ɧə 𝐎ɭɖ 𝐎ηə 𝐁əɕɑɱə 𝐌ɣ 𝐅ɑηs• 🍁🩸<|3",
"_ I'm hɑppƔ SīīnɕƏ I hāvƏ Sʈറppəd 🍀 Əxpɚɕʈīīnɠ Fɽറm റʈhəɽ -ıı 🥂",
"𝐈 𝐃ση'ᴛ 𝐂αʀə 𝐖ʜσ 𝐈 𝐋σsᴛ , 𝐈 𝐇αᴠə 𝐁əəη 𝐑əαɭ 𝐓σ 𝐄ᴠəʀყʙσᴅყ __:🦋 🤧",
"𝐈ϝ 𝐈 𝐃ҽʅҽƚҽ 𝐘συɾ 𝐍υɱႦҽɾ,🔵 𝐘συ’ɾҽ 𝐁αʂιƈα𝔩𝔩ყ 𝐃ҽ𝕝ҽƚҽԀ 𝐅ɾσɱ 𝐌ყ 𝐋ιϝҽ.🔴🖕",
"𝗠ɣ 𝐀ʈʈıʈʋɗƏ 𝐈s 𝐀 𝐑Əsʋɭʈ ❍ʆ 𝐘❍ʋɽ 𝐀ᴄʈı❍ŋ .•_•👑:))°",
"𝕾⃪𝗺İ❘⃪ә 𝗜⃪𝘀 𝗺⃪𝝲 𝕾⃪𝘁𝝲❘ә..😊.𝝰⃪𝘁𝘁İ𝘁𝘂⃪𝗱ә 𝗜⃪𝘀 𝗺⃪𝝲 𝐏⃪𝝰𝘀𝘀İ⃪𝞂𝝶..",
"🤍᪳_𝐘𝐨u 𝗔rƏ 𝕾𝗼 𝗔w⃫ ə𝛅❍мə 𝗧ʜ𝝰ʈ, 𝗠y 𝗠i𝗱𝗱ɭə 𝐅iη𝗴ər 𝕾𝝰ɭ𝞄⃕𝘁e𝛅 ϓ𝗼u.....🖕😂",
"↑×͜×⋆★°𝗺y 𝗲ϓə𝛅 𝗮r𝗲 𝗶ɳ ɭѳ⃔ѵə 𝘄iʈʜ ϒѳ𝞄⃕𝗿⵿ 𝕾ϻ⃕ıɭƏ__°♡👀🍫✨",
"🍒▬̻ꙺ▬̻ⷭ Ɲo ❍ɴǝ  𝙳ɩɘ  Vɩꭆɢɩƞ 💦  𝗔ℓᴘʜᴧ Ƒʋɕ͜𝙺s* 🤙  Ɛⱱǝɼɣօռǝ__🍃 ✨💫",
 ]

# Command
SHAYRI_COMMAND = ["aj", "ajlovely", "ajlove"]

@app.on_message(
    filters.command(SHAYRI_COMMAND)
    & filters.group
    )
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(SHAYRI),
    )

@app.on_message(
    filters.command(SHAYRI_COMMAND)
    & filters.private
    )
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(SHAYRI),
    )
