from pages.overall_summary_page import OverallSummaryPage


def test_selected_chart_highlight(page,valid_login):
    overall_summary_page = OverallSummaryPage(page)
    overall_summary_page.handle_welcome_popup()
    overall_summary_page.click_att_carrier()
    overall_summary_page.click_tmobile_carrier()
    overall_summary_page.click_verizon_carrier()