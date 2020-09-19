import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = self.set_up_browser()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    @staticmethod
    def set_up_browser():
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        options.add_argument('-private')
        return webdriver.Firefox(options=options)

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith 聽到一個很酷的新線上待辦事項 app
        # 她去查看它的首頁
        self.browser.get('http://localhost:8000')

        # 她發現網頁標題與標頭顯示待辦事項清單
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 她馬上受邀輸入一個待辦事項
        input_box = self.browser.find_element_by_id('new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 她在文字方塊輸入 "購買孔雀羽毛"
        # (Edith 的興趣是綁蒼蠅魚餌)
        input_box.send_keys('Buy peacock feathers')

        # 當她按下 enter 時，網頁會更新，現在網頁列出
        # "1. 購買孔雀羽毛"，一個待辦事項清單項目
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # 此時仍然有一個文字方塊，讓她可以加入另一個項目
        # 她輸入 "使用孔雀羽毛來製作一隻蒼蠅" (Edith 非常有條理)
        input_box = self.browser.find_element_by_id('new_item')
        input_box.send_keys('Use peacock feathers to make a fly')
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        # 網頁再次更新，現在她的清單有這兩個項目
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Edith 不知道網站能否記得她的清單
        # 接著她看到網站產生一個唯一的 URL 給她
        # 網頁有一些文字說明這個效果
        self.fail('Finish the test!')

        # 她前往那個 URL - 她的待辦清單仍然在那裡

        # 她很滿意地上床睡覺


if __name__ == '__main__':
    unittest.main(warnings='ignore')
