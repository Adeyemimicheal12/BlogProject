import requests
import random
import random
from blogservice.models import BlogPost,Category

r = requests.get('https://newsapi.org/v2/everything?q=tesla&from=2024-03-09&sortBy=publishedAt&apiKey=dd2b35d691f348bd83cb9551c7d39491')
post_data=r.json()
post_data=post_data['articles'][:100]

cat = [1,2,3,4,5,6]
user = [1,2,3,4,5,6]

for post in post_data:
    BlogPost.objects.create(
        title=post["title"],
        body=post['content'],
        caterory=random.choice(cat),
        author=random.choice(user)
    )
   