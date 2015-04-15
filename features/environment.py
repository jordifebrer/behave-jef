from selenium import webdriver


def before_all(context):
    # default browser
    browser_name = "htmlunit"
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
        return webdriver.Remote(
            desired_capabilities=webdriver.DesiredCapabilities.HTMLUNIT)
    else:
        raise RuntimeError("Browser name not found by: %s" % name)
