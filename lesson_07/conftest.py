from pathlib import Path

import pytest

SCREENSHOT_DIR = Path(__file__).parent / "screenshots"


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")  # имя твоей фикстуры с браузером
        if driver is None:
            return

        SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
        filename = f"{item.name}.png"
        path = SCREENSHOT_DIR / filename
        driver.save_screenshot(str(path))
