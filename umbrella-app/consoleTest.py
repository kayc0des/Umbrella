import models.basemodel
import inspect

print(type(models.basemodel))

for name, obj in inspect.getmembers(models.basemodel):
    if inspect.isclass(obj):
        print(obj) 