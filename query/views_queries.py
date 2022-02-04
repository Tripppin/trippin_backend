from rest_framework.decorators import api_view
from django.shortcuts import HttpResponse
from rest_framework import status
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
from .models import Query
import json
import datetime


def serialize_query(order):
    serialized = model_to_dict(query)
    serialized["date"] = str(query.date)
    serialized["title"] = float(query.title)
    serialized["query"] = float(query.query)
    serialized["email"] = float(query.email)
    return serialized

# ----------------------------------------------- #
            ## To save new Query    ##
# ----------------------------------------------- #
def save_query(request, query, success_status):
    errors = []
    item = request.data.get("item", "")
    if item == "":
        errors.append({"item": "This field is required"})
    
    # Try getting query_title
    try:
        title = request.data.get("title", "")
    except ValueError:
        errors.append({"title": "Could not parse field"})
    
    # Try getting query_text
    try:
        query = request.data.get("query", "")
        if query == "" or str(quantity).strip()=="":
            errors.append({"query": "This field is required"})
        else:
            query = str(quantity).strip()
    except ValueError:
        errors.append({"query": "Could not parse field"})
    
    # Try getting author's email
    try:
        email = request.data.get("email", "")
        if email == "" or str(quantity).strip()=="":
            errors.append({"email": "This field is required"})
        else:
            email = str(quantity).strip()
    except ValueError:
        errors.append({"email": "Could not parse field"})
    
    date = request.data.get("date", "")
    if date == "":
        date = datetime.datetime.now()

    if len(errors) > 0:
        return HttpResponse(json.dumps(
            {
                "errors": errors
            }), status=status.HTTP_400_BAD_REQUEST)

    try:
        query.date = date
        query.title = title
        query.query = query
        query.email = email
        query.save()
    except Exception as e:
        return HttpResponse(json.dumps(
            {
                "errors": {"Query": str(e)}
            }), status=status.HTTP_400_BAD_REQUEST)

    return HttpResponse(json.dumps({"data": serialize_order(order)}), status=success_status)



# ----------------------------------------------- #
  ## Implement the API: POST, PUT and delete ##
# ----------------------------------------------- #
@api_view(['GET', 'POST'])
def queries(request):
    if request.user.is_anonymous:
        return HttpResponse(json.dumps({"detail": "Not authorized"}), status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "GET":
        queries_data = list(Query.objects.all())

        query_count = orders_data.count()
        
        '''page_size = int(request.GET.get("page_size", "10"))
        page_no = int(request.GET.get("page_no", "0"))
        queries_data = list(queries_data[page_no * page_size:page_no * page_size + page_size])'''
        
        query_data = [serialize_query(query) for query in queries_data]
        return HttpResponse(json.dumps({"count": queries_count, "data": queries_data}), status=status.HTTP_200_OK)
    
    if request.method == "POST":
        query = Query()
        return save_query(request, query, status.HTTP_201_CREATED)

    return HttpResponse(json.dumps({"detail": "Wrong method"}), status=status.HTTP_501_NOT_IMPLEMENTED)


@api_view(['GET', 'PUT', 'DELETE'])
def query(request, query_id):
    if request.user.is_anonymous:
        return HttpResponse(json.dumps({"detail": "Not authorized"}), status=status.HTTP_401_UNAUTHORIZED)

    try:
        query = Query.objects.get(pk=query_id)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({"detail": "Not found"}), status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        return HttpResponse(json.dumps({"data": serialize_query(query)}), status=status.HTTP_200_OK)

    if request.method == "PUT":
        return save_query(request, query, status.HTTP_200_OK)

    if request.method == "DELETE":
        query.delete()
        return HttpResponse(json.dumps({"detail": "deleted"}), status=status.HTTP_410_GONE)

    return HttpResponse(json.dumps({"detail": "Wrong method"}), status=status.HTTP_501_NOT_IMPLEMENTED)

































