import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category, Ad


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesView(View):
    def get(self, request):
        categories = Category.objects.all()
        return JsonResponse([cat.serialize() for cat in categories], safe=False, status=200)

    def post(self, request):
        category_data = json.loads(request.body)
        new_category = Category.objects.create(**category_data)
        return JsonResponse(new_category.serialize(), safe=False, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):
    def get(self, request):
        ads = Ad.objects.all()
        return JsonResponse([ad.serialize() for ad in ads], safe=False, status=200)

    def post(self, request):
        ad_data = json.loads(request.body)
        new_ad = Ad.objects.create(**ad_data)
        return JsonResponse(new_ad.serialize(), safe=False, status=200)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        try:
            return JsonResponse(self.get_object().serialize(), status=200)
        except Category.DoesNotExist:
            return JsonResponse({"error": "Not found"}, safe=False, status=404)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        try:
            return JsonResponse(self.get_object().serialize(), safe=False, status=200)
        except Ad.DoesNotExist:
            return JsonResponse({"error": "Not found"}, safe=False, status=404)
