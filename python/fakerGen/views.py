import random
from django.http import JsonResponse
from faker import Faker

fake = Faker()
Faker.seed(random.random())




def genUsers(request, count=10):
    data = []
    for i in range(1, count + 1):
        data.append(
            {   
                "id" : i + 1,
                "name" : fake.name(),
                "email" : fake.email(),
                "phone" : fake.phone_number(),
            }
        )

    return JsonResponse({ "message" : data }, status=200)

def genProducts(request, count=10):
    data = []
    for i in range(1, count + 1):
        data.append(
            {
                "id" : i + 1,
                "name" : f"{fake.word().capitalize()} {fake.word().capitalize()}",
                "price" : fake.pricetag(),
                "category" : fake.bs(),
            }
        )

    return JsonResponse({ "message" : data }, status=200)

def genCompanies(request, count=10):
    data = []
    for i in range(1, count + 1):
        data.append(
            {
                "id" : i + 1,
                "name" : fake.company(),
                "catchPhrase" : fake.catch_phrase(),
                "industry" : fake.bs(),
            }
        )

    return JsonResponse({ "message" : data }, status=200)

def genCreditCards(request, count=10):
    cardTypes = ["Visa", "MasterCard", "American Express", "Discover"]
    data = []
    for i in range(1, count + 1):
        data.append(
            {
                "id" : i + 1,
                "number" : fake.credit_card_number(),
                "type" : random.choice(cardTypes),
                "expDate" : fake.future_date(end_date="+5y").isoformat(),
            }
        )

    return JsonResponse({ "message" : data }, status=200)

def genJobs(request, count=10):
    data = []
    for i in range(1, count + 1):
        data.append(
            {
                "id" : i + 1,
                "title" : fake.job(),
                "company" : fake.company(),
                "location" : fake.city(),
            }
        )

    return JsonResponse({ "message" : data }, status=200)

def genText(request, count=10):
    data = []
    for i in range(1, count + 1):
        data.append(
            {
                "id" : i + 1,
                "text" : fake.paragraph(),
            }
        )

    return JsonResponse({ "message" : data }, status=200)

