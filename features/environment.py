from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver


def before_all(context):
    # default browser
    browser_name = "chrome"

    # browser selection by -D browser=browser_name
    if 'browser' in context.config.userdata:
        browser_name = context.config.userdata['browser']

    context.browser = _get_browser_driver_by_name(browser_name)


def after_all(context):
    context.browser.quit()


def _get_browser_driver_by_name(name):
    """
    Return the driver for the passed browser name
    :name: Name of the browser
    """
    if name == 'chrome':
        return webdriver.Chrome()
    elif name == 'firefox':
        return webdriver.Firefox()
    elif name == 'ie':
        return webdriver.Ie()
    elif name == 'htmlunit':
        return WebDriver(
            'http://localhost:4444/wd/hub',
            DesiredCapabilities.HTMLUNIT)
    else:
        raise RuntimeError("Browser name not found by: %s" % name)
