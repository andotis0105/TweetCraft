
# Install dependencies: openai, python-dotenv, tweepy, urllib3==1.26.6


# Import the required stuff
import openai
import os
import requests 
import tweepy

from openai import OpenAI

# Read .env file
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) 

# Set up OpenAI Authentication - from .env 
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY']  
)

# Input for the URL
print()
print("Paste in a URL and the Tweet-Bot will do its thing!")
user_input = input('User: ')
print()

# VARIABLES FOR INSTRUCTIONS
TEXT_MODEL="gpt-3.5-turbo"
instructions = "I will provide you with a URL, and in return, you will summarize that webpage in 50 words or less in the form of an attention-grabbing tweet for twitter, including appropriate hashtags"
context = [{'role': 'user', 'content': f"{user_input} {instructions}"}]

# Completeion function:
def get_completion(user_input, instructions="", temperature=0):
    try:
        response = client.chat.completions.create(
            model=TEXT_MODEL,
            messages=context,
            temperature=temperature,
        )

        return response.choices[0].message.content
    except openai.APIError as e:
        print(e.http_status)
        print(e.error)
        return e.error




# Save the URL for later
initial_url = f"{user_input}"

# Get the Response
summary = get_completion(user_input, instructions)
print("Tweet-Bot:", summary)


# Create the image prompt (image_summary)
def get_image_summary(temperature=0.7): 
    try:
        response = client.chat.completions.create(
        model=TEXT_MODEL,
        messages=[
            {'role': 'system', 'content': 'You are a skilled writer that is particularly proficient at writing visual discriptions of art - please write an image prompt based on the content of this tweet:'},
            {'role': 'user', 'content': summary},
         ],
    )

        return response.choices[0].message.content
    except openai.APIError as e:
        print(e.http_status)
        print(e.error)
        return e.error


# Create image from Image Summary - get_image_summary()
def generate_image(image_summary):
    print(image_summary)
    
    try:
        response = client.images.generate(
          model="dall-e-3",
          prompt=summary,
          size="1024x1024",
          quality="standard",
          n=1, 
        )
        
        image_url = response.data[0].url #URLs will expire after an hour

        return image_url
    except openai.APIError as e:
        print(e.http_status)
        print(e.error)
        return e.error


print()
image_summary = get_image_summary()
url = generate_image(image_summary)
print()
print()


def download_image(imageURL):
    print("downloading - ", imageURL)
    
    img_data = requests.get(imageURL).content
    with open('dalle_image.jpg', 'wb') as handler:
        handler.write(img_data)
    
    return "dalle_image.jpg"

image_name = download_image(url)


# Authenticate to Twitter API **NOT SECURE!** 
consumer_key = "your-twitter-consumer-key"
consumer_secret = "your-twitter-consumer-secret"
access_token = "your-twitter-access-token"
access_token_secret = "your-twitter-access-token-secret"


combined = f"{summary} {initial_url}"


#upload image media using V1 of Twitter API
def upload_image(image):
    auth = tweepy.OAuth1UserHandler(
       consumer_key,
       consumer_secret,
       access_token,
       access_token_secret
    )

    api = tweepy.API(auth)
    media = api.media_upload(filename=image) 
    
    return media

# Send the tweet using V2 of the Twitter API
def send_tweet(combined, image):
    client = tweepy.Client(
        consumer_key=consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_token_secret
    )

    # Upload image to Twitter servers and get media metadata (media_id)
    media = upload_image(image)
    media_ids = [media.media_id]
    
    #send the tweet
    response = client.create_tweet(text=combined, media_ids=media_ids)
    
    print(f"https://twitter.com/user/status/{response.data['id']}")
    
    
    print(combined)
    
    #send tweet
send_tweet(combined, image_name)