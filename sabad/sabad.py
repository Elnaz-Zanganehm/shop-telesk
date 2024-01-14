from decimal import Decimal
from django.conf import settings
from shophummin import models


class Sabad:
    def __init__(self, request):
        self.session = request.session
        sabad = self.session.get(settings.SABAD_SESSION_ID)
        if not sabad:
            sabad = self.session[settings.SABAD_SESSION_ID] = {}
        self.sabad = sabad

    def add(self, product, product_count=1, update_count=False):
        product_id = str(product.id)
        if product_id not in self.sabad:
            self.sabad[product_id] = {'product_count': 0,
                                      'price': str(product.price)}
        if update_count:
            self.sabad[product_id]['product_count'] = product_count
        else:
            self.sabad[product_id]['product_count'] += product_count
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.sabad:
            del self.sabad[product_id]
            self.save()

    def save(self):
        self.session[settings.SABAD_SESSION_ID] = self.sabad
        self.session.modified = True

    def __iter__(self):
        product_ids = self.sabad.keys()
        products = models.Product.objects.filter(id__in=product_ids)

        for product in products:
            self.sabad[str(product.id)]['product'] = product

        for item in self.sabad.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['product_count']
            yield item

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['product_count'] for item in self.sabad.values())
