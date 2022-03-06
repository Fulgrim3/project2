from django.contrib.auth.models import AbstractUser
from django.db import models
#from matplotlib.pyplot import title

#create comment here
class User(AbstractUser):
    pass
    #watched_listing=models.M2M('Listing', related_name='watchers')


#bid keeps track of the user id, the amount of money bid on ther certain id, the item(listing) that was bid on, and the bidder's unique user information as a way to track   id 
 #   amount 
 #   listing 
 #   bidder 
class Bid(models.Model):
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pass

#it's a catoary that tracks the ID, and the name associated with the type of catagory 
class Category():
    pass
#listing is the main table that will branch from all other tables... id title
#    description 
#    seller 
#    image_url 
#    starting bid 
#    is_active 
#    category 
#    timestamp 
class Listing():
    pass

#id, watcher, and listing
class Watchlist(models.Model):
    #ManyToMany.UserListing
    pass


#comment will track author, text created, a timestamp of the comment, and which listing the comment is associated with
class Comment(models.Model):
    #id =
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    body = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    #this listing tab may need to be deleted...
    #TODO #1
    #listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="get_comments")

    class Meta: 
        ordering =['timestamp']
    
    def __str__(self):
        return 'Comment {} by {}' .format(self.body, self.name)