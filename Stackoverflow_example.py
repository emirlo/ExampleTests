import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class StackOverflowTests(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)

    def test_stackoverflow_print_python_question_highest_votes(self):
        # 1. Navigate to google.com
        self.browser.get("https://www.google.com")
        
        # 2. Type in stackoverflow
        search_bar = self.browser.find_element_by_name("q")
        search_bar.send_keys("stackoverflow")
        search_bar.submit()

        # 3. Click the link for the official stackoverflow site
        stackoverflow_link = self.browser.find_element_by_css_selector('a[href="https://stackoverflow.com/"]')
        stackoverflow_link.click()

        # 4. Open the hamburger menu icon in the top left & select Tags
        hamburger_menu = self.browser.find_element_by_css_selector('a[role = "menuitem"]')
        hamburger_menu.click()
        hamburger_menu_item = self.browser.find_element_by_link_text("Tags")
        hamburger_menu_item.click()

        # 5. Type "python" into the 'filter by tag name' search bar
        # 6. Select the link for python-3.6
        filter_by_tag = self.browser.find_element_by_css_selector('[placeholder = "Filter by tag name"]')
        filter_by_tag.send_keys("python")
        python_version = self.browser.find_element_by_css_selector('a[href="/questions/tagged/python-3.6"]')
        python_version.click()

        # 7. Sort by most frequent
        more_button = self.browser.find_element_by_css_selector('[data-target = "se-uql.toggleMoreButton"]')
        more_button.click()
        more_dropdown = self.browser.find_element_by_id("uql-more-popover")
        filter_sort_frequent = more_dropdown.find_element_by_link_text("Frequent")
        filter_sort_frequent.click()

        # 8. Click the question with the highest number of votes
        highest_voted_question = self.browser.find_element_by_css_selector("#questions :first-child .summary h3 a")
        highest_voted_question.click()
        user_details = self.browser.find_element_by_css_selector(".user-details a")

        # 9. Print the author of the answer with the highest number of votes
        print(f"The user with the highest voted python 3.6 question is: {user_details.text}")

    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
        unittest.main()