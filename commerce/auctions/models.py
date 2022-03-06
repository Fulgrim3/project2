from logging.handlers import WatchedFileHandler
from pyexpat import model
from this import d
from django.contrib.auth.models import AbstractUser
from django.db import models
#from matplotlib.pyplot import title

#create comment here
class User(AbstractUser):
    pass

#bid keeps track of the user id, the amount of money bid on ther certain id, the item(listing) that was bid on, and the bidder's unique user information as a way to track   id 
 #   amount 
 #   listing 
 #   bidder 
class Bid(models.Model):
    #id = 
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bidder =models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids") 
    time = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return f"{self.bidder} put a bid in for {self.amount}"

#it's a catoary that tracks the ID, and the name associated with the type of catagory. Categories are freeform from a dropdown menu. 

CATEGORIES = (
    ('a', 'Clothing, Shoes & Accessories'),
    ('b', 'Baby'),
    ('c', 'Food'),
    ('d', 'Miscellaneous'),
    ('e', 'Electronics'),
    ('f', 'None'),
)

#listing is the main table that will branch from all other tables... id title
#    description 
#    seller 
#    image_url 
#    starting bid 
#    is_active 
#    category 
#    timestamp 
#TODO fix the id 
class Listing(models.Model): 
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seller")
    image_url = models.ImageField(null=True, blank=True)
    starting_bid =  models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    category = models.CharField(max_length=3, choices=CATEGORIES, default=d)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.title}: is {self.startin_bid} and is being sold by {self.seller}"

#id, watcher, and listing
class Watchlist(models.Model):
    #id
    watcher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listings")
    
    def __str__(self):
        return f"{self.user.username} listed {self.listing.id}"


#comment will track author, text created, a timestamp of the comment, and which listing the comment is associated with
class Comment(models.Model):
    #id =
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    body = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="get_comments")

    class Meta: 
        ordering =['timestamp']
    
    def __str__(self):
        return 'Comment {} by {}' .format(self.author, self.body)