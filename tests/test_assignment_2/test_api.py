# Databricks notebook source

def test_api_integration():
    # Fetch data from API
    base_url = "https://reqres.in/api/users"
    page = 1
    data_available = True
    all_data = []

    while data_available:
        response = requests.get(f"{base_url}?page={page}")
        data = response.json().get("data", [])
        if not data:
            data_available = False
        else:
            all_data.extend(data)
            page += 1
