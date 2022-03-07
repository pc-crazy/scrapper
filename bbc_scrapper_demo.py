import csv
from urllib.parse import urlparse
from selenium import webdriver


class InstaScrapper(object):

    def __init__(self):
        self.url = 'https://www.bbc.com/'
        self.driver = webdriver.Chrome(executable_path="/home/paras/Downloads/chromedriver_linux64/chromedriver")
        self.driver.get(self.url)
        self.driver.implicitly_wait(15)
        self.urls = set()

    def start_scrap(self, username=None, password=None):
        for lnk in self.driver.find_elements_by_tag_name("a"):
            print(lnk.get_attribute("href"))
            url = lnk.get_attribute("href")
            url_parse = urlparse(url)
            if url_parse.netloc == "www.bbc.com":
                self.urls.add(url)


    def get_description_title_and_write_in_csv(self):
        with open('bbc_url.csv', 'w') as test_file:
            file_writer = csv.writer(test_file)
            file_writer.writerow(["URL", "HEADING", "DESCRIPTION"])
            for url in self.urls:
                main_heading = "Not Found"
                description = "Not Found"
                try:
                    self.driver.get(url)
                    self.driver.implicitly_wait(10)
                    main_heading = self.driver.find_element_by_id("main-heading").text
                    first_block = self.driver.find_element_by_xpath("//div[@data-component='image-block']/following-sibling::div[@data-component='text-block']")
                    description = ""
                    while first_block.get_attribute("data-component") == 'text-block':
                        description += first_block.text
                        first_block = first_block.find_element_by_xpath("following-sibling::div")
                    
                except Exception as e:
                    pass

                file_writer.writerow([url, main_heading, description])

if __name__ == "__main__":
    obj = InstaScrapper()
    obj.start_scrap()
    obj.get_description_title_and_write_in_csv()
    obj.driver.close()