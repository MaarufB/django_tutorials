from rest_framework.serializers import ModelSerializer
from db_query_app.models import Author, Blog, Entry

class BlogSerializer(ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'

class AuthorSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'
        
class EntrySerializer(ModelSerializer):

    class Meta:
        model = Entry
        fields = '__all__'
