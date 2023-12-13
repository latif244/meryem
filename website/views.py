from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponse
from .models import PostForm
from django.conf import settings


class FormMixin:
    def save_form(self, form_class, request):
        """
        Saves the content of the form provided and returns the result
        """
        details = form_class(request.POST)
        if details.is_valid():
            post = details.save(commit=False)
            post.save()
            email = details.cleaned_data.get('email')
            subject = details.cleaned_data.get('subject')
            message = details.cleaned_data.get('message')
            # send_mail(
            #     [subject],
            #     [message],
            #     [email],
            #     ['info@skylinewebservice.de'], # Replace with your email address
            #     fail_silently=False,
            # )
            send_mail(
                subject=[subject],
                message=[message] + [email],
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.RECIPIENT_ADDRESS],
                fail_silently=False,
            )
            result = "Thank you"
            return HttpResponse(result, status=200)
        else:
            result = "Something went wrong. Please try again."
            return HttpResponse(result, status=400)


class HomeView(FormMixin, TemplateView):
    template_name = "index.html"

    def post(self, request, *args, **kwargs):
        return self.save_form(PostForm, request)

    def get(self, request, *args, **kwargs):
        form = PostForm(None)
        return render(request, "index.html", {"form": form})


class ImpressumView(TemplateView):
    template_name = "impressum.html"
