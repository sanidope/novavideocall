from rest_framework import status
from core.models import NadiaProfile
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view 


@api_view(['PUT'])
def update_installed_app(request, id_token):
    try:
        nadia_profile = NadiaProfile.objects.get(id_token=id_token)
    
    except NadiaProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'PUT':
        data = JSONParser().parse(request) 
        app_installed = data.get('app_installed')
        NadiaProfile.objects.select_for_update().filter(id_token=id_token).update(app_installed=app_installed)
        
            
    return Response(status=status.HTTP_400_BAD_REQUEST)


