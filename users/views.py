# from restless.auth import BasicHttpAuthMixin, login_required
from restless.modelviews import ListEndpoint, DetailEndpoint
# from restless.views import Endpoint
from models import User, SocialNetwork, Friend

# class SecretGreeting(Endpoint, BasicHttpAuthMixin):
#     @login_required
#     def get(self, request):
#         return {'message': 'Hello, %s!' % request.user}

class UserList(ListEndpoint):
    model = User

class UserDetail(DetailEndpoint):
    model = User

# class FriendList(Endpoint):
#     def get(self, request, id_user):
#         friend = Friend.objects.get(pk=id_user)
#         return serialize(user, exclude=['password'])

# class SocialNetworksList(Endpoint):
#     def get(self, request, id_user):
#         socialNetwork = SocialNetwork.objects.get(pk=id_user)
#         return serialize(socialNetwork, exclude=['password'])