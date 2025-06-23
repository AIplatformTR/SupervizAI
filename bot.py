import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters



openai.api_key = os.getenv("sk-proj-I2hDtdOyN73Mryrfh065K86LZiVq1ePf8g15Z79Xi2FiUayo1-1ZcBRW_Zk6c0OjYERiFBb1T3BlbkFJAM_q2vw9mMC9t-awNRJcmgs3PYRBd6jojVapapoxtlThYXvhhuimFrFkvfYZVQxvuxPee2UFgA")
TELEGRAM_TOKEN = os.getenv("8103587222:ADybWP4EWJ1SxEx8RvKpxqFQXODZKCxy4")

print(f"TELEGRAM_TOKEN is: {TELEGRAM_TOKEN}")
if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_TOKEN is not set")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": (
                "Ты — SupervizAI, помощник психолога. Всегда соблюдай этические нормы психолога, принцип конфиденциальности и работай по 4 шагам: "
                "1. Уточни запрос специалиста по кейсу; "
                "2. Поддержи специалиста и выдели его ресурсы; "
                "3. Предложи гипотезу по случаю; "
                "4. Подскажи направления работы с клиентом. "
                "Отвечай на языке пользователя (русский или английский)."
            )},
            {"role": "user", "content": user_input}
        ]
    )

    await update.message.reply_text(response['choices'][0]['message']['content'])

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
