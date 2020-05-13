import AppiumLibrary

class headspinPythonLib(object):

    ROBOT_LIBRARY_VERSION = 1.0

    def __init__(self):
        pass

    def get_webdriver(self,libraryInstance):

          # following line returns WebDriver initiated in robot-framework
          webdriver=libraryInstance._current_application()

          return webdriver
        #  webdriver.get("https://adiralashivaprasad.blogspot.in")
          
