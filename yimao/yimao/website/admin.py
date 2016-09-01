from django.contrib import admin


from yimao.website.models import (
    Product,
    Company,
)


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "intro", "img_index"]


class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "intro", "img"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Company, CompanyAdmin)
