from selenium import webdriver
from selenium import remote


def before_all(context):
    # default browser
    browser_name = "chrome"
    context.browser = _get_browser_driver_by_name(browser_name)


def after_all(context):
    pass


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
        return remote.connect('htmlunit')
    else:
        raise RuntimeError("Browser name not found by: %s" % name)
