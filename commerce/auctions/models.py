from django.contrib.auth.models import AbstractUser
from django.db import models
from matplotlib.pyplot import title


class User(AbstractUser):
    watched_listing=models.M2M('Listing', related_name='watchers')

class Category(#todo):
    id 
    name 
    pass

class Bid(#todo):
    id 
    amount 
    listing 
    bidder 
    pass

class Listing(#todo):
    id 
    title
    description 
    seller 
    image_url 
    starting bid 
    is_active 
    category 
    timestamp 
    pass

class Watchlist(ManyToMany.UserListing):
    id
    watcher
    listing
    pass

class Comment(#todo):
    id
    author
    body
    timestamp
    listing
    pass