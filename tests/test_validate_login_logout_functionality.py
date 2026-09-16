from pages.overall_summary_page import OverallSummaryPage


def test_login_logout_flow(valid_login):
    overall_summary_page = OverallSummaryPage(valid_login)
    overall_summary_page.verify_summary_page_title()
    overall_summary_page.handle_welcome_popup()
    overall_summary_page.click_user_menu()
    overall_summary_page.click_logout()
    overall_summary_page.verify_login_page_title()


from pages.overall_summary_page import OverallSummaryPage
from pages.test_script_helpers import _run_genai_validation


def test_login_logout_flow(valid_login):
    overall_summary_page = OverallSummaryPage(valid_login)
    overall_summary_page.verify_summary_page_title()
    overall_summary_page.handle_welcome_popup()
    overall_summary_page.click_user_menu()
    overall_summary_page.click_logout()
    overall_summary_page.verify_login_page_title()


def test_national_route_no_rootscore_validation(valid_login):
    overall_summary_page = OverallSummaryPage(valid_login)
    overall_summary_page.verify_summary_page_title()
    overall_summary_page.handle_welcome_popup()
    overall_summary_page.click_and_verify_overall()
    overall_summary_page.click_national_route_link()
    instruction = 'Verify that no RootScore values or carrier ranking positions are displayed for any carrier.'
    _run_genai_validation(valid_login, instruction)
