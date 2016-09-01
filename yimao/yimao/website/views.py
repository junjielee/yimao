from django.shortcuts import render
from django.views.generic import View

from yimao.website.models import (
    Product,
    Company,
)


class IndexView(View):
    template_name = "website/index.html"

    def get(self, request):
        products = Product.objects.all()
        context = {"products": products}
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
