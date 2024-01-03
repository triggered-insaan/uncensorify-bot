# Uncensorify Bot

🚀 **Hey there! Welcome to Uncensorify Bot** 🌈✨

I'm your automated guardian on a mission to keep our Telegram experience respectful and clean 🌐.

## Getting Started
### For deploying locally

1. **Installation**
   - Clone the repository: `git clone https://github.com/triggered-insaan/uncensorify-bot.git`
   - Navigate to the project directory: `cd uncensorify-bot`
   - Install dependencies: `pip install -r requirements.txt`

2. **Environment Variables**

   - For deploying the bot, there are some required environment variables
      - `api_id`
      - `api_hash`
      - `bot_token`
      - `bot_username`
   
   - How to get these variables
     - Sign in with your Telegram account on https://my.telegram.org and get these variables
        - `api_id` : Telegram API ID 
        - `api_hash` : Telegram API Hash
     - Go to [@Botfather](https://t.me/botfather) on telegram
        - Start the bot
        - Make a new bot using /newbot
        - Give suitable name and username to your bot.
           - `bot_token` : Bot token provided when you successfully create your bot
           - `bot_username` : Username of your Telegram Bot 

2. **Usage**
   - Run the bot using this command: `python -m worker`

3. **Bot Commands**
   - `/start`: Start the bot and receive a welcome message.

### For deploying on cloud

- #### Render Deployment
  Click on the button to deploy on Render cloud Application
  
  [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/triggered-insaan/uncensorify-bot.git)