import time

@when('visit url google')
def step(context):
    context.browser.get('http://www.google.com.pk')

@when('search for testingbot')
def step(context):
    elem = context.browser.find_element_by_name('q')
    elem.send_keys('testingbot')
    elem.submit()
    time.sleep(5)

@then('title becomes TestingBot')
def step(context, ):
    assert context.browser.title == 'testingbot - Google Search'

@then(u'page contains "{body}"')
def step(context, body):
    assert body in context.browser.page_source
