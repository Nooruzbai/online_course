from decimal import Decimal
from django.conf import settings
from course.models import Course


class Cart(object):
    def __init__(self, request):
        # Initialisation of user's cart
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Saving user's cart in session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    # Adding product to user's cart
    # or updating the quantity of products
    def add(self, course, quantity=1, update_quantity=False):
        course_id = str(course.id)
        if course_id not in self.cart:
            self.cart[course_id] = {'quantity': 0,
                                     'price': str(course.price)}
        if update_quantity:
            self.cart[course_id]['quantity'] = quantity
        else:
            self.cart[course_id]['quantity'] += quantity
        self.save()

    # Saving data to session
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        # Telling that session is modified
        self.session.modified = True

    # Removing product from cart
    def remove(self, product):
        course_id = str(product.id)
        if course_id in self.cart:
            del self.cart[course_id]
            self.save()

    # Iteration through products
    def __iter__(self):
        course_ids = self.cart.keys()
        courses = Course.objects.filter(id__in=course_ids)
        for course in courses:
            self.cart[str(course.id)]['course'] = course

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    # Quantity of products
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price'])*item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
