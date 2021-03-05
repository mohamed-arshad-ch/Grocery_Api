from .models import *

class ModelController:
    
    def __init__(self, *args, **kwargs):
        self.table = kwargs['table']

    def get_all_content(self,count):
        
        if count:
            data = self.table.objects.all().count()
            return data
        else:
            data = self.table.objects.all()
            return data


    def get_one_content(self,*args, **kwargs):
        try:
            
            val = kwargs['val']
            data = self.table.objects.get(pk=val)
            return data,True
        except self.table.DoesNotExist:
            return "Not Data in {0} Table".format(self.table),False
    
    

    