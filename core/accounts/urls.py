from django.urls import path,include

app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path('api/v1/', include('accounts.api.v1.urls')), # api address accounts/api/v1
    #path('api/v2/', include('djoser.urls')),
    #path('api/v2/', include('djoser.urls.jwt')),
]