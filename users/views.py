# from restless.auth import BasicHttpAuthMixin, login_required
from restless.modelviews import ListEndpoint, DetailEndpoint
from restless.views import Endpoint
from models import User, SocialNetwork, Friend
from restless.models import serialize
from restless.http import Http201, HttpError
from django.db.models import Q
from restless.auth import BasicHttpAuthMixin, login_required

# class SecretGreeting(Endpoint, BasicHttpAuthMixin):
#     @login_required
#     def get(self, request):
#         return {'message': 'Hello, %s!' % request.user}

class UserList(ListEndpoint):
    model = User

class UserDetail(Endpoint):
    # @login_required
    def get(self, request, pk):
        user = User.objects.get(pk=pk)

        user = serialize(user, fields=[
            'id',
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
        friends = []
        for f in Friend.objects.filter(Q(id_user__id=pk) | Q(id_owner__id=pk)):
            if pk == f.id_user:
                friends.append({'id':f.id_owner.id, 'name':f.id_owner.name, 'surname':f.id_owner.surname, 'active': f.active})
            else:
                friends.append({'id':f.id_user.id, 'name':f.id_user.name, 'surname':f.id_user.surname, 'active': f.active})
        user['friends'] = friends
        user['socials'] = {s.name:s.link for s in SocialNetwork.objects.filter(user__id=pk)}
        return user


class SocialNetworkList(ListEndpoint):
    model = SocialNetwork            

class SocialNetworkDetail(DetailEndpoint):
    model = SocialNetwork

class FriendList(ListEndpoint):
    def post(self, request, *args, **kwargs):
        if 'POST' not in self.methods:
            raise HttpError(405, 'Method Not Allowed')
          
        id_owner = User.objects.get(id=request.data['id_owner'])
        id_user = User.objects.get(id=request.data['id_user'])
        friend = Friend.objects.create(id_owner=id_owner, id_user=id_user)
        return Http201(self.serialize(friend))

class FriendDetail(DetailEndpoint):
    model = Friend