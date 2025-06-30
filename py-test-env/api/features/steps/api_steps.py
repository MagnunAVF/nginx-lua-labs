from behave import when, then
import requests

RESPONSE = None
BASE_URL = "http://localhost:1666"

@when('I make a GET request to "{endpoint}"')
def step_make_get_request(context, endpoint):
    global RESPONSE
    RESPONSE = requests.get(f"{BASE_URL}{endpoint}")

@then('the response status code should be {status_code:d}')
def step_check_status_code(context, status_code):
    assert RESPONSE.status_code == status_code, f"Expected status code {status_code}, but got {RESPONSE.status_code}"

@then('the response body should be "{expected_body}"')
def step_check_response_body(context, expected_body):
    assert RESPONSE.text == expected_body, f"Expected body '{expected_body}', but got '{RESPONSE.text}'"
