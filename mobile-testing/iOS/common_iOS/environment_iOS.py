from appium import webdriver


class Environment:

    def set_capabilities(context):
        desired_caps = {}

        desired_caps['platformName']            = 'iOS'
        desired_caps['avd']                     = 'iPhone 11'
        desired_caps['deviceName']              = 'iPhone 11'
        desired_caps['automationName']          = 'XCUITest'
        desired_caps['autoGrantPermissions']    = True
        desired_caps['autoAcceptAlerts']        = True
        desired_caps['locationServicesEnabled'] = True
        desired_caps['autoDismissAlerts']       = True
        desired_caps['noReset']                 = False
        desired_caps['newCommandTimeout']       = 60000
        desired_caps['app']                     = context.config.userdata['app_folder_location']
        context.driver                          = webdriver.Remote(
                context.config.userdata['appium_server'], desired_caps)