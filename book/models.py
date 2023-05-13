from django.db import models


class Book(models.Model):
    Book_Title = models.CharField(("Book-Title"), max_length=255)
    Book_Author = models.CharField(("Book-Author"), max_length=255)
    Year_Of_Publication = models.CharField(
        ("Year-Of-Publication"), max_length=255)
    Publisher = models.CharField(("Publisher"), max_length=255)
    Image_URL_S = models.CharField(("Image-URL-S"), max_length=255)
    Image_URL_M = models.CharField(("Image-URL-M"), max_length=255)
    Image_URL_L = models.CharField(("Image-URL-L"), max_length=255)
