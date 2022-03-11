from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


urlpatterns = [
    path('snippets/', views.SnippetListGen.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetailGen.as_view()),
]

# We don't necessarily need to add these extra url patterns in, 
# but it gives us a simple, clean way of referring to a specific format.
urlpatterns = format_suffix_patterns(urlpatterns)