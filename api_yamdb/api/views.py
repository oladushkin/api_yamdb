

class CategoryViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet, ):
    """Класс представления категории."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [&&&]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet, ):
    """Класс представления жанра."""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [&&&]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=name',)
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    """Класс представления произведения."""
    queryset = Title.objects.annotate(rating=Avg('reviews__score'))
    permission_classes = (&&&)
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    ordering = ('name',)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleSerializer
        return TitleCreateSerializer