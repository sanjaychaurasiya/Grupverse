from rest_framework import generics
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from PIL import Image
from rest_framework.decorators import api_view
from django.template import Context

from django.template.loader import get_template
from .serializers import UserSerializer
from email_tracker.models import Users


class UserList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class SendTemplateMailView(APIView):
    """This class will send the mail with custom template to the target user's email."""

    def post(self, request, *args, **kwargs):
        target_user_email = request.data.get('email')
        mail_template = get_template("mail_template.html")
        context_data_is = dict()
        context_data_is["image_url"] = request.build_absolute_uri("render_image")
        url_is = context_data_is["image_url"]
        context_data_is['url_is'] = url_is
        html_detail = mail_template.render(context_data_is)
        subject, from_email, to = "Greetings !!", 'smtptesting404@gmail.com', [target_user_email]
        msg = EmailMultiAlternatives(subject, html_detail, from_email, to)
        msg.content_subtype = 'html'
        msg.send()
        return Response({"success": True})


@api_view((["PUT", "GET"]))
def render_image(request):
    """This method will increase the value count by 1 when the mail is opened by the receiver"""

    if request.method == 'GET':
        image = Image.new('RGB', (20, 20))
        response = HttpResponse(content_type="image/png", status=status.HTTP_200_OK)
        # If user auth is enabled then just replace the 6 by request.id to get the id of the user making the request.
        user = Users.objects.get(id=6)
        user.status = True
        user.count += 1
        user.save()
        image.save(response, "PNG")
        return response
