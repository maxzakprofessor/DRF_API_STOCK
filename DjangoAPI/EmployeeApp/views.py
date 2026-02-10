from django.db.models import Sum, Q
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Goods,Goodincomes,Stocks, Goodmoves, Goodrests
from EmployeeApp.serializers import GoodSerializer,GoodcomineSerializer, StockSerializer,GoodmoveSerializer,GoodrestSerializer

from django.core.files.storage import default_storage
from django.db.models import Sum, OuterRef, Subquery, FloatField
from django.db.models.functions import Coalesce

from rest_framework.decorators import api_view
from rest_framework.response import Response
import google.generativeai as genai
import os
import requests # Добавьте этот импорт в начало файла!
from .ai_engine import SkladAI  # Наш мозг для работы с ChromaDB







# Create your views here.

@csrf_exempt
def goodApi(request,id=0):
    if request.method=='GET':
        goods = Goods.objects.all()
        goods_serializer=GoodSerializer(goods,many=True)
        return JsonResponse(goods_serializer.data,safe=False)
    elif request.method=='POST':
        good_data=JSONParser().parse(request)
        goods_serializer=GoodSerializer(data=good_data)
        if goods_serializer.is_valid():
            goods_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        good_data=JSONParser().parse(request)
        good=Goods.objects.get(id=good_data['id'])
        goods_serializer=GoodSerializer(good,data=good_data)
        if goods_serializer.is_valid():
            goods_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        good=Goods.objects.get(id=id)
        good.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def stockApi(request,id=0):
    if request.method=='GET':
        stocks = Stocks.objects.all()
        stocks_serializer=StockSerializer(stocks,many=True)
        return JsonResponse(stocks_serializer.data,safe=False)
    elif request.method=='POST':
        stock_data=JSONParser().parse(request)
        stocks_serializer=StockSerializer(data=stock_data)
        if stocks_serializer.is_valid():
            stocks_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        stock_data=JSONParser().parse(request)
        stock=Stocks.objects.get(id=stock_data['id'])
        stocks_serializer=StockSerializer(stock,data=stock_data)
        if stocks_serializer.is_valid():
            stocks_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        stock=Stocks.objects.get(id=id)
        stock.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def goodincomeApi(request,id=0):
    if request.method=='GET':
        goodincomes = Goodincomes.objects.all()
        goodincomes_serializer=GoodcomineSerializer(goodincomes,many=True)
        return JsonResponse(goodincomes_serializer.data,safe=False)
    elif request.method=='POST':
        goodincome_data=JSONParser().parse(request)
        goodincomes_serializer=GoodcomineSerializer(data=goodincome_data)
        if goodincomes_serializer.is_valid():
            goodincomes_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        goodincome_data=JSONParser().parse(request)
        goodincome=Goodincomes.objects.get(id=goodincome_data['id'])
        goodincomes_serializer=GoodcomineSerializer(goodincome,data=goodincome_data)
        if goodincomes_serializer.is_valid():
            goodincomes_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        goodincome=Goodincomes.objects.get(id=id)
        goodincome.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    
@csrf_exempt
def goodmoveApi(request,id=0):
    if request.method=='GET':
        goodmoves = Goodmoves.objects.all()
        goodmoves_serializer=GoodmoveSerializer(goodmoves,many=True)
        return JsonResponse(goodmoves_serializer.data,safe=False)
    elif request.method=='POST':
        goodmove_data=JSONParser().parse(request)
        goodmoves_serializer=GoodmoveSerializer(data=goodmove_data)
        if goodmoves_serializer.is_valid():
            goodmoves_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        goodmove_data=JSONParser().parse(request)
        goodmove=Goodmoves.objects.get(id=goodmove_data['id'])
        goodmoves_serializer=GoodmoveSerializer(goodmove,data=goodmove_data)
        if goodmoves_serializer.is_valid():
            goodmoves_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        goodmove=Goodmoves.objects.get(id=id)
        goodmove.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    

@csrf_exempt
def goodrestApi(request, wnameStock="Все", wnameGood="Все"):
    if request.method == 'GET':
        # Базовые фильтры для всех таблиц
        income_qs = Goodincomes.objects.all()
        move_from_qs = Goodmoves.objects.all()
        move_to_qs = Goodmoves.objects.all()

        # 1. Фильтруем по ТОВАРУ (если выбрано не "Все")
        if wnameGood != "Все":
            income_qs = income_qs.filter(nameGood=wnameGood)
            move_from_qs = move_from_qs.filter(nameGood=wnameGood)
            move_to_qs = move_to_qs.filter(nameGood=wnameGood)

        # 2. Фильтруем по СКЛАДУ (если выбрано не "Все")
        if wnameStock != "Все":
            income_qs = income_qs.filter(nameStock=wnameStock)
            move_from_qs = move_from_qs.filter(nameStockFrom=wnameStock)
            move_to_qs = move_to_qs.filter(nameStockTowhere=wnameStock)

        # 3. Считаем итоговые суммы
        income_sum = income_qs.aggregate(s=Sum('qty'))['s'] or 0
        move_from_sum = move_from_qs.aggregate(s=Sum('qty'))['s'] or 0
        move_to_sum = move_to_qs.aggregate(s=Sum('qty'))['s'] or 0

        qty_rest = income_sum - move_from_sum + move_to_sum

        # Возвращаем результат
        return JsonResponse([{
            "nameGood": wnameGood,
            "nameStock": wnameStock,
            "qty": qty_rest
        }], safe=False)





@api_view(['GET'])
def ai_inventory_analysis(request):
    try:
        # 1. Берем ключ из .env (Безопасность)
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            return Response({"report": "### 🔴 Ошибка\nКлюч API не найден в системе (.env)"})

        # 2. Собираем URL из ваших частей (Гибкая архитектура)
        base_url = "https://generativelanguage.googleapis.com/v1beta2"
        model_path = "models/gemini-1.5-flash"
        action = ":generateContent"
        full_url = f"{base_url}{model_path}{action}"



        # 3. Сбор данных из PostgreSQL
        all_goods = Goods.objects.all()
        summary = []
        for g in all_goods:
            inc = Goodincomes.objects.filter(nameGood=g.nameGood).aggregate(s=Sum('qty'))['s'] or 0
            out = Goodmoves.objects.filter(nameGood=g.nameGood).aggregate(s=Sum('qty'))['s'] or 0
            summary.append(f"- {g.nameGood}: {inc - out} шт.")
        data_str = "\n".join(summary) if summary else "Склад пуст"

        # 4. RAG: Получаем контекст из ChromaDB
        context = "Инструкции не найдены."
        try:
            ai = SkladAI()
            relevant_docs = ai.collection.query(query_texts=[data_str], n_results=1)
            if relevant_docs['documents'] and len(relevant_docs['documents']) > 0:
                context = " ".join(relevant_docs['documents'][0])
        except Exception as e:
            print(f"ChromaDB Error: {e}")

        # 5. Формируем полезную нагрузку (Payload)
        payload = {
            "contents": [{
                "parts": [{
                    "text": f"Ты ИИ-аналитик склада. Инструкции: {context}. Данные склада:\n{data_str}\nДай краткий профессиональный совет на русском в формате Markdown."
                }]
            }]
        }

        # 6. Отправка запроса с использованием ваших частей URL
        response = requests.post(full_url, params={'key': api_key}, json=payload, timeout=15)
        
        if response.status_code == 200:
            res_data = response.json()
            # Безопасное извлечение текста от ИИ
            ai_text = res_data['candidates'][0]['content']['parts'][0]['text']
            return Response({"report": ai_text})
        else:
            # Обработка ошибок (например, если нужен VPN/WARP)
            return Response({
                "report": f"### 🔴 Ошибка API (Код {response.status_code})\n{response.text}"
            })

    except Exception as e:
        return Response({"report": f"### ⚠️ Системная ошибка\nДетали: {str(e)}"})
