import pytest
from pages.technologies import C_tech


@pytest.mark.smoke
def test_ecoptions(page):
    ec = C_tech(page)
    ec.ec_options()

@pytest.mark.smoke
def test_madoptions(page):
    mad = C_tech(page)
    mad.mad_options()

@pytest.mark.smoke
def test_aioptions(page):
    ai = C_tech(page)
    ai.ai_options()
    



