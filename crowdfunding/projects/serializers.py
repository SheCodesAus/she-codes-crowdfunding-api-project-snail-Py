from unicodedata import category
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Project, Pledge, Tag, Question, Answer

class TagSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    slug = serializers.SlugField()
    title = serializers.CharField(max_length=200, default=None)

    def create(self, validated_data):
        return Tag.objects.create(**validated_data)

class QuestionSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    project_id = serializers.IntegerField()
    anonymous = serializers.BooleanField()
    question_text = serializers.CharField()
    pub_date = serializers.DateTimeField()

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

class AnswerSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    project_id = serializers.IntegerField()
    question_id = serializers.IntegerField()
    owner =  serializers.ReadOnlyField(source = 'owner.id')
    answer_text = serializers.CharField()
    pub_date = serializers.DateTimeField()

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)

class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length = 200)
    anonymous = serializers.BooleanField()
    supporter = serializers.CharField(max_length = 200)
    project_id = serializers.IntegerField()

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)
        

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    date_closed = serializers.DateTimeField()
    category = TagSerializer(many=True, read_only = True)
    owner =  serializers.ReadOnlyField(source = 'owner.id')
    # owner = serializers.CharField(max_length=200)
    # pledges = PledgeSerializer(many=True, read_only=True)

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.category = validated_data.get('category', instance.category)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance


