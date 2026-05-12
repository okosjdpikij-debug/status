from pypresence import Presence
import time

# الـ ID بتاعك من الصور اللي بعتها
client_id = '1503810878477176942' 

RPC = Presence(client_id)
RPC.connect()

print("✅ السكربت شغال دلوقتي يا عبدالرحمن، تقدر تروح تشوف بروفايلك!")

# تحديث الـ Rich Presence
RPC.update(
    state="ذَكِّرْ غَيْرَكَ", 
    details="ذكر الله حياة القلوب",
    large_image="logo",  # لازم يكون نفس الاسم اللي في صورة image_9c8182.png
    large_text="اللَّهُمَّ صَلِّ وَسَلِّمْ عَلَيْهِ",
    start=time.time(),   # عشان يظهر التايمر "Playing for..."
    buttons=[
        {"label": "Youtube", "url": "https://youtube.com"},
        {"label": "Discord", "url": "https://discord.gg/yourlink"}
    ]
)

# الحفاظ على تشغيل السكربت
try:
    while True:
        time.sleep(15)
except KeyboardInterrupt:
    print("إيقاف السكربت...")