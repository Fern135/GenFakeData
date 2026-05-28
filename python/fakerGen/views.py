import asyncio
import random
from django.http import JsonResponse
from faker import Faker

fake = Faker()
Faker.seed(random.random())


def _build_users(count):
    print("building users")
    return [
        {
            "id": i + 1,
            "name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
        }
        for i in range(1, count + 1)
    ]

def _build_products(count):
    print("building products")
    return [
        {
            "id": i + 1,
            "name": f"{fake.word().capitalize()} {fake.word().capitalize()}",
            "price": fake.pricetag(),
            "category": fake.bs(),
        }
        for i in range(1, count + 1)
    ]

def _build_companies(count):
    print("building companies")
    return [
        {
            "id": i + 1,
            "name": fake.company(),
            "catchPhrase": fake.catch_phrase(),
            "industry": fake.bs(),
        }
        for i in range(1, count + 1)
    ]

def _build_credit_cards(count):
    print("building cc")
    card_types = ["Visa", "MasterCard", "American Express", "Discover"]
    return [
        {
            "id": i + 1,
            "number": fake.credit_card_number(),
            "type": random.choice(card_types),
            "expDate": fake.future_date(end_date="+5y").isoformat(),
        }
        for i in range(1, count + 1)
    ]

def _build_jobs(count):
    print("building jobs")
    return [
        {
            "id": i + 1,
            "title": fake.job(),
            "company": fake.company(),
            "location": fake.city(),
        }
        for i in range(1, count + 1)
    ]

def _build_text(count):
    print("building text")
    return [
        {
            "id": i + 1,
            "text": fake.paragraph(),
        }
        for i in range(1, count + 1)
    ]


async def genUsers(_, count=10):
    data = await asyncio.to_thread(_build_users, count)
    return JsonResponse({"message": data}, status=200)

async def genProducts(_, count=10):
    data = await asyncio.to_thread(_build_products, count)
    return JsonResponse({"message": data}, status=200)

async def genCompanies(_, count=10):
    data = await asyncio.to_thread(_build_companies, count)
    return JsonResponse({"message": data}, status=200)

async def genCreditCards(_, count=10):
    data = await asyncio.to_thread(_build_credit_cards, count)
    return JsonResponse({"message": data}, status=200)

async def genJobs(_, count=10):
    data = await asyncio.to_thread(_build_jobs, count)
    return JsonResponse({"message": data}, status=200)

async def genText(_, count=10):
    data = await asyncio.to_thread(_build_text, count)
    return JsonResponse({"message": data}, status=200)
