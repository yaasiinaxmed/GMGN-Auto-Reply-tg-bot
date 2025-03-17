# GMGN AutoReply Bot

The **GMGN AutoReply Bot** is designed to automatically reply to tweets containing certain keywords such as "gm", "gn", "Good Morning", and "Good Night". It helps users avoid repetitive interactions while engaging meaningfully on Twitter. 

This bot is for **personal use only** and **not a public bot**. To use it, you'll need to **set it up on your own computer or deploy it to a cloud service**.

## Setup Guide

Follow the steps below to **clone the repo**, **set up the Telegram bot**, and **run the bot** either locally or by deploying it on a cloud platform like **Heroku** or **Railway**.

### 1. **Clone the Repository**

Start by cloning the repository to your computer:

```bash
git clone https://github.com/yourusername/gmgn-auto-reply-bot.git
cd gmgn-auto-reply-bot
```

### 2. **Create a Telegram Bot Using BotFather**

You need to set up your own **Telegram Bot** using **BotFather**. Follow these steps:

1. Open Telegram and search for **BotFather** (official Telegram bot creation tool).
2. Start a chat with **BotFather** and type `/newbot` to create a new bot.
3. Follow the instructions to name your bot and choose a username (e.g., `gmgn_reply_bot`).
4. Once the bot is created, **BotFather** will give you a **Telegram bot token**. Copy the token.
5. Add this token to your `.env` file in the project directory as follows:
   ```
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   ```

### 3. **Set Up Twitter API**

Next, you’ll need to set up access to the **Twitter API**:

1. Create a **Twitter Developer** account and create an application at [Twitter Developer](https://developer.twitter.com/).
2. Generate your **API keys** and **Access tokens** and save them to a `.env` file:
   ```
   API_KEY=your_api_key
   API_SECRET=your_api_secret
   ACCESS_TOKEN=your_access_token
   ACCESS_TOKEN_SECRET=your_access_token_secret
   BEARER_TOKEN=your_bearer_token
   ```

### 4. **Install Dependencies**

Make sure you have **Python 3.x** installed on your machine. Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 5. **Run the Bot Locally**

Once you've set up the `.env` file with your credentials, run the bot locally on your computer:

```bash
python3 bot.py
```

The bot will start and will begin replying to tweets containing "gm", "gn", "Good Morning", and "Good Night".

## Benefits of Using This Bot

- **Avoid being a "Reply Guy"**: By automatically replying to specific tweets with engaging and friendly messages like "Good Morning" or "Good Night," this bot helps users avoid being labeled as a "Reply Guy" (someone who only replies with short, repetitive comments on social media). The bot provides genuine responses without flooding the platform with irrelevant replies.
  
- **Increase Engagement**: Users who engage with popular tweets or regular "gm" or "gn" messages will appear more active in the community. The bot will keep the interaction professional, friendly, and positive, boosting your online presence without coming off as intrusive.

- **Saves Time**: The bot automates the process of replying to tweets, saving users time while ensuring that their responses are consistent and timely.



### 6. **Deploy the Bot (Optional)**

If you prefer the bot to run continuously, you can deploy it to a cloud platform like **Heroku** or **Railway**. This ensures that the bot runs 24/7 without you having to keep it running on your own machine.

### 7. **Important Notes**

- **Personal Use Only**: This bot is designed for personal use, meaning **only you can use it**. It’s not a public bot that anyone can use. The setup must be done on your own machine or cloud instance.
- **Rate Limits**: The **Twitter API** has rate limits, which means there are restrictions on how frequently you can send requests. If you want to increase the speed, you may need to purchase a **Pro** plan from Twitter’s API service.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.