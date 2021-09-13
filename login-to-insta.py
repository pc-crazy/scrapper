from selenium import webdriver


class InstaScrapper(object):

    def __init__(self):
        self.url = 'https://www.instagram.com/'
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)
        self.driver.implicitly_wait(15)

    def login(self, username, password):
        login_form = self.driver.find_element_by_xpath('//*[@id="loginForm"]')
        login_form.find_element_by_xpath('//input[@name="username"]').send_keys(username)
        login_form.find_element_by_xpath('//input[@name="password"]').send_keys(password)
        login_form.submit()

        try:
            self.driver.implicitly_wait(15)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
        except:
            pass

        try:
            self.driver.implicitly_wait(15)
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
        except:
            pass
        self.driver.save_screenshot("test.png")
        self.driver.close()
