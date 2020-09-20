import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

MAX_WAIT = 10


class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = self.set_up_browser()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        # self.browser.refresh()
        self.browser.quit()

    @staticmethod
    def set_up_browser():
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        options.add_argument('-private')
        return webdriver.Firefox(options=options)

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return None
            except(AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_for_one_user(self):
        # Edith 聽到一個很酷的新線上待辦事項 app
        # 她去查看它的首頁
        self.browser.get(self.live_server_url)

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
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # 此時仍然有一個文字方塊，讓她可以加入另一個項目
        # 她輸入 "使用孔雀羽毛來製作一隻蒼蠅" (Edith 非常有條理)
        input_box = self.browser.find_element_by_id('new_item')
        input_box.send_keys('Use peacock feathers to make a fly')
        input_box.send_keys(Keys.ENTER)

        # 網頁再次更新，現在她的清單有這兩個項目
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # 她很滿意地上床睡覺

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith 輸入一個新的項目，做出一個新的清單
        self.browser.get(self.live_server_url)
        input_box = self.browser.find_element_by_id('new_item')
        input_box.send_keys('Buy peacock feathers')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # Edith 取得他自己獨一無二的 URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/todos/.+')

        # 在新的使用者 Francis 來到網站

        ## 我們使用一個新的瀏覽器工作階段來確保
        ## Edith 的任何資訊都不會被 cookies 等機制送出
        self.browser.quit()
        self.browser = self.set_up_browser()

        # Francis 造訪首頁，沒有任何 Edith 的清單的跡象
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis 輸入一個新的項目，做出一個新的清單
        # 他比 Edith 無趣
        input_box = self.browser.find_element_by_id('new_item')
        input_box.send_keys('Buy milk')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Francis 取得他自己獨一無二的 URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/todos/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # 同樣的，沒有 Edith 的清單的跡象
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # 他們都很滿意的回去睡覺了

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
