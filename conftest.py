from pathlib import Path

import pytest
from pytest_html import extras
from playwright.sync_api import sync_playwright

from config import BASE_URL

@pytest.fixture(scope="session")
def browser():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)

    yield browser

    browser.close()
    p.stop()


@pytest.fixture
def page(browser, request):
    videos_dir = Path("videos")
    videos_dir.mkdir(exist_ok=True)

    context = browser.new_context(
        ignore_https_errors=True,
        record_video_dir=str(videos_dir),
    )
    page = context.new_page()

    page.goto(BASE_URL)
    page.wait_for_load_state("load")

    try:
        yield page
    finally:
        context.close()
        request.node.video_path = page.video.path()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, "extras", [])

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)

            file_name = screenshots_dir / f"{item.name}.png"

            page.screenshot(path=str(file_name))

            extra.append(extras.image(str(file_name)))

        report.extras = extra

    if report.when == "teardown":
        video_path = getattr(item, "video_path", None)

        if video_path and Path(video_path).exists():
            extra.append(
                extras.video(
                    str(video_path),
                    name="Test video",
                    mime_type="video/webm",
                    extension="webm",
                )
            )

            report.extras = extra