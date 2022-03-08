class DriverManager:

    def __init__(self, driver):
        self.driver = driver

    
    def quit_app(self):
        self.driver.close_app()
        self.driver.quit()