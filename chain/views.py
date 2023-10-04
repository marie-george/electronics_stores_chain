from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from chain.models import ChainUnit
from chain.permissions import IsActive
from chain.serializers import ChainUnitSerializer, ChainUnitUpdateSerializer


class ChainUnitCreateAPIView(generics.CreateAPIView):
    """Создание объекта сети"""
    serializer_class = ChainUnitSerializer
    permission_classes = [IsAuthenticated, IsActive]

    def perform_create(self, serializer):
        new_module = serializer.save()
        new_module.owner = self.request.user
        new_module.save()


class ChainUnitUpdateAPIView(generics.UpdateAPIView):
    """Редактирование объекта сети"""
    serializer_class = ChainUnitUpdateSerializer
    queryset = ChainUnit.objects.all()
    permission_classes = [IsAuthenticated, IsActive]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return ChainUnit.objects.none()
        else:
            user = self.request.user
            return ChainUnit.objects.filter(owner=user)


class ChainUnitDestroyAPIView(generics.DestroyAPIView):
    """Удаление объекта сети"""
    queryset = ChainUnit.objects.all()
    permission_classes = [IsAuthenticated, IsActive]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return ChainUnit.objects.none()
        else:
            user = self.request.user
            return ChainUnit.objects.filter(owner=user)


class ChainUnitRetrieveAPIView(generics.RetrieveAPIView):
    """Вывод подробной информации об объекте сети"""
    serializer_class = ChainUnitSerializer
    queryset = ChainUnit.objects.all()
    permission_classes = [IsAuthenticated, IsActive]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return ChainUnit.objects.none()
        else:
            user = self.request.user
            return ChainUnit.objects.filter(owner=user)


class ChainUnitListAPIView(generics.ListAPIView):
    """Вывод списка объектов сети"""
    serializer_class = ChainUnitSerializer
    queryset = ChainUnit.objects.all()
    permission_classes = [IsAuthenticated, IsActive]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return ChainUnit.objects.none()
        else:
            user = self.request.user
            return ChainUnit.objects.filter(owner=user)
