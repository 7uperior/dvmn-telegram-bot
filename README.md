# DVMN Lesson Status Telegram Bot

## Overview
This Telegram bot is designed to periodically check for updates on lesson statuses from the DVMN.org API and send notifications to a specified Telegram user. The bot uses long polling to retrieve updates and informs the user about the results of their lesson submissions.

## Features
- Retrieves updates from DVMN.org API using long polling.
- Sends notifications to the user about lesson check results.
- Handles errors and timeouts gracefully.

## Setup and Installation
### Prerequisites
- Python 3.10 or higher.
- A Telegram Bot Token. You can create a bot and obtain a token by talking to [BotFather](https://t.me/botfather) on Telegram.
- An API token from DVMN.org.

### Installation
1. Clone the repository: 
`git clone https://github.com/7uperior/dvmn-telegram-bot.git`
2. Navigate to the cloned directory:
   `cd dvmn-telegram-bot`
3. Install dependencies using Poetry:
   `poetry install`

### Configuration
1. Create a `.env` file in the root directory.
2. Add the following environment variables:
`TLGR_TOKEN=<your-telegram-bot-token>
DVMN_TOKEN=<your-dvmn-api-token>`
> Replace `<your-telegram-bot-token>` and `<your-dvmn-api-token>` with your actual tokens

## Usage
To run the bot:
`poetry run python src/dvmn_telegram_bot.py`
> Once the bot is running, send `/start` to your Telegram bot from your Telegram account (just a simple 'start a bot') to initiate the lesson status notifications.



## Troubleshooting

### Conflict Error: Multiple Bot Instances
If you encounter the following error:
`Conflict: terminated by other getUpdates request; make sure that only one bot instance is running`

This usually means that multiple instances of your bot are running at the same time, which can conflict with each other when trying to fetch updates.

#### How to Avoid
- Ensure that you only have one instance of your bot script running at any time.
- If running the bot on a server, check for any background processes that might be running the same script and terminate them if necessary.
- Restart your server or environment where the bot is hosted to clear any lingering processes.

#### How to Resolve
- Stop all instances of the bot.
- Run the script again to start only a single instance of the bot.
- If the issue persists, consider rebooting your server or development environment.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
