


import pytest

from Pages.portfolio import Portfolio


@pytest.mark.smoke
def test_portfolio(page):
    port=Portfolio(page)
    port.viewMore_click()