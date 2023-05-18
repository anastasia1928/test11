from playwright.sync_api import Page
import config


class IndexPage:
    _BUTTON_GOOGlE_SEARCH = "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']"


    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)




        def open_index_page(self, page: Page) -> None:
        return page.locator(self._BUTTON_GOOGlE_SEARCH).get_attribute('value')
