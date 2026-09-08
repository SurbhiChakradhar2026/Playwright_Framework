


import pytest

from Pages.technologies import Tech


@pytest.mark.smoke
def test_techecomdev(page):
    tech1=Tech(page)
    tech1.ecom_dev()

@pytest.mark.smoke
def test_techmobiledev(page):
    tm=Tech(page)
    tm.mob_app_dev()
@pytest.mark.smoke
def test_artificialIntelligence(page):
    ai=Tech(page)
    ai.artifical_intellligence()