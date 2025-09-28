import requests

base_url = "http://localhost:3000/api"

def get_users(count):
    user_url = f"{base_url}/users/{count}"
    response = requests.get(user_url)
    print(response.json())
    # time.sleep(1)

def get_products(count):
    product_url = f"{base_url}/products/{count}"
    response = requests.get(product_url)
    print(response.json())
    # time.sleep(1)

def get_companies(count):
    company_url = f"{base_url}/companies/{count}"
    response = requests.get(company_url)
    print(response.json())
    # time.sleep(1)

def get_credit_cards(count):
    credit_card_url = f"{base_url}/credit-cards/{count}"
    response = requests.get(credit_card_url)
    print(response.json())
    # time.sleep(1)

def get_jobs(count):
    job_url = f"{base_url}/jobs/{count}"
    response = requests.get(job_url)
    print(response.json())
    # time.sleep(1)

def get_text_contents(count):
    text_content_url = f"{base_url}/text-contents/{count}"
    response = requests.get(text_content_url)
    print(response.json())
    # time.sleep(1)


def main():
    for i in range(1, 14001):
        # print(f"\n\nRequest: {i}\n\n")
        get_users(i)
        get_products(i)
        get_companies(i)
        get_credit_cards(i)
        get_jobs(i)
        get_text_contents(i)

if __name__ == "__main__":
    main()