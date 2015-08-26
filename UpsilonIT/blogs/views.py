from rest_framework import viewsets, filters
from blogs.serializers import BlogSerializer, PostSerializer
from blogs.models import Blog, Post
from django.db.models import Count, Max
import django_filters


class BlogFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.query_params.get('max', '') == 'True':
            test = Blog.objects.all().annotate(amount=Count('posts')).order_by('-amount')[0]
            return queryset.filter(id=test.id)
        else:
            return queryset


class BlogFilter(django_filters.FilterSet):
    start = django_filters.DateFilter(name='posts__created_at', lookup_type='gt')

    class Meta:
        model = Blog
        fields = ['start']


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    filter_backends = (
        filters.DjangoFilterBackend,
        BlogFilterBackend,
    )
    filter_class = BlogFilter


class PostFilter(django_filters.FilterSet):
    start = django_filters.DateRangeFilter(name='created_at', lookup_type='gte')
    end = django_filters.DateFilter(name='created_at', lookup_type='lte')
    name = django_filters.CharFilter(name='user__first_name')

    class Meta:
        model = Post
        fields = ['is_deleted', 'start', 'end', 'name']


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = (
        filters.DjangoFilterBackend,
    )
    filter_class = PostFilter