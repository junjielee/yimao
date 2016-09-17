#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import View

from yimao.website.models import (
    Product,
    Company,
)


class IndexView(View):
    template_name = "website/index.html"

    def get(self, request):
        products = Product.objects.filter(is_main=True)
        context = {"products": products}
        return render(request, self.template_name, context)


class ProductsView(View):
    template_name = "website/products.html"

    def get(self, request):
        products = Product.objects.all()
        length = len(products)
        mod = length % 3
        len_new_list = length / 3
        if mod != 0:
            len_new_list += 1
        new_list = [[]] * len_new_list
        for i in range(len_new_list):
            new_list.append(products[i * 3: (i + 1) * 3])
        context = {"products": new_list}
        return render(request, self.template_name, context)


class ProductDetailView(View):
    template_name = "website/product_detail.html"

    def get(self, request, pid):
        product = Product.objects.get(id=int(pid))
        context = {"product": product}
        return render(request, self.template_name, context)


class AboutView(View):
    template_name = "website/about.html"

    def get(self, request):
        company = Company.objects.get(name="Yimao")
        context = {"company": company}
        return render(request, self.template_name, context)
