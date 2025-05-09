from behave import *
import requests

@given('Book "{name}" by "{author}" with ISBN number "{isbn}"')
def step_impl(context, name, author, isbn):
	context.name = name
	context.author = author
	context.isbn = isbn

@when('I store the book in the library')
def step_impl(context):
	request = requests.post("http://127.0.0.1:5000/books", json = {"isbn": context.isbn, "name": context.name,"author": context.author}, headers={'Content-Type': 'application/json'})
	assert request.status_code == 200, f"expected status code 200 but got {context.status_code}"

@then('I am able to retreive the book by ISBN number')
def step_impl(context):
	request = requests.get(f"http://127.0.0.1:5000/books/{context.isbn}")
	assert request.status_code == 200, f"it did not work :("
