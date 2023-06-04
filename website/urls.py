from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .views import HomeView, ImpressumView
from .sitemaps import StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
}

app_name = "website"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("impressum.html", ImpressumView.as_view(), name="impressum"),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]
