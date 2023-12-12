from django.urls import path
from .views import CreateView, PartList

urlpatterns = [
    path('create/',  CreateView.as_view(), name='adding new elements'),
    path('show/', PartList.as_view(), name='displaying elements')
]
