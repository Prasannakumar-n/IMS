from django.shortcuts import render
from django.views.generic import View, TemplateView
from inventory.models import Stock
from transactions.models import SaleBill, PurchaseBill

class HomeView(View):
    template_name = "home.html"

    def get(self, request):
        selected_product = request.GET.get('product', '')

        labels = []
        data = []

        stock_queryset = Stock.objects.filter(is_deleted=False).order_by('-quantity')

        if selected_product:
            stock_queryset = stock_queryset.filter(name=selected_product)

        for item in stock_queryset:
            labels.append(f"{item.name} ({item.sub_category})" if item.sub_category else item.name)
            data.append(item.quantity)

        sales = SaleBill.objects.order_by('-time')[:3]
        purchases = PurchaseBill.objects.order_by('-time')[:3]

        context = {
            'labels': labels,
            'data': data,
            'sales': sales,
            'purchases': purchases,
            'product_items': Stock.objects.filter(is_deleted=False).values('name').distinct(),
        }
        return render(request, self.template_name, context)




class AboutView(TemplateView):
    template_name = "about.html"
