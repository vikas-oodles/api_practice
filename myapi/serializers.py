from rest_framework import serializers
from django.contrib.auth.models import User
from myapi.models import Profile, Address

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # profile_url = serializers.HyperlinkedRelatedField(view_name='profile-detail')
    class Meta():
        model = User
        fields = ('username','email','password',)


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    # user_url = serializers.HyperlinkedIdentityField(view_name='user-detail')
    user = UserSerializer()
    # username = serializers.CharField(source='user.username', read_only=True)
    
    # email = serializers.CharField(source='user.email')
    
    class Meta():
        model = Profile
        fields = ('user','phone_number','gender','date_of_birth',)

    def get_full_name(self,obj):
        request = self.context['request']
        return request.user.get_full_name()

    def update(self,instance, validated_data):
        user_data = validated_data.pop('user',None)
        for attr, value in user_data.items():
            setattr(instance.user, attr, value)
        instance.user.save()
        instance.save()
        return instance

    