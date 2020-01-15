from django.urls import path
from .views import HomePageView, WineDetailView
# from .views import 

urlpatterns = [
    path('', HomePageView.as_view(), name='home'), # homepage
    path('cellar/<int:pk>', WineDetailView.as_view(), name='wine_detail') #detail-view
    # path('post/new/', CellarAddView.as_view(), name='add_new') #user indicates they want to add something new
]