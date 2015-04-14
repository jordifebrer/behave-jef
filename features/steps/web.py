from behave import *


@step("I open the following url {url}")
def step_impl(context, url):
    br = context.browser
    br.get(url)


@step("I am on the {name} website")
def step_impl(context, name):
    br = context.browser
    assert name in br.current_url
