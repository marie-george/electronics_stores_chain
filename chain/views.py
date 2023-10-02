from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from chain.models import ChainUnit
from chain.serializers import ChainUnitSerializer


class ChainUnitCreateAPIView(generics.CreateAPIView):
    serializer_class = ChainUnitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_module = serializer.save()
        new_module.owner = self.request.user
        new_module.save()


class ChainUnitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ChainUnitSerializer
    queryset = ChainUnit.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return ChainUnit.objects.none()
        else:
            user = self.request.user
            return ChainUnit.objects.filter(owner=user)


class ChainUnitDestroyAPIView(generics.DestroyAPIView):
    queryset = ChainUnit.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return ChainUnit.objects.none()
        else:
            user = self.request.user
            return ChainUnit.objects.filter(owner=user)


class ChainUnitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ChainUnitSerializer
    queryset = ChainUnit.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return ChainUnit.objects.none()
        else:
            user = self.request.user
            return ChainUnit.objects.filter(owner=user)


class ChainUnitListAPIView(generics.ListAPIView):
    serializer_class = ChainUnitSerializer
    queryset = ChainUnit.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return ChainUnit.objects.none()
        else:
            user = self.request.user
            return ChainUnit.objects.filter(owner=user)
