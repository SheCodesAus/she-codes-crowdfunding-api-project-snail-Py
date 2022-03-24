from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge, Tag, Question, Answer
from. serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer, TagSerializer, QuestionSerializer, AnswerSerializer, TagDetailSerializer
from django.http import Http404
from rest_framework import status, permissions, generics
from .permissions import IsOwnerorReadOnly

class PledgeList(APIView):
    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

class ProjectList(APIView):
    
    # I can see the project list when loged off but I can't post/create a project unless logged in.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner = request.user)
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

class ProjectDetail(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerorReadOnly]

    def get_object(self, pk):
        # return Project.objects.get(pk=pk)
        try:
            # return Project.objects.get(pk=pk)
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request,project)
            return project

        except Project.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailSerializer(
            instance = project,
            data = data,
            partial = True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetail(APIView):

    # def get(self, request):
    #     model = Tag

    def get(self, request, slug):
        tag = Tag.objects.get(slug = slug)
        serializer = TagDetailSerializer(tag, many=False)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(APIView):

    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)


class AnswerDetail(APIView):
    def get(self, request):
        answers = Answer.objects.all()
        serializer = AnswerSerializer(questions, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
