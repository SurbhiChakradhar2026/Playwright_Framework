


import pytest
from Pages.contactUs import ContactUs
@pytest.mark.smoke
def test_formDetails(page):
    details=ContactUs(page)
    details.formDetails()

def test_webdevlopemtLinks(page):
    link1=ContactUs(page)
    link1.webdevelopmentLinks()

def test_AppDevlopmentLinks(page):
    link2=ContactUs(page)
    link2.appDevelopment()

def test_graphicDesignLinks(page):
    link3=ContactUs(page)
    link3.graphichDesign()

def test_socialMediaLinks(page):
    sm=ContactUs(page)
    sm.socialMedia_Links()
    