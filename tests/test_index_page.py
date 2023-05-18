import pytest
import pages



class TestFooter:

    def test_user_should_be_able_to_open_popup_select_subscription_plan(self, page):
        pages.index_page.open_index_page(page)
        result = pages.index_page.get_text_from_google_search_button(page)

        assert result == 'Поиск в Google', 'Google Search button text is not correct'

