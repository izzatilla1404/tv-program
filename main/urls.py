from django.urls import path
from .views import MainIndex, ChannelView, CategoryView, ProgramView

app_name = 'main'
urlpatterns = [
    path('', MainIndex.as_view(), name="index"),
    path('g/<int:gid>/', CategoryView.as_view(), name="index"),
    # path('', ChannelView.as_view(), name="index"),
    # path('', ProgramView.as_view(), name="index"),
]