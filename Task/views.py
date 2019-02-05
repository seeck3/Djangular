from django.http import JsonResponse
from django.views import View
from .models import Task
import json
# Create your views here.

class Tasks(View):
    def get(self, request):
        tasks = list(Task.objects.values().all())
        return JsonResponse({"status": "ok", "tasks": tasks})

    def post(self, request):
        body = json.loads(request.body.decode())
        print(body)
        Task.objects.create(
            task = body['task'],
            isComplete = False
        )
        return JsonResponse({"status": "okay", "message": "task is updated"})

    def put(self, request, _id):
        tasks = Task.objects.get(id = _id)
        print(tasks.isComplete)
        if tasks.isComplete == "True":
            tasks.isComplete = "False"
            print('true', tasks.isComplete)
        else:
            tasks.isComplete = "True"
            print('false', tasks.isComplete)
        tasks.save()    
        t = list(Task.objects.values().all())
        print(t)
        result = t
        return JsonResponse({"status": "okay", "result": result})

    def delete(self, request, _id):
        print(_id)
        result = Task.objects.get(id = _id).delete()
        return JsonResponse({'status': "okay", "result": result})