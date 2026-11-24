import os
import allure
import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page and not page.is_closed():
            allure.attach(
                page.screenshot(),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )

@pytest.fixture(autouse=True)
def attach_video_on_failure(request):
    yield
    rep = getattr(request.node, "rep_call", None)
    if rep and rep.failed:
        page = request.node.funcargs.get("page")
        if page and page.video:
            video_path = page.video.path()
            page.context.close()
            if os.path.exists(video_path):
                allure.attach.file(
                    video_path,
                    name="failure_video",
                    attachment_type=allure.attachment_type.WEBM
                )

@pytest.fixture(scope = 'session', autouse= True)
def beforeAll():
    print("Starting Test Suite")
    yield
    print("Completed Test Suite")

@pytest.fixture(scope="function", autouse=True)
def block_ads(context):
    ad_domains = [
        "**/*googleads*",
        "**/*doubleclick*",
        "**/*googlesyndication*",
        "**/*adtrafficquality*",
        "**/*google_vignette*",
        "**/*adservice*",
    ]
    for pattern in ad_domains:
        context.route(pattern, lambda route: route.abort())


@pytest.fixture(scope = 'function', autouse= True)
def beforeEach():
    print("Starting individual method")
    yield
    print("Ending individual method")

