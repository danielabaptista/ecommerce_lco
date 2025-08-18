from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    readonly_fields = ('price',)  # price will be set automatically

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'status', 'created_at')
    inlines = [OrderItemInline]
    readonly_fields = ('total_price',)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in instances:
            if isinstance(obj, OrderItem) and not obj.price:
                obj.price = obj.product.price  # copy product price
            obj.save()
        formset.save_m2m()

admin.site.register(Order, OrderAdmin)
