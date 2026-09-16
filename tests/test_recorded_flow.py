import logging

from pages.login_page import LoginPage
from pages.overall_summary_page import OverallSummaryPage
from pages.test_script_helpers import _run_genai_validation

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_recorded_flow(page):
    login_page = LoginPage(page)
    overall_summary_page = OverallSummaryPage(page)

    login_page.open_authorize_page()
    login_page.login()
    overall_summary_page.select_market("Fresno, CA")
    overall_summary_page.open_point_analysis_and_show_more()
    _run_genai_validation(page, 'Verify that the ?Overall Performance - Contributing Metrics? table displays exactly 10 data rows, with metric data visible in each row.')
