from __future__ import unicode_literals

from django.db import models


class Product(models.Model):
    name = models.CharField(default="", max_length=32)
    intro = models.TextField(default="", max_length=256)
    img_index = models.CharField(default="", max_length=64)
    img_detail_index = models.TextField(default="", max_length=256)
    img_detail_arg = models.TextField(default="", max_length=256)
    img_detail_detail = models.TextField(default="", max_length=256)

    def __unicode__(self):
        return self.name

    @property
    def index_img(self):
        return "img/products/" + self.name + "/" + self.img_index

    @property
    def detail_index_imgs(self):
        img_paths = self.img_detail_index.split("\r\n")
        r = []
        for img in img_paths:
            r.append((img.split(".")[0], "img/products/" + self.name + "/" + img))
        return r

    @property
    def detail_arg_imgs(self):
        img_paths = self.img_detail_arg.split("\r\n")
        r = []
        for img in img_paths:
            r.append("img/products/" + self.name + "/" + img)
        return r

    @property
    def detail_detail_imgs(self):
        img_paths = self.img_detail_detail.split("\r\n")
        r = []
        for img in img_paths:
            r.append("img/products/" + self.name + "/" + img)
        return r


class Company(models.Model):
    name = models.CharField(default="", max_length=32)
    intro = models.TextField(default="", max_length=2048)
    img = models.TextField(default="", max_length=256)

    def __unicode__(self):
        return self.name

    @property
    def intro_list(self):
        intros = self.intro.split("\n")
        return intros

    @property
    def img_list(self):
        img_paths = self.img.split("\r\n")
        r = []
        for img in img_paths:
            r.append("img/about/" + img)
        return r
