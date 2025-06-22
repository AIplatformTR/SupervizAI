import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# Загружаем токены из переменных окружения
openai.api_key = os.getenv("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")
TELEGRAM_TOKEN = os.getenv("8103587222:AAFDybWP4EWJ1SxEx8RvKpxqFQXODZKCxy4")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": (
                "Ты — SupervizAI, помощник психолога, который помогает анализировать случаи из практики. "
                "Соблюдай этические нормы психолога и принцип конфиденциальности. Работай по следующей структуре: "
                "1) Уточни основной запрос; "
                "2) Поддержи специалиста, выдели его ресурсы; "
                "3) Сформулируй гипотезу; "
                "4) Предложи направления дальнейшей работы. "
                "Определи язык общения у пользователя и отвечай на нём."
            )},
            {"role": "user", "content": user_input}
        ]
    )

    await update.message.reply_text(response.choices[0].message["content"])

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
