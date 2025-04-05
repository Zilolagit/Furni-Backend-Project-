from django.contrib import admin
from django.utils import html

from core.models import *
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "short_description",
        "product_image",
    )
    list_filter = (
        "name",
        "price",
    )
    def product_image(self, obj):
        if obj.image:
            return html.format_html("<img width=40 height=40 src=" + obj.image.url +">")
        else:
            return ""


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "created_at",
        "product_image",
        )
    list_filter = (
        "title",
        "created_at",
    )
    def product_image(self, obj):
        if obj.image:
            return html.format_html("<img width=40 height=40 src=" + obj.image.url +">")
        else:
            return ""

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "job",
        "product_image",
    )
    list_filter = (
        "job",
    )
    def product_image(self, obj):
        if obj.image:
            return html.format_html("<img width=40 height=40 src=" + obj.image.url +">")
        else:
            return ""

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "job",
        "product_image",
    )
    list_filter = (
        "job",
    )
    def product_image(self, obj):
        if obj.image:
            return html.format_html("<img width=40 height=40 src=" + obj.image.url +">")
        else:
            return ""

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
    )
    list_filter = (
        "first_name",
        "last_name",
        "email",
    )

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email"
    )

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "percent_off"
    )
    list_filter = (
        "percent_off",
        "code"
    )

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "coupon",
        "user",
        "billing",
    )
    list_filter = (
        "coupon",
        "user__username",
        "billing",
    )

@admin.register(OrderBilling)
class OrderBillingAdmin(admin.ModelAdmin):
    list_display = (
        "country",
        "first_name",
        "company_name",
        "state",
        "email",
    )
    list_filter = (
        "country",
        "first_name",
        "last_name",
        "company_name",
        "street_address",
        "state",
        "zip",
        "email",
        "phone",
        "shipping_account",
    )

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "product",
        "quantity",
    )
    list_filter = (
        "order__user",
        "product",
        "quantity",
    )

@admin.register(OrderShipping)
class OrderShippingAdmin(admin.ModelAdmin):
    list_display = (
        "country",
        "first_name",
        "last_name",
        "company_name",
        "street_address",
        "state",
        "zip",
        "email",
        "phone",
    )
    list_filter = (
        "country",
        "first_name",
        "company_name",
        "state",
        "email",
    )