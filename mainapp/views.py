from django.shortcuts import render_to_response


def two_gis_view(request):
    return render_to_response("index.html")