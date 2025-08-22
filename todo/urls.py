from rest_framework.routers import DefaultRouter
from .views import AppUserViewSet, ToDoViewSet

router = DefaultRouter()
router.register(r"users", AppUserViewSet, basename="user")
router.register(r"todos", ToDoViewSet, basename="todo")

urlpatterns = router.urls
