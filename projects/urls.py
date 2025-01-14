from django.urls import path

from . import views


urlpatterns = [
	path("", views.home, name="home"),
	path("map", views.map, name="map"),
    path("resource", views.project_index, name="project_index"),
    path("setting/", views.setting, name="setting"),
    path("setting/my_post", views.my_post, name="my_post"),
    path("setting/my_video", views.my_video, name="my_video"),
    path("setting/my_column", views.my_column, name="my_column"),
    path("resource/background", views.background, name="background"),
    path("resource/setting", views.game_setting, name="game_setting"),
    path("resource/download", views.download, name="download"),
    path("resource/mod", views.mod, name="mod"),
    path("resource/history", views.history, name="history"),
    path("resource/allied_mission", views.mission, name="mission"),
    path("resource/soviet_mission", views.mission2, name="mission2"),
    path("resource/unit_data", views.unit_data, name="unit_data"),
    path("resource/story", views.story, name="story"),
    path("resource/super_weapon", views.super_weapon, name="super_weapon"),
    path("resource/tech_building", views.tech_building, name="tech_building"),
    path("resource/timeline", views.timeline, name="timeline"),
    path("resource/quotes", views.quotes, name="quotes"),
    path("resource/manual1", views.manual1, name="manual1"),
    path("resource/manual2", views.manual2, name="manual2"),
    path("resource/stat", views.stat, name="stat"),
    path("resource/time", views.time, name="time"),
    path("resource/special", views.special, name="special"),
    path("resource/yuri", views.yuri, name="yuri")
]
