


import pytest

from Pages.blog import Blog


@pytest.mark.smoke
def test_blog(page):
    blog1=Blog(page)
    blog1.blog_options()
