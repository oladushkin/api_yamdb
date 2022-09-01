from rest_framework import filters, mixins, viewsets
from django.shortcuts import get_object_or_404
from django.db.models import Avg
from reviews.models import Category, Comment, Genre, Review, Title
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from .permissions import IsAdminUser, IsAuthenticated
from .serializers import (CategorySerializer, CommentSerializer,
                          GenreSerializer, ReviewSerializer, TitleSerializer, TitleCreateSerializer)
from.pagination import ReviewPagination
from .filters import TitleFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class ListCreateDestroyViewSet(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               mixins.DestroyModelMixin,
                               viewsets.GenericViewSet):
    pass


class CategoryViewSet(ListCreateDestroyViewSet, viewsets.GenericViewSet):
    """Класс представления категории."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser, ]
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(ListCreateDestroyViewSet, viewsets.GenericViewSet):
    """Класс представления жанра."""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminUser, ]
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=name',)
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    """Класс представления произведения."""
    queryset = Title.objects.all().annotate( 
        Avg('review__score') 
    ) 
    permission_classes = [IsAdminUser, ]
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    ordering = ('year',)
    filterset_class = TitleFilter
    pagination_class = LimitOffsetPagination

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleSerializer
        return TitleCreateSerializer
       

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, ]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        title_id = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title_id)

    def get_queryset(self):
        titles = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        return titles.review.all()

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, ]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review_id=review)

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return review.comments.all()