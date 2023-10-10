from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from ..cart import Cart
from ..models import Course

class CartAddView(APIView):
    def post(self, request, pk,  *args, **kwargs):
        cart = Cart(request)
        course = get_object_or_404(Course, id=pk)
        cart.add(course)
        print(self.request.session['cart'])
        return Response({"message": f"{course.name} was added to cart!"})


class CartListView(APIView):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        data = cart.cart
        return Response(data)


class CartCourseRemoveView(APIView):

    def delete(self, request, pk, *args, **kwargs):
        cart = Cart(request)
        course = get_object_or_404(Course, pk=pk)
        cart.remove(course)
        message = {"message": f"{course.name} was removed"}
        return Response(message)


class CartClearView(APIView):
    def delete(self, request, *args, **kwargs):
        cart = Cart(request)
        cart.clear()
        message = {'message': "Cart was cleared!"}
        return Response(message)
