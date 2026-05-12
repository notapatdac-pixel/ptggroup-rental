import reflex as rx
from pages.explorepage.explorePage import explore_page
from pages.landingpage.landingPage import landing_page
from pages.loginpage.loginpage import login_page
from pages.pricingpage.pricingPage import pricing_page
from pages.stationdetailpage.stationDetailsPage import station_detail_page
from pages.checkoutpage.checkoutPage import checkout_growth_page, checkout_pro_page
from pages.createaccountpage.createAccountPage import create_account_page
from pages.retailerdashboardpage.retailerDashboardPage import retailer_dashboard_page
from pages.performancepage.performancePage import performance_page
from pages.mlpredictionspage.mlPredictionsPage import ml_predictions_page
from pages.submitstoredatapage.submitStoreDataPage import submit_store_data_page
from pages.myapplicationspage.myApplicationsPage import my_applications_page
from pages.aiadvisorpage.aiAdvisorPage import ai_advisor_page
from pages.approveddocspage.approvedDocsPage import approved_docs_page
from pages.schedulechatpage.scheduleChatPage import schedule_chat_page
from pages.bookingconfirmpage.bookingConfirmPage import booking_confirm_page
from pages.explorelocationpage.exploreLocationPage import explore_location_page
from pages.slotselectionpage.slotSelectionPage import slot_selection_page
from pages.confirmapplypage.confirmApplyPage import confirm_apply_page


app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&family=DM+Serif+Display:ital@0;1&family=Newsreader:ital,opsz,wght@0,6..72,200..800;1,6..72,200..800&family=Inter:wght@100..900&display=swap",
        "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap",
        "https://unpkg.com/leaflet@1.9.4/dist/leaflet.css",
        "/style/global.css",
    ]
)
app.add_page(landing_page, route="/", title="PTG Retail Platform | Thailand's Premier Retail Marketplace")
app.add_page(pricing_page, route="/pricingpage", title="PTG Retail Platform | Pricing")
app.add_page(explore_page, route="/explorepage", title="PTG Retail Platform | Explore Locations")
app.add_page(login_page, route="/loginpage", title="PTG Retail Platform | Sign In")
app.add_page(
    station_detail_page,
    route="/stationdetailpage/[station_id]",
    title="PTG Retail Platform | Station",
)
app.add_page(checkout_growth_page, route="/checkoutpage/growth", title="PTG Retail Platform | Checkout — Growth Plan")
app.add_page(checkout_pro_page, route="/checkoutpage/pro", title="PTG Retail Platform | Checkout — Pro Plan")
app.add_page(create_account_page, route="/createaccountpage", title="PTG Retail Platform | Create Account")

# ── Retailer Backoffice ────────────────────────────────────────────────
app.add_page(retailer_dashboard_page, route="/retailerdashboard", title="PTG Retailer | Dashboard")
app.add_page(performance_page, route="/retailerperformance", title="PTG Retailer | Performance")
app.add_page(ml_predictions_page, route="/retailerml", title="PTG Retailer | ML Growth Intelligence")
app.add_page(submit_store_data_page, route="/retailersubmitdata", title="PTG Retailer | Submit Store Data")
app.add_page(my_applications_page, route="/retailerapplications", title="PTG Retailer | My Applications")
app.add_page(ai_advisor_page, route="/retaileraiadvisor", title="PTG Retailer | AI Advisor")
app.add_page(approved_docs_page, route="/retailerapprovedocs", title="PTG Retailer | Application Approved")
app.add_page(schedule_chat_page, route="/retailerschedulechat", title="PTG Retailer | Schedule Walkthrough")
app.add_page(booking_confirm_page, route="/retailerbookingconfirm", title="PTG Retailer | Booking Confirmed")
app.add_page(explore_location_page, route="/retailerexplorelocation", title="PTG Retailer | Explore Location")
app.add_page(slot_selection_page, route="/retailerslotselection", title="PTG Retailer | Slot Selection")
app.add_page(confirm_apply_page, route="/retailerconfirmapply", title="PTG Retailer | Confirm & Apply")
