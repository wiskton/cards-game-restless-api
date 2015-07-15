# from restless.auth import BasicHttpAuthMixin, login_required
from restless.modelviews import ListEndpoint, DetailEndpoint
from restless.views import Endpoint
from models import User, SocialNetwork, Friend
from restless.models import serialize
from django.db.models import Q
from restless.auth import BasicHttpAuthMixin, login_required

# class SecretGreeting(Endpoint, BasicHttpAuthMixin):
#     @login_required
#     def get(self, request):
#         return {'message': 'Hello, %s!' % request.user}

__all__ = ['UsernamePasswordAuthMixin', 'BasicHttpAuthMixin',
    'AuthenticateEndpoint', 'login_required']
    
class UserList(ListEndpoint):
    model = User

class UserDetail(Endpoint):
    @login_required
    def get(self, request, pk):
        user = User.objects.get(pk=pk)

        user = serialize(user, fields=[
            'email',
            'name',
            'surname',
            'profession',
            'company',
            'avatar',
            'cover',
            'phone_number_1',
            'phone_number_1_carrier',
            'phone_number_2',
            'phone_number_2_carrier',
            'website',
            'street',
            'neightborhood',
            'city_state',
            'creation',
            'modification',
        ])

        # for f in Friend.objects.filter(Q(id_user__id=pk) | Q(id_owner__id=pk)):
        #     pass
        user['socials'] = {s.name:s.link for s in SocialNetwork.objects.filter(user__id=pk)}
        return user

class SocialNetworkList(ListEndpoint):
    model = SocialNetwork

class SocialNetworkDetail(DetailEndpoint):
    model = SocialNetwork

class FriendList(ListEndpoint):
    model = Friend

class FriendDetail(DetailEndpoint):
    model = Friend