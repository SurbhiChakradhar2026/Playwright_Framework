
import pytest
from pages.verticals import cls_Verti

@pytest.mark.smoke
def test_trading(page):
    trade = cls_Verti(page)
    trade.click_trading_options()

@pytest.mark.smoke
def test_rae(page):
    rae = cls_Verti(page)
    rae.click_rae_options()

@pytest.mark.smoke
def test_hc(page):
    hc = cls_Verti(page)
    hc.click_hc_options()

@pytest.mark.smoke
def test_ft(page):
    ft = cls_Verti(page)
    ft.click_ft_options()

@pytest.mark.smoke
def test_ca(page):
    ca = cls_Verti(page)
    ca.click_ca_options()