rom HeartBeat import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🦋🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ "_°𝐈 𝐃𝐨ŋ’ʈ 𝐇ɑ𝐯ɘ αŋ 𝐀ʈʈııʈʋ𝐝 𝐉ꪊ𝐬ʈ 𝐀 ℘ɘɽ𝐬𝗼ŋ𝐀ɭıʈ𝐘 ʈhɑʈ 𝐘𝐎ʋ ɕɑn'ʈ ʜαŋdɭɘ 🍁",
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
"m ƞOʈ A bαd PεrsOƞ •   SıʈuαʈıOƞ Mαkes mε bαd._• 😻😈",
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
"•✦ 𝐎ɴᴄᴇ 𝐘ᴏᴜ 𝐋ᴏᴏsᴇ 𝐌ᴇ, 𝐘ᴏᴜ 𝐖ɪʟʟ 𝐍ᴇᴠᴇʀ 𝐆ᴇᴛ 𝐌ᴇ 𝐀ɢᴀɪɴ👆🏻♥︎<|3",
"𝗠ɣ 𝐀ʈʈıʈʋɗƏ 𝐈s 𝐀 𝐑Əsʋɭʈ ❍ʆ 𝐘❍ʋɽ 𝐀ᴄʈı❍ŋ .•_•👑:))°",
"𝕾⃪𝗺İ❘⃪ә 𝗜⃪𝘀 𝗺⃪𝝲 𝕾⃪𝘁𝝲❘ә..😊.𝝰⃪𝘁𝘁İ𝘁𝘂⃪𝗱ә 𝗜⃪𝘀 𝗺⃪𝝲 𝐏⃪𝝰𝘀𝘀İ⃪𝞂𝝶..",
"🤍᪳_𝐘𝐨u 𝗔rƏ 𝕾𝗼 𝗔w⃫ ə𝛅❍мə 𝗧ʜ𝝰ʈ, 𝗠y 𝗠i𝗱𝗱ɭə 𝐅iη𝗴ər 𝕾𝝰ɭ𝞄⃕𝘁e𝛅 ϓ𝗼u.....🖕😂",
"↑×͜×⋆★°𝗺y 𝗲ϓə𝛅 𝗮r𝗲 𝗶ɳ ɭѳ⃔ѵə 𝘄iʈʜ ϒѳ𝞄⃕𝗿⵿ 𝕾ϻ⃕ıɭƏ__°♡👀🍫✨",
"🍒▬̻ꙺ▬̻ⷭ Ɲo ❍ɴǝ  𝙳ɩɘ  Vɩꭆɢɩƞ 💦  𝗔ℓᴘʜᴧ Ƒʋɕ͜𝙺s* 🤙  Ɛⱱǝɼɣօռǝ__🍃 ✨💫",
]

VC_TAG = [ "**❅ ɪғ ʏᴏᴜ ᴅᴏ ɴᴏᴛ sᴛᴇᴘ ғᴏʀᴡᴀʀᴅ ʏᴏᴜ ᴡɪʟʟ ʀᴇᴍᴀɪɴ ɪɴ ᴛʜᴇ sᴀᴍᴇ ᴘʟᴀᴄᴇ.**",
         "**❅ ʟɪғᴇ ɪs ʜᴀʀᴅ ʙᴜᴛ ɴᴏᴛ ɪᴍᴘᴏssɪʙʟᴇ.**",
         "**❅ ʟɪғᴇ’s ᴛᴏᴏ sʜᴏʀᴛ ᴛᴏ ᴀʀɢᴜᴇ ᴀɴᴅ ғɪɢʜᴛ.**",
         "**❅ ᴅᴏɴ’ᴛ ᴡᴀɪᴛ ғᴏʀ ᴛʜᴇ ᴘᴇʀғᴇᴄᴛ ᴍᴏᴍᴇɴᴛ ᴛᴀᴋᴇ ᴍᴏᴍᴇɴᴛ ᴀɴᴅ ᴍᴀᴋᴇ ɪᴛ ᴘᴇʀғᴇᴄᴛ.**",
         "**❅ sɪʟᴇɴᴄᴇ ɪs ᴛʜᴇ ʙᴇsᴛ ᴀɴsᴡᴇʀ ᴛᴏ sᴏᴍᴇᴏɴᴇ ᴡʜᴏ ᴅᴏᴇsɴ’ᴛ ᴠᴀʟᴜᴇ ʏᴏᴜʀ ᴡᴏʀᴅs.**",
         "**❅ ᴇᴠᴇʀʏ ɴᴇᴡ ᴅᴀʏ ɪs ᴀ ᴄʜᴀɴᴄᴇ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ʟɪғᴇ.**",
         "**❅ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ʟɪғᴇ, ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ᴘʀɪᴏʀɪᴛɪᴇs.**",
         "**❅ ʟɪғᴇ ɪs ᴀ ᴊᴏᴜʀɴᴇʏ, ɴᴏᴛ ᴀ ʀᴀᴄᴇ..**",
         "**❅ sᴍɪʟᴇ ᴀɴᴅ ᴅᴏɴ’ᴛ ᴡᴏʀʀʏ, ʟɪғᴇ ɪs ᴀᴡᴇsᴏᴍᴇ.**",
         "**❅ ᴅᴏ ɴᴏᴛ ᴄᴏᴍᴘᴀʀᴇ ʏᴏᴜʀsᴇʟғ ᴛᴏ ᴏᴛʜᴇʀs ɪғ ʏᴏᴜ ᴅᴏ sᴏ ʏᴏᴜ ᴀʀᴇ ɪɴsᴜʟᴛɪɴɢ ʏᴏᴜʀsᴇʟғ.**",
         "**❅ ɪ ᴀᴍ ɪɴ ᴛʜᴇ ᴘʀᴏᴄᴇss ᴏғ ʙᴇᴄᴏᴍɪɴɢ ᴛʜᴇ ʙᴇsᴛ ᴠᴇʀsɪᴏɴ ᴏғ ᴍʏsᴇʟғ.**",
         "**❅ ʟɪғᴇ ɪs ʟɪᴋᴇ ɪᴄᴇ ᴇɴᴊᴏʏ ɪᴛ ʙᴇғᴏʀᴇ ɪᴛ ᴍᴇʟᴛs.**",
         "**❅ ʙᴇ ғʀᴇᴇ ʟɪᴋᴇ ᴀ ʙɪʀᴅ.**",
         "**❅ ɴᴏ ᴏɴᴇ ɪs ᴄᴏᴍɪɴɢ ᴛᴏ sᴀᴠᴇ ʏᴏᴜ. ᴛʜɪs ʟɪғᴇ ᴏғ ʏᴏᴜʀ ɪs 100% ʏᴏᴜʀ ʀᴇsᴘᴏɴsɪʙɪʟɪᴛʏ..**",
         "**❅ ʟɪғᴇ ᴀʟᴡᴀʏs ᴏғғᴇʀs ʏᴏᴜ ᴀ sᴇᴄᴏɴᴅ ᴄʜᴀɴᴄᴇ. ɪᴛ’s ᴄᴀʟʟᴇᴅ ᴛᴏᴍᴏʀʀᴏᴡ.**",
         "**❅ ʟɪғᴇ ʙᴇɢɪɴs ᴀᴛ ᴛʜᴇ ᴇɴᴅ ᴏғ ʏᴏᴜʀ ᴄᴏᴍғᴏʀᴛ ᴢᴏɴᴇ.**",
         "**❅ ᴀʟʟ ᴛʜᴇ ᴛʜɪɴɢs ᴛʜᴀᴛ ʜᴜʀᴛ ʏᴏᴜ, ᴀᴄᴛᴜᴀʟʟʏ ᴛᴇᴀᴄʜ ʏᴏᴜ.**",
         "**❅ ʟɪғᴇ ɪs ʟɪᴋᴇ ᴀ ᴄᴀᴍᴇʀᴀ. sᴏ ғᴀᴄᴇ ɪᴛ ᴡɪᴛʜ ᴀ sᴍɪʟᴇ.**",
         "**❅ ʟɪғᴇ ɪs 10% ᴏғ ᴡʜᴀᴛ ʜᴀᴘᴘᴇɴs ᴛᴏ ʏᴏᴜ ᴀɴᴅ 90% ᴏғ ʜᴏᴡ ʏᴏᴜ ʀᴇsᴘᴏɴᴅ ᴛᴏ ɪᴛ.**",
         "**❅ ʟɪғᴇ ᴀʟᴡᴀʏs ᴏғғᴇʀs ʏᴏᴜ ᴀ sᴇᴄᴏɴᴅ ᴄʜᴀɴᴄᴇ. ɪᴛ’s ᴄᴀʟʟᴇᴅ ᴛᴏᴍᴏʀʀᴏᴡ.**",
         "**❅ ɴᴏ ᴏɴᴇ ɪs ᴄᴏᴍɪɴɢ ᴛᴏ sᴀᴠᴇ ʏᴏᴜ. ᴛʜɪs ʟɪғᴇ ᴏғ ʏᴏᴜʀ ɪs 100% ʏᴏᴜʀ ʀᴇsᴘᴏɴsɪʙɪʟɪᴛʏ..**",
         "**❅ ʟɪғᴇ ɪs ɴᴏᴛ ᴀɴ ᴇᴀsʏ ᴛᴀsᴋ.**",
         "**❅ ʟɪғᴇ ɪs ᴀ ᴡᴏɴᴅᴇʀғᴜʟ ᴀᴅᴠᴇɴᴛᴜʀᴇ.**",
         "**❅ ʟɪғᴇ ʙᴇɢɪɴs ᴏɴ ᴛʜᴇ ᴏᴛʜᴇʀ sɪᴅᴇ ᴏғ ᴅᴇsᴘᴀɪʀ.**",
         "**❅ ʟɪғᴇ ɪs ɴᴏᴛ ᴀ ᴘʀᴏʙʟᴇᴍ ᴛᴏ ʙᴇ sᴏʟᴠᴇᴅ ʙᴜᴛ ᴀ ʀᴇᴀʟɪᴛʏ ᴛᴏ ʙᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇᴅ.**",
         "**❅ ʟɪғᴇ ᴅᴏᴇs ɴᴏᴛ ʜᴀᴠᴇ ᴀ ʀᴇᴍᴏᴛᴇ; ɢᴇᴛ ᴜᴘ ᴀɴᴅ ᴄʜᴀɴɢᴇ ɪᴛ ʏᴏᴜʀsᴇʟғ.**",
         "**❅ sᴛᴀʀᴛ ᴛʀᴜsᴛɪɴɢ ʏᴏᴜʀsᴇʟғ, ᴀɴᴅ ʏᴏᴜ’ʟʟ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ʟɪᴠᴇ.**",
         "**❅ ʜᴇᴀʟᴛʜ ɪs ᴛʜᴇ ᴍᴏsᴛ ɪᴍᴘᴏʀᴛᴀɴᴛ ɢᴏᴏᴅ ᴏғ ʟɪғᴇ.**",
         "**❅ ᴛɪᴍᴇ ᴄʜᴀɴɢᴇ ᴘʀɪᴏʀɪᴛʏ ᴄʜᴀɴɢᴇs.**",
         "**❅ ᴛᴏ sᴇᴇ ᴀɴᴅ ᴛᴏ ғᴇᴇʟ ᴍᴇᴀɴs ᴛᴏ ʙᴇ, ᴛʜɪɴᴋ ᴀɴᴅ ʟɪᴠᴇ.**",
         "**❅ ʙᴇ ᴡɪᴛʜ sᴏᴍᴇᴏɴᴇ ᴡʜᴏ ʙʀɪɴɢs ᴏᴜᴛ ᴛʜᴇ ʙᴇsᴛ ᴏғ ʏᴏᴜ.**",
         "**❅ ʏᴏᴜʀ ᴛʜᴏᴜɢʜᴛs ᴀʀᴇ ʏᴏᴜʀ ʟɪғᴇ.**",
         "**❅ ᴘᴇᴏᴘʟᴇ ᴄʜᴀɴɢᴇ, ᴍᴇᴍᴏʀɪᴇs ᴅᴏɴ’ᴛ.**",
         "**❅ ᴏᴜʀ ʟɪғᴇ ɪs ᴡʜᴀᴛ ᴡᴇ ᴛʜɪɴᴋ ɪᴛ ɪs.**",
         "**❅ ʟɪɢʜᴛ ʜᴇᴀʀᴛ ʟɪᴠᴇs ʟᴏɴɢᴇʀ.**",
         "**❅ ᴅᴇᴘʀᴇssɪᴏɴ ᴇᴠᴇɴᴛᴜᴀʟʟʏ ʙᴇᴄᴏᴍᴇs ᴀ ʜᴀʙɪᴛ.**",
         "**❅ ʟɪғᴇ ɪs ᴀ ɢɪғᴛ. ᴛʀᴇᴀᴛ ɪᴛ ᴡᴇʟʟ.**",
         "**❅ ʟɪғᴇ ɪs ᴡʜᴀᴛ ᴏᴜʀ ғᴇᴇʟɪɴɢs ᴅᴏ ᴡɪᴛʜ ᴜs.**",
         "**❅ ᴡʀɪɴᴋʟᴇs ᴀʀᴇ ᴛʜᴇ ʟɪɴᴇs ᴏғ ʟɪғᴇ ᴏɴ ᴛʜᴇ ғᴀᴄᴇ.**",
         "**❅ ʟɪғᴇ ɪs ᴍᴀᴅᴇ ᴜᴘ ᴏғ sᴏʙs, sɴɪғғʟᴇs, ᴀɴᴅ sᴍɪʟᴇs.**",
         "**❅ ɴᴏᴛ ʟɪғᴇ, ʙᴜᴛ ɢᴏᴏᴅ ʟɪғᴇ, ɪs ᴛᴏ ʙᴇ ᴄʜɪᴇғʟʏ ᴠᴀʟᴜᴇᴅ.**",
         "**❅ ʏᴏᴜ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ʟɪғᴇ ʙʏ ᴄʜᴀɴɢɪɴɢ ʏᴏᴜʀ ʜᴇᴀʀᴛ.",
         "**❅ ʟɪғᴇ ɪs ɴᴏᴛʜɪɴɢ ᴡɪᴛʜᴏᴜᴛ ᴛʀᴜᴇ ғʀɪᴇɴᴅsʜɪᴘ.**",
         "**❅ ɪғ ʏᴏᴜ ᴀʀᴇ ʙʀᴀᴠᴇ ᴛᴏ sᴀʏ ɢᴏᴏᴅ ʙʏᴇ, ʟɪғᴇ ᴡɪʟʟ ʀᴇᴡᴀʀᴅ ʏᴏᴜ ᴡɪᴛʜ ᴀ ɴᴇᴡ ʜᴇʟʟᴏ.**",
         "**❅ ᴛʜᴇʀᴇ ɪs ɴᴏᴛʜɪɴɢ ᴍᴏʀᴇ ᴇxᴄɪᴛɪɴɢ ɪɴ ᴛʜᴇ ᴡᴏʀʟᴅ, ʙᴜᴛ ᴘᴇᴏᴘʟᴇ.**",
         "**❅ ʏᴏᴜ ᴄᴀɴ ᴅᴏ ᴀɴʏᴛʜɪɴɢ, ʙᴜᴛ ɴᴏᴛ ᴇᴠᴇʀʏᴛʜɪɴɢ.**",
         "**❅ ʟɪғᴇ ʙᴇᴄᴏᴍᴇ ᴇᴀsʏ ᴡʜᴇɴ ʏᴏᴜ ʙᴇᴄᴏᴍᴇ sᴛʀᴏɴɢ.**",
         "**❅ ᴍʏ ʟɪғᴇ ɪsɴ’ᴛ ᴘᴇʀғᴇᴄᴛ ʙᴜᴛ ɪᴛ ᴅᴏᴇs ʜᴀᴠᴇ ᴘᴇʀғᴇᴄᴛ ᴍᴏᴍᴇɴᴛs.**",
         "**❅ ʟɪғᴇ ɪs ɢᴏᴅ’s ɴᴏᴠᴇʟ. ʟᴇᴛ ʜɪᴍ ᴡʀɪᴛᴇ ɪᴛ.**",
         "**❅ ᴏᴜʀ ʟɪғᴇ ɪs ᴀ ʀᴇsᴜʟᴛ ᴏғ ᴏᴜʀ ᴅᴏᴍɪɴᴀɴᴛ ᴛʜᴏᴜɢʜᴛs.**",
         "**❅ ʟɪғᴇ ɪs ᴀ ᴍᴏᴛɪᴏɴ ғʀᴏᴍ ᴀ ᴅᴇsɪʀᴇ ᴛᴏ ᴀɴᴏᴛʜᴇʀ ᴅᴇsɪʀᴇ.**",
         "**❅ ᴛᴏ ʟɪᴠᴇ ᴍᴇᴀɴs ᴛᴏ ғɪɢʜᴛ.**",
         "**❅ ʟɪғᴇ ɪs ʟɪᴋᴇ ᴀ ᴍᴏᴜɴᴛᴀɪɴ, ɴᴏᴛ ᴀ ʙᴇᴀᴄʜ.**",
         "**❅ ᴛʜᴇ ᴡᴏʀsᴛ ᴛʜɪɴɢ ɪɴ ʟɪғᴇ ɪs ᴛʜᴀᴛ ɪᴛ ᴘᴀssᴇs.**",
         "**❅ ʟɪғᴇ ɪs sɪᴍᴘʟᴇ ɪғ ᴡᴇ ᴀʀᴇ sɪᴍᴘʟᴇ.**",
         "**❅ ᴀʟᴡᴀʏs ᴛʜɪɴᴋ ᴛᴡɪᴄᴇ, sᴘᴇᴀᴋ ᴏɴᴄᴇ.**",
         "**❅ ʟɪғᴇ ɪs sɪᴍᴘʟᴇ, ᴡᴇ ᴍᴀᴋᴇ ɪᴛ ᴄᴏᴍᴘʟɪᴄᴀᴛᴇᴅ.**",
         "**❅ ʟɪғᴇ ɪs ɴᴏᴛ ᴍᴜᴄʜ ᴏʟᴅᴇʀ ᴛʜᴀɴ ᴛʜᴇ ᴅᴇᴀᴛʜ.**",
         "**❅ ᴛʜᴇ sᴇᴄʀᴇᴛ ᴏғ ʟɪғᴇ ɪs ʟᴏᴡ ᴇxᴘᴇᴄᴛᴀᴛɪᴏɴs!**",
         "**❅ ʟɪғᴇ ɪs ᴀ ᴛᴇᴀᴄʜᴇʀ..,ᴛʜᴇ ᴍᴏʀᴇ ᴡᴇ ʟɪᴠᴇ, ᴛʜᴇ ᴍᴏʀᴇ ᴡᴇ ʟᴇᴀʀɴ.**",
         "**❅ ʜᴜᴍᴀɴ ʟɪғᴇ ɪs ɴᴏᴛʜɪɴɢ ʙᴜᴛ ᴀɴ ᴇᴛᴇʀɴᴀʟ ɪʟʟᴜsɪᴏɴ.**",
         "**❅ ᴛʜᴇ ʜᴀᴘᴘɪᴇʀ ᴛʜᴇ ᴛɪᴍᴇ, ᴛʜᴇ sʜᴏʀᴛᴇʀ ɪᴛ ɪs.**",
         "**❅ ʟɪғᴇ ɪs ʙᴇᴀᴜᴛɪғᴜʟ ɪғ ʏᴏᴜ  ᴋɴᴏᴡ ᴡʜᴇʀᴇ ᴛᴏ ʟᴏᴏᴋ.**",
         "**❅ ʟɪғᴇ ɪs ᴀᴡᴇsᴏᴍᴇ ᴡɪᴛʜ ʏᴏᴜ ʙʏ ᴍʏ sɪᴅᴇ.**",
         "**❅ ʟɪғᴇ – ʟᴏᴠᴇ = ᴢᴇʀᴏ**",
         "**❅ ʟɪғᴇ ɪs ғᴜʟʟ ᴏғ sᴛʀᴜɢɢʟᴇs.**",
         "**❅ ɪ ɢᴏᴛ ʟᴇss ʙᴜᴛ ɪ ɢᴏᴛ ʙᴇsᴛ **",
         "**❅ ʟɪғᴇ ɪs 10% ᴡʜᴀᴛ ʏᴏᴜ ᴍᴀᴋᴇ ɪᴛ, ᴀɴᴅ 90% ʜᴏᴡ ʏᴏᴜ ᴛᴀᴋᴇ ɪᴛ.**",
         "**❅ ᴛʜᴇʀᴇ ɪs sᴛɪʟʟ sᴏ ᴍᴜᴄʜ ᴛᴏ sᴇᴇ**",
         "**❅ ʟɪғᴇ ᴅᴏᴇsɴ’ᴛ ɢᴇᴛ ᴇᴀsɪᴇʀ ʏᴏᴜ ɢᴇᴛ sᴛʀᴏɴɢᴇʀ.**",
         "**❅ ʟɪғᴇ ɪs ᴀʙᴏᴜᴛ ʟᴀᴜɢʜɪɴɢ & ʟɪᴠɪɴɢ.**",
         "**❅ ᴇᴀᴄʜ ᴘᴇʀsᴏɴ ᴅɪᴇs ᴡʜᴇɴ ʜɪs ᴛɪᴍᴇ ᴄᴏᴍᴇs.**",
        ]


@app.on_message(filters.command(["ajtag" ], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")

    if message.reply_to_message and message.text:
        return await message.reply("/ajtag ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/ajtag ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs...")
    else:
        return await message.reply("/ajtag ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs...")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"<blockquote>[{usr.user.first_name}](tg://user?id={usr.user.id}</blockquote>\n) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"<blockquote>{usrtxt} {random.choice(TAGMES)}</blockquote>"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(3)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["lifetag"], prefixes=["/", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["cancel", "stop", "stopall"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("๏ ᴄᴜʀʀᴇɴᴛʟʏ ɪ'ᴍ ɴᴏᴛ ᴛᴀɢɢɪɴɢ ʙᴀʙʏ.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("๏ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss sᴛᴏᴘᴘᴇᴅ ๏")
