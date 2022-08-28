from datetime import date
from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User

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


class TitleSerializer(serializers.ModelSerializer):
    """Сериализатор произведения для получения экземпляра или списка."""
    genre = serializers.SlugRelatedField(
        many=True, slug_field='slug',
        queryset=Genre.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all()
    )
    rating = serializers.SlugRelatedField(
        many=True, slug_field='score',
        queryset=Review.objects.all()
    )

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'rating', 'description', 'genre', 'category')


class TitleCreateSerializer(serializers.ModelSerializer):
    """Сериализатор создания экземпляра произведения."""
    genre = serializers.SlugRelatedField(many=True, write_only=True,
                                         slug_field='slug', required=False,
                                         queryset=Genre.objects.all())
    category = serializers.SlugRelatedField(many=False, write_only=True,
                                            slug_field='slug', required=False,
                                            queryset=Category.objects.all())

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'description', 'genre', 'category')

    def validate_year(self, value):
        if not 0 < value < date.today().year:
            raise serializers.ValidationError(
                'Нельзя добавлять произведения, которые еще не вышли!'
            )
        return value


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=False,
        slug_field='username',
        queryset=User.objects.all()
    )
    title_id = serializers.SlugRelatedField(
        many=False,
        slug_field='id',
        queryset=Title.objects.all()
    )
    class Meta:
        model = Review
        fields = ('id', 'text', 'score', 'author', 'title_id', 'pub_date')
        read_only_fields = ('id', 'author', 'title_id', )


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=False,
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
        read_only_fields = ('id', 'author', )