from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """ 
    Allows us to add and edit line items in the admin right from inside
    the order model.
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag', 'stripe_pid')

    fields = ('order_number', 'date', 'full_name', 'email', 'phone_number',
              'street_address1', 'street_address2', 'town_or_city',
              'postcode', 'county', 'delivery_cost', 'order_total',
              'grand_total', 'original_bag', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name', 'delivery_cost',
                    'order_total', 'grand_total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
