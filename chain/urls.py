from chain.apps import ChainConfig
from django.urls import path

from chain.views import ChainUnitCreateAPIView, ChainUnitUpdateAPIView, ChainUnitDestroyAPIView, ChainUnitRetrieveAPIView, ChainUnitListAPIView

app_name = ChainConfig.name

urlpatterns = [
    path('create/', ChainUnitCreateAPIView.as_view(), name='unit_create'),
    path('update/<int:pk>/', ChainUnitUpdateAPIView.as_view(), name='unit_update'),
    path('delete/<int:pk>/', ChainUnitDestroyAPIView.as_view(), name='unit_delete'),
    path('<int:pk>/', ChainUnitRetrieveAPIView.as_view(), name='unit_detail'),
    path('', ChainUnitListAPIView.as_view(), name='units_list')
]
