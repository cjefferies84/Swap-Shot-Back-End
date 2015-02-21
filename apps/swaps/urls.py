from django.conf.urls import patterns, url
from django.conf import settings
from views import *
urlpatterns = patterns(
    '',

    url(r'^swaps/$', SwapList.as_view(), name='swaps'),
    url(r'^swaps-nested/$', SwapNestedList.as_view(), name='swaps'),
    url(r'^swaps/(?P<pk>[0-9]+)$', SwapDetail.as_view(), name='swap-detail'),
    url(r'^items/$', ItemList.as_view(), name='items'),
    url(r'^items/(?P<pk>[0-9]+)$', ItemDetail.as_view(), name='item-detail'),
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),

    # url(r'^recipes/(?P<pk>[0-9]+)$', RecipeDetail.as_view(), name='recipe-list'),
    # url(r'^add-item$', AddRecipe.as_view(), name='add-item'),
    # url(r'^ingredients$', IngredientList.as_view(), name='ingredient-list'),

    # Handling media files
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)