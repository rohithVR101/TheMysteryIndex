from django.urls import path
from . import views


urlpatterns = [
    path('',views.IndexView,name='index'),
    path('blog/',views.PostListView.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('mysterious-places/', views.MysteriousListView.as_view(), name='mysterious-places'),
    path('ancient-cities/', views.AncientListView.as_view(), name='ancient-cities'),
    path('legendary-places/', views.LegendaryListView.as_view(), name='legendary-places'),
    path('uninhabited-islands/', views.UninhabitedListView.as_view(), name='uninhabited-islands'),
    path('unexplained-disappearances/', views.UnexplainedListView.as_view(), name='unexplained-disappearances'),
    path('stones-and-statues/', views.StatuesListView.as_view(), name='stones-and-statues'),
    path('treasures/', views.TreasuresListView.as_view(), name='treasures'),
    path('shipwrecks/', views.ShipwrecksListView.as_view(), name='shipwrecks'),
    path('monsters/', views.MonstersListView.as_view(), name='monsters'),
    path('bizarre-people/', views.BizzareListView.as_view(), name='bizarre-people'),
    path('murders/', views.MurdersListView.as_view(), name='murders'),
    path('serial-killers/', views.SerialListView.as_view(), name='serial-killers'),
    path('ghosts/', views.GhostsListView.as_view(), name='ghosts'),
    path('extra-terrestrial/', views.ETListView.as_view(), name='extra-terrestrial'),
    path('incidents/', views.IncidentsListView.as_view(), name='incidents'),
    path('egyptian-mysteries/', views.EgyptianListView.as_view(), name='egyptian-mysteries'),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]
