from django.urls import path
from .views import GptResponse


urlpatterns = [
    path("", GptResponse.as_view(), name="gpt_response"),
]
