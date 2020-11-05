from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Edith 前往首頁，並且不小心提交一個空的清單項目
        # 她在空的輸入方塊中按下 Enter
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('new_item').send_keys(Keys.ENTER)

        # 首頁重新整理，有一個錯誤訊息，說不能有空白的清單項目
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
        ))

        # 她再試一次，在項目中加入一些文字，現在可以動作了
        self.browser.find_element_by_id('new_item').send_keys('Buy milk')
        self.browser.find_element_by_id('new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # 離譜的是，現在她決定要提交第二個空白的清單項目
        self.browser.find_element_by_id('new_item').send_keys(Keys.ENTER)

        # 她在清單網頁上看到類似的警告
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
        ))

        # 她可以填入一些文字來修正它
        self.browser.find_element_by_id('new_item').send_keys('Make tea')
        self.browser.find_element_by_id('new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')
