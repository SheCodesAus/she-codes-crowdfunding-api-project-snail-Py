from unicodedata import category
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Project, Pledge, Tag, Faq, Milestone
from users.models import CustomUser

class TagSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    slug = serializers.SlugField()
    name = serializers.CharField(max_length=200, default=None)

    def create(self, validated_data):
        return Tag.objects.create(**validated_data)

class FaqSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    question_text = serializers.CharField()
    answer_text = serializers.CharField()        
    pub_date = serializers.DateTimeField()
    supporter = serializers.ReadOnlyField(source='supporter.id')
    # supporter =  serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())
    # def create(self, validated_data):
    #     return Faq.objects.create(**validated_data)
    
    project_id = serializers.IntegerField()

    def create(self, validated_data):
        return Faq.objects.create(**validated_data)

class FaqDetailSerializer(serializers.Serializer):

    def update(self, instance, validated_data):
        instance.question_text = validated_data.get('question_text', instance.question_text)
        instance.answer_text = validated_data.get('answer_text', instance.answer_text)
        instance.pub_data = validated_data.get('pub_date', instance.pub_date)
        instance.supporter = validated_data.get('owner', instance.supporter)
        instance.save()
        return instance


class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length = 200)
    anonymous = serializers.BooleanField()
    supporter = serializers.ReadOnlyField(source='supporter.id')
    # supporter = serializers.CharField(max_length = 200)
    project_id = serializers.IntegerField()

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

class PledgeDetailSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.anonymous = validated_data.get('anomymous', instance.anonymous)
        instance.supporter = validated_data.get('owner', instance.supporter)
        instance.save()
        return instance
        

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    tagline = serializers.CharField(max_length=None)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    date_closed = serializers.DateTimeField()
    owner =  serializers.ReadOnlyField(source = 'owner.id')
    category = serializers.SlugRelatedField(slug_field = "slug",queryset = Tag.objects.all())
    # faq = serializers.CharField()
    # category = TagSerializer(many=True, read_only = True)
    # owner = serializers.CharField(max_length=200)
    # pledges = PledgeSerializer(many=True, read_only=True)

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    project_faq = FaqSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.tagline = validated_data.get('tagline', instance.tagline)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.category = validated_data.get('category', instance.category)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

class TagDetailSerializer(TagSerializer):
    projects = ProjectSerializer (many = True)


class MilestoneSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField()
    description = serializers.CharField()
    project = serializers.IntegerField()

    def create(self, validated_data):
        return Milestone.objects.create(**validated_data)
