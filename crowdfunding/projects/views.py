from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Faq, Milestone, Project, Pledge, Tag
from. serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer, TagSerializer, FaqSerializer, TagDetailSerializer, MilestoneSerializer
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
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

class PledgeDetail(APIView):
    #   permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerorReadOnly]

    def get_object(self, pk):
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request,pledge)
            return pledge

        except Pledge.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        pledge = self.get_object(pk)
        data = request.data
        serializer = PledgeDetailSerializer(
            instance = pledge,
            data = data,
            partial = True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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


class FaqList(APIView):

# Only project owner can answer questions
# Only users can ask questions
# Anyone can see questions and answers

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def get(self, request):
        faqs = Faq.objects.all()
        serializer = FaqSerializer(faqs, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = FaqSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

class FaqDetail(APIView):

    def get_object(self, request, pk):

        try:
            answers = Faq.objects.get(pk=pk)
            self.check_object_permissions(self.request,answers)
            return answers

        except Project.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        answers = self.get_object(pk)
        serializer = FaqSerializer(answers)
        return Response(serializer.data)

    def put(self, request, pk):
        answers = self.get_object(pk)
        data = request.data
        serializer = FaqSerializer(
            instance = answers,
            data = data,
            partial = True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MilestoneList(APIView):

# Only project owner can create and edit milestones

    def get(self, request):
        milestones = Milestone.objects.all()
        # answers = 
        serializer = MilestoneSerializer(milestones, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = MilestoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
