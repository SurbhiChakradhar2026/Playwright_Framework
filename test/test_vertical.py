


import pytest

from Pages.verticals import vertical

@pytest.mark.smoke
def test_trading(page):
    trade=vertical(page)
    trade.trading_options()
@pytest.mark.smoke
def retailEcom(page):
    trade1=vertical(page)
    trade1.retail_ecommerce_options()
@pytest.mark.smoke
def healthcare(page):
    healthcare=vertical(page)
    healthcare.healthcare_options()

@pytest.mark.smoke
def fintech(page):
    fin=vertical(page)
    fin.fintech_options()
@pytest.mark.smoke
def customApp(page):
    custom=vertical(page)
    custom.custom_app_options()