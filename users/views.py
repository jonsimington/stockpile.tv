from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


class ProfileView(DetailView):
    """ A view that displays a user's profile.
    """
    template_name = "profiles/view_profile.html"
    context_object_name = "userprofile"
    model = UserProfile

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        """Ensures that only authenticated users can access the view."""
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        try:
            username = self.kwargs['username']
            return queryset.get(user__username=username)
        except UserProfile.DoesNotExist:
            raise Http404("User profile doesn't exist for user %s" % username)


class MyProfileView(ProfileView):
    """ A view that displays a user's own profile.
    """
    def get_object(self, queryset=None):
        try:
            return self.request.user.profile
        except UserProfile.DoesNotExist:
            user = self.request.user
            logger.info("Creating user profile for %s" % user.username)
            return UserProfile.objects.create(user=user)


class ProfileUpdateView(UpdateView):
    """ A view that displays a form for editing a user's profile.
    """
    template_name = "profiles/update_profile.html"
    form_class = UserProfileForm
    context_object_name = "userprofile"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        """Ensures that only authenticated users can access the view."""
        return super(ProfileUpdateView, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        return self.request.user.profile

    def get_initial(self):
        initial = super(ProfileUpdateView, self).get_initial()
        initial['first_name'] = self.request.user.first_name
        initial['last_name'] = self.request.user.last_name
        initial['email'] = self.request.user.email
        return initial

    def form_valid(self, form):
        messages.success(self.request, "Profile updated")
        return super(ProfileUpdateView, self).form_valid(form)
