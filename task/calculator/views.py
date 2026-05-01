from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def add(request):
    a = float(request.GET.get("a", 0))
    b = float(request.GET.get("b", 0))
    return Response({"operation": "add", "a": a, "b": b, "result": a + b})


@api_view(["GET"])
def subtract(request):
    a = float(request.GET.get("a", 0))
    b = float(request.GET.get("b", 0))
    return Response({"operation": "subtract", "a": a, "b": b, "result": a - b})


@api_view(["GET"])
def multiply(request):
    a = float(request.GET.get("a", 0))
    b = float(request.GET.get("b", 0))
    return Response({"operation": "multiply", "a": a, "b": b, "result": a * b})


@api_view(["GET"])
def divide(request):
    a = float(request.GET.get("a", 0))
    b = float(request.GET.get("b", 0))
    if b == 0:
        return Response({"error": "Division by zero is not allowed."}, status=400)
    return Response({"operation": "divide", "a": a, "b": b, "result": a / b})
