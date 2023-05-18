from playwright.sync_api import Page
import config


class IndexPage:
    _BUTTON_GOOGlE_SEARCH = "//div[@class='FPdoLc lJ9FBc']//input[@class='gNO89b']"

    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    def get_text_from_google_search_button(self, page: Page) -> None:
        return page.locator(self._BUTTON_GOOGlE_SEARCH).get_attribute('value')
