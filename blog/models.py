from django.db import models


# Create your models here.

class Author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


    def __str__(self):
        return self.get_full_name()
    
class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.caption}"

    

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
    excerpt = models.CharField(max_length=500)
    date = models.DateField(auto_now=True)
    content = models.TextField(max_length=10000)
    slug = models.SlugField()
    image = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.title} {self.author}"
    
    tag = models.ManyToManyField(Tag, default="")
    


    

  