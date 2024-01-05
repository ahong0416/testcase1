from django.shortcuts import render

# Create your views here.
################################################################################
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
################################################################################




# ################################################################################
# from catalog.models import RWB_Job, Job_Monitoring, Thread_Center
# ################################################################################


# import requests


# Create your views here.
class Case1ApiView(APIView):
   
    def get(self, request, input=None):


        # command = input
        # command = command.replace('$',' ')
        # command = command.replace('@','\\')


        # if input == None:
        #     print('nothing from user side')
        # elif 'activate' in input:
        #     Thread_Center.main(input)
        # elif input == 'monitor':
        #     print('monitoring job queue')
        #     return Response(Job_Monitoring.main(), status=status.HTTP_200_OK)
        # else:
        #     print('command = {}'.format(command))
        #     RWB_Job.add_to_job_queue(command)
        #     # RWB_Job.cmd_jsl(command)
        #     # RWB_Job.cmd_jsl_testing(command)
       
        return Response({'flag':'T'}, status=status.HTTP_200_OK)
