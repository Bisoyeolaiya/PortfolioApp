from rest_framework import routers
from .api import CategoryViewSet, PostViewSet, CommentViewSet, ContactViewSet, ProjectViewSet

app_name = 'projectapi'

router = routers.DefaultRouter()
router.register('category', CategoryViewSet, 'category')
router.register('blogpost', PostViewSet, 'blogpost')
router.register('comment', CommentViewSet, 'comment')
router.register('contact', ContactViewSet, 'contact')
router.register('projects', ProjectViewSet, 'projects')

urlpatterns = router.urls
