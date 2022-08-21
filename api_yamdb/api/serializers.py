from rest_framework import serializers

from reviews.models import Category, Genre, Title

class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор категории."""

    class Meta:
        model = Category
        fields = ('name', 'slug')

    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        return category


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор жанра."""

    class Meta:
        model = Genre
        fields = ('name', 'slug')

    def create(self, validated_data):
        genre = Genre.objects.create(**validated_data)
        return genre


class TitleSlugSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(many=True, slug_field='slug',
                                         queryset=Genre.objects.all())
    category = serializers.SlugRelatedField(slug_field='slug',
                                            queryset=Category.objects.all())

    class Meta:
        model = Title
        fields = '__all__'