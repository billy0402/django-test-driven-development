from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        # Edith 前往首頁
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # 她發現輸入方塊已被妥善地置中
        input_box = self.browser.find_element_by_id('new_item')
        self.assertAlmostEqual(
            input_box.location['x'] + input_box.size['width'] / 2,
            self.browser.get_window_size()['width'] / 2,
            delta=10
        )

        # 她開始編輯一個新清單
        # 看到這裡的輸入欄位也妥善地置中
        input_box.send_keys('testing')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')
        input_box = self.browser.find_element_by_id('new_item')
        self.assertAlmostEqual(
            input_box.location['x'] + input_box.size['width'] / 2,
            self.browser.get_window_size()['width'] / 2,
            delta=10
        )
