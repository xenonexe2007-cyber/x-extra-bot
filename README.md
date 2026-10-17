# X-EXTRA Telegram Bot

## Files
- `bot.py`: Telegram bot source
- `requirements.txt`: Python dependency

## Deploy on Render
1. Upload these files to a GitHub repository.
2. In Render, create a **Background Worker** and connect the repository.
3. Build command: `pip install -r requirements.txt`
4. Start command: `python bot.py`
5. Add an environment variable:
   - Key: `BOT_TOKEN`
   - Value: your NEW Telegram BotFather token

Never commit your bot token to GitHub. If a token has been exposed, revoke it with BotFather and create a new one.

The Dino button is a random-score demo, not a full playable game.
