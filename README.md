# TweetCraft

TweetCraft is a Python script designed to automate the process of creating and posting enriched tweets. It leverages the OpenAI API to summarize web content and generate related images, then posts these summaries along with the images to Twitter, enhancing user engagement with visually appealing, informative tweets.

## Features

- **Content Summarization**: Utilizes OpenAI's GPT model to generate concise summaries of web content.
- **Image Generation**: Uses OpenAI's DALL-E to create images that complement the text summaries.
- **Tweet Automation**: Automatically posts tweets with text, images, and links to the original content.

## Prerequisites

Before you can run TweetCraft, you'll need:
- Python 3.x
- OpenAI API key
- Twitter Developer account and authentication credentials (API key, API secret key, Access token, Access token secret)
- Installation of the following Python packages: `openai`, `tweepy`, `python-dotenv`, `requests`.

## Installation

Clone the repository:
```bash
git clone https://github.com/yourusername/TweetCraft.git
```

Navigate to the script directory:
```bash
cd TweetCraft
```

Install required Python packages:
```bash
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the root directory of the project.
2. Add the following lines to the `.env` file, replacing placeholders with your actual keys:
   ```
   OPENAI_API_KEY='Your_OpenAI_API_Key'
   CONSUMER_KEY='Your_Twitter_Consumer_Key'
   CONSUMER_SECRET='Your_Twitter_Consumer_Secret'
   ACCESS_TOKEN='Your_Twitter_Access_Token'
   ACCESS_TOKEN_SECRET='Your_Twitter_Access_Token_Secret'
   ```

## Usage

To run TweetCraft:
```bash
python tweetcraft.py
```
Follow the prompts to input the URL you want to summarize and tweet.

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

Distributed under the MIT License. See `LICENSE` for more information.
