from pages.overall_summary_page import OverallSummaryPage


def test_completed_markets(page, valid_login):
    overall_summary_page = OverallSummaryPage(page)
    overall_summary_page.handle_welcome_popup()
    overall_summary_page.click_and_verify_completed_market_checkbox()
    overall_summary_page.verify_completed_markets()