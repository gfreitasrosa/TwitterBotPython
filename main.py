import tweepy
import time
import os


auth = tweepy.OAuthHandler(os.environ['API_KEY'], os.environ['API_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])

api = tweepy.API(auth)
mention_id = 1

user_bot = api.get_user(screen_name="Lz892445823")
bot_id = user_bot.id_str

words = ['@Lz892445823', 'como', 'quando', 'what', '?']
message = "Se voce tiver qualquer dúvida, sinta-se a vontade para nos mandar DM @{}"

while True:
    mentions = api.mentions_timeline(since_id=mention_id)
    for mention in mentions:
        print("Você foi mencionado em um tuite")
        print(f"{mention.author.screen_name} = {mention.text}")
        mention_id = mention_id
        if mention.in_reply_to_status_id is None and mention.author.id != bot_id:
            if True in [word in mention.text.lower() for word in words]:
                try:
                    print("Tentando responder...")
                    api.update_status(message.format(mention.author.screen_name), in_reply_to_status_id=mention.id_str)
                    print("Respondindo com sucesso")
                except Exception as exc:
                    print(exc)
    time.sleep(15)