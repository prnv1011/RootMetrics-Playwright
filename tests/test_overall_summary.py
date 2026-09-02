from pages.overall_summary_page import OverallSummaryPage

def test_carrier_presence(page, valid_login):
    overall_summary_page = OverallSummaryPage(page)
    overall_summary_page.handle_welcome_popup()
    overall_summary_page.click_and_verify_overall()
    overall_summary_page.click_and_verify_reliability()
    overall_summary_page.click_and_verify_responsiveness()
    overall_summary_page.click_and_verify_speed()
    overall_summary_page.click_and_verify_data()
    overall_summary_page.click_and_verify_call()
    overall_summary_page.click_and_verify_text()
    overall_summary_page.click_and_verify_video()
    overall_summary_page.verify_att_carrier_presence()
    overall_summary_page.verify_tmobile_carrier_presence()
    overall_summary_page.verify_verizon_carrier_presence()
    overall_summary_page.click_download_dropdown()
    overall_summary_page.click_export_view()
    download = overall_summary_page.download_file()
    download.save_as("downloads/report.xlsx")


from pages.overall_summary_page import OverallSummaryPage


def test_carrier_presence(page, valid_login):
    overall_summary_page = OverallSummaryPage(page)
    overall_summary_page.handle_welcome_popup()
    overall_summary_page.click_and_verify_overall()
    overall_summary_page.click_and_verify_reliability()
    overall_summary_page.click_and_verify_responsiveness()
    overall_summary_page.click_and_verify_speed()
    overall_summary_page.click_and_verify_data()
    overall_summary_page.click_and_verify_call()
    overall_summary_page.click_and_verify_text()
    overall_summary_page.click_and_verify_video()
    overall_summary_page.verify_att_carrier_presence()
    overall_summary_page.verify_tmobile_carrier_presence()
    overall_summary_page.verify_verizon_carrier_presence()
    overall_summary_page.click_download_dropdown()
    overall_summary_page.click_export_view()
    download = overall_summary_page.download_file()
    download.save_as("downloads/report.xlsx")
