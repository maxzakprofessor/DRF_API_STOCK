from rest_framework import serializers
from EmployeeApp.models import Goods,Goodincomes,Stocks,Goodmoves,Goodrests
    #    fields=('DepartmentId','DepartmentName')
     #    fields=('EmployeeId','EmployeeName','Department','DateOfJoining','PhotoFileName')   
class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Goods 
        fields=('id','nameGood')

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stocks 
        fields=('id','nameStock')

class GoodcomineSerializer(serializers.ModelSerializer):
    class Meta:
        model=Goodincomes 
        fields=('id','idStock','nameStock','idGood','nameGood','qty','datetime')

class GoodmoveSerializer(serializers.ModelSerializer):
    class Meta:
        model=Goodmoves
        fields=('id','nameStockFrom','nameStockTowhere','nameGood','qty','datetime')

class GoodrestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Goodrests
        fields=('id','nameStock','nameGood','qty')







