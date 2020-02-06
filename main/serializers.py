from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.contenttypes.models import ContentType


from rest_framework import serializers
from main.models import Article, News, Comment, Vote, POSIBLE_VOIT


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'text', 'creation_date', 'publication_date', 'author']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'text', 'creation_date', 'publication_date', 'author']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'comment', 'content_type', 'author']


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'author', 'vote', 'content_type', 'object_id', 'content_object']


class ArticleCommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    article = serializers.PrimaryKeyRelatedField(source='object_id',queryset=Article.objects.all())
    comment = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        comment = Comment(
            comment=validated_data['comment'],
            author = validated_data['author'],
            content_object=validated_data['object_id'],
        )
        comment.save()

        return comment

    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        return instance


class NewsCommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    news = serializers.PrimaryKeyRelatedField(source='object_id',queryset=News.objects.all())
    comment = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        comment = Comment(
            comment=validated_data['comment'],
            author = validated_data['author'],
            content_object=validated_data['object_id'],
        )
        comment.save()

        return comment

    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        return instance


class NewsVoteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    news = serializers.PrimaryKeyRelatedField(source='object_id',queryset=News.objects.all())
    vote = serializers.ChoiceField(choices=POSIBLE_VOIT)

    def create(self, validated_data):
        try:
            is_exist = Vote.objects.get(
                author=validated_data['author'],
                content_type=ContentType.objects.get(app_label='main', model='news'),
                object_id=validated_data['object_id'].id
            )
        except Vote.DoesNotExist:
                    is_exist = None
        if is_exist:
            is_exist.vote=validated_data['vote']
            is_exist.save()
            return is_exist
        comment = Vote(
            vote=validated_data['vote'],
            author = validated_data['author'],
            content_object=validated_data['object_id'],
        )
        comment.save()

        return comment

    def update(self, instance, validated_data):
        instance.vote = validated_data.get('vote', instance.vote)
        instance.save()
        return instance

    def validate(self, attrs):
        try:
            is_exist = Vote.objects.get(
                author=attrs.get('author'),
                content_type=ContentType.objects.get(app_label='main', model='news'),
                object_id=attrs.get('object_id').id
            )
        except Vote.DoesNotExist:
            is_exist = None

        if is_exist and is_exist.vote == attrs.get('vote'):
            raise serializers.ValidationError('This user already voted')
        return attrs


class ArticleVoteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    article = serializers.PrimaryKeyRelatedField(source='object_id',queryset=Article.objects.all())
    vote = serializers.ChoiceField(choices=POSIBLE_VOIT)

    def create(self, validated_data):
        try:
            is_exist = Vote.objects.get(
                author=validated_data['author'],
                content_type=ContentType.objects.get(app_label='main', model='article'),
                object_id=validated_data['object_id'].id
            )
        except Vote.DoesNotExist:
                    is_exist = None
        if is_exist:
            is_exist.vote=validated_data['vote']
            is_exist.save()
            return is_exist

        comment = Vote(
            vote=validated_data['vote'],
            author = validated_data['author'],
            content_object=validated_data['object_id'],
        )
        comment.save()

        return comment

    def update(self, instance, validated_data):
        instance.vote = validated_data.get('vote', instance.vote)
        instance.save()
        return instance

    def validate(self, attrs):
        try:
            is_exist = Vote.objects.get(
                author=attrs.get('author'),
                content_type=ContentType.objects.get(app_label='main', model='article'),
                object_id=attrs.get('object_id').id
            )
        except Vote.DoesNotExist:
            is_exist = None

        if is_exist and is_exist.vote == attrs.get('vote'):
            raise serializers.ValidationError('This user already voted')
        return attrs


class CommentVoteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    comment = serializers.PrimaryKeyRelatedField(source='object_id',queryset=Comment.objects.all())
    vote = serializers.ChoiceField(choices=POSIBLE_VOIT)

    def create(self, validated_data):
        try:
            is_exist = Vote.objects.get(
                author=validated_data['author'],
                content_type=ContentType.objects.get(app_label='main', model='comment'),
                object_id=validated_data['object_id'].id
            )
        except Vote.DoesNotExist:
                    is_exist = None
        if is_exist:
            is_exist.vote=validated_data['vote']
            is_exist.save()
            return is_exist
        comment = Vote(
            vote=validated_data['vote'],
            author = validated_data['author'],
            content_object=validated_data['object_id'],
        )
        comment.save()

        return comment

    def update(self, instance, validated_data):
        instance.vote = validated_data.get('vote', instance.vote)
        instance.save()
        return instance

    def validate(self, attrs):
        try:
            is_exist = Vote.objects.get(
                author=attrs.get('author'),
                content_type=ContentType.objects.get(app_label='main', model='comment'),
                object_id=attrs.get('object_id').id
            )
        except Vote.DoesNotExist:
            is_exist = None

        if is_exist and is_exist.vote == attrs.get('vote'):
            raise serializers.ValidationError('This user already voted')
        return attrs
