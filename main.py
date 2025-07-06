import telegram
import datetime
import random
import time
import schedule

# 🔐 तेरा बॉट टोकन और ग्रुप ID
TOKEN = "8013164021:AAHMk4iH6Vh79DyNVkJuosxtRaDU9fQjx2Y"
CHAT_ID = -1002564868666  # @AstroTantraTalk group

bot = telegram.Bot(token=TOKEN)

# 🌞 सनातन धर्म के रोचक तथ्य
facts = [
    "🕉️ ॐ का उच्चारण मस्तिष्क को शांत करता है और ध्यान में सहायक होता है।",
    "🔥 हवन करने से वायुमंडल शुद्ध होता है — यह वैज्ञानिक रूप से सिद्ध है।",
    "🌿 तुलसी पौधे के पास बैठना तनाव कम करता है और ऊर्जा बढ़ाता है।",
    "📿 रुद्राक्ष धारण करने से हृदय और मन शांत रहता है।",
    "🪔 दीपक की लौ ब्रह्मांडीय चेतना का प्रतीक मानी गई है।",
    "📜 भगवद्गीता जीवन का व्यवहारिक दर्शन है — केवल युद्ध नहीं।",
    "🧘 ध्यान से चक्र जागृत होते हैं और आत्मिक उन्नति होती है।",
    "🛕 शंखनाद से वायुमंडल की नकारात्मकता दूर होती है।"
]

# 🎉 त्योहारों की लिस्ट (MM-DD format)
festivals_by_date = {
    "07-06": "🚩 *आज जगन्नाथ रथ यात्रा* है — भगवान को मन से खींचो, पुण्य अनंत होगा।",
    "08-19": "🌙 *आज श्रीकृष्ण जन्माष्टमी* है — रात्रि 12 बजे तक व्रत रखें और ध्यान करें।",
    "10-12": "🌺 *आज दुर्गा अष्टमी* है — कन्या पूजन करें, माँ की कृपा प्राप्त करें।",
    "10-23": "🔥 *आज दशहरा* है — रावण दहन से पहले अपने भीतर के रावण को जलाएं।"
    # ✨ और त्योहार जोड़ने हो तो इसी फ़ॉर्मेट में डाल सकते हो
}

# 🕯️ मैसेज भेजने का फंक्शन
def send_daily_fact():
    today = datetime.datetime.now().strftime("%m-%d")
    fact = random.choice(facts)
    text = f"📿 *आज का सनातन तथ्य:*\n\n{fact}"

    # अगर आज त्योहार है तो जोड़ो
    if today in festivals_by_date:
        text += f"\n\n🎉 *त्योहार विशेष:*\n{festivals_by_date[today]}"

    # भेजो!
    bot.send_message(chat_id=CHAT_ID, text=text, parse_mode=telegram.ParseMode.MARKDOWN)

# ⏱️ समय जांच: सिर्फ सुबह 6-8 और शाम 6-8 के बीच भेजें
def scheduler():
    now = datetime.datetime.now()
    hour = now.hour
    if (6 <= hour < 8) or (18 <= hour < 20):
        send_daily_fact()

# ⏳ हर 30 मिनट में चेक करो
schedule.every(30).minutes.do(scheduler)

# 🔁 बॉट चालू रखो
while True:
    schedule.run_pending()
    time.sleep(5)
