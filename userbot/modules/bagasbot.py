from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.yatim(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`𝐂𝐢𝐡𝐡 𝐁𝐚𝐜𝐨𝐭 𝐋𝐮 𝐘𝐚𝐭𝐢𝐦 !`")
    sleep(2)
    await typew.edit("`𝐄𝐦𝐚𝐤 , 𝐁𝐚𝐩𝐚𝐤.. 𝐊𝐨𝐤 𝐝𝐢 𝐓𝐚𝐧𝐞𝐦 !`")
    sleep(1)
    await typew.edit("`𝐃𝐢 𝐓𝐚𝐧𝐞𝐦 𝐊𝐞𝐤 𝐒𝐢𝐧𝐠𝐤𝐨𝐧𝐠 , 𝐁𝐇𝐀𝐊𝐒𝐒𝐒𝐒𝐒𝐒`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Permisi Aku mau nimbrung Kk..**")


@register(outgoing=True, pattern='^.bagas(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**kyy Peler☑️**")
    await typew.edit("**kyy Peler✅**")
    sleep(2)
    await typew.edit("**Rendi Gilaa☑️**")
    await typew.edit("**Rendi Gilaa✅**")
    sleep(2)
    await typew.edit("**Skyzu Depresi☑️**")
    await typew.edit("**Skyzu Depresi✅**")
    sleep(2)
    await typew.edit("**Kitaro Gajelas☑️**")
    await typew.edit("**Kitaro Gajelas✅**")
    sleep(2)
    await typew.edit("**Sayo Ganteng!☑️**")
    await typew.edit("**Sayo Sunghu!✅**")
    sleep(2)
    await typew.edit("**Kyy² kang gabut!☑️**")
    await typew.edit("**Kyy² kang gabut!✅**")
    sleep(2)
    await typew.edit("**Tonic,MengRibet☑️**")
    await typew.edit("**Tonic,MengRibet✅**")
    sleep(2)
    await typew.edit("**Penggali,Mengintil☑️**")
    await typew.edit("**Penggali,Mengintil✅**")
    sleep(2)
    await typew.edit("**BAGAS YANG PALING GANTENG FIX !**")
    sleep(3)

@register(outgoing=True, pattern='^.lah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Lahk, Lo tolol?`")
    sleep(1)
    await typew.edit("`Apa dongok?`")
    sleep(1)
    await typew.edit("`Gausah sok keras`")
    sleep(1)
    await typew.edit("`Gua ga ketrigger sama bocah baru nyemplung!`")


@register(outgoing=True, pattern='^.wah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wahh, War nya keren bang`")
    sleep(2)
    await typew.edit("`Tapi, Yang gua liat, kok Kaya lawakan`")
    sleep(2)
    await typew.edit("`Oh iya, Kan lo badut 🤡`")
    sleep(2)
    await typew.edit("`Kosa kata pas ngelawak, Jangan di pake war bang`")
    sleep(2)
    await typew.edit("`Kesannya lo ngasih kita hiburan.`")
    sleep(2)
    await typew.edit("`Kasian badut🤡, Ga di hargain pengunjung, Eh lampiaskan nya ke Tele, Wkwkwk`")
    sleep(3)
    await typew.edit("`Dah sana cabut, Makasih hiburannya, Udah bikin Gua tawa ngakak`")
    
@register(outgoing=True, pattern='^.gc(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`SUPPORT.. `")
    sleep(1)
    await typew.edit("`CENGHA...`")
    sleep(1)
    await typew.edit("`SUCCESSFULLY COMPELED`")
    sleep(1)
    await typew.edit("`💀SUPPORT` @allfucek 💀 CENGHA` @loveisfuckedup")



CMD_HELP.update({
    "bagasbot":
    "`.bagas`\
    \nUsage: menampilkan alive bot.\
    \n\n`.yatim`\
    \n\n`.lah`\
    \nUsage: hiks\
    \n\n`.gc`\
    \nUsage: support\
    \n\n`.punten` ; `.sayonara`\
    \nUsage: misi."
    
})
