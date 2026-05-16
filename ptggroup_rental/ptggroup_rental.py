import reflex as rx
from pages.explorepage.explorePage import explore_page
from pages.landingpage.landingPage import landing_page
from pages.loginpage.loginpage import login_page
from pages.pricingpage.pricingPage import pricing_page
from pages.stationdetailpage.stationDetailsPage import station_detail_page
from pages.checkoutpage.checkoutPage import checkout_growth_page, checkout_pro_page
from pages.createaccountpage.createAccountPage import create_account_page
from pages.retailer_backoffice.retailerDashboardPage import retailer_dashboard_page
from pages.retailer_backoffice.performancePage import performance_page
from pages.retailer_backoffice.mlPredictionsPage import ml_predictions_page
from pages.retailer_backoffice.submitStoreDataPage import submit_store_data_page
from pages.retailer_backoffice.myApplicationsPage import my_applications_page
from pages.retailer_backoffice.aiAdvisorPage import ai_advisor_page
from pages.retailer_backoffice.approvedDocsPage import approved_docs_page
from pages.retailer_backoffice.scheduleChatPage import schedule_chat_page
from pages.retailer_backoffice.bookingConfirmPage import booking_confirm_page
from pages.retailer_backoffice.exploreLocationPage import explore_location_page
from pages.retailer_backoffice.slotSelectionPage import slot_selection_page
from pages.retailer_backoffice.confirmApplyPage import confirm_apply_page
from pages.retailer_backoffice.retailerProfileSetupPage import retailer_profile_setup_page
from pages.landlord_backoffice.landlordOverviewPage import landlord_overview_page
from pages.landlord_backoffice.landlordMyStationsPage import landlord_my_stations_page
from pages.landlord_backoffice.landlordEditStationPage import landlord_edit_station_page
from pages.landlord_backoffice.landlordApplicationsPage import landlord_applications_page
from pages.landlord_backoffice.landlordTenantsPage import landlord_tenants_page
from pages.landlord_backoffice.landlordRevenuePage import landlord_revenue_page
from pages.landlord_backoffice.landlordAiAdvisorPage import landlord_ai_advisor_page
from component.auth_state import AuthState


app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&family=DM+Serif+Display:ital@0;1&family=Newsreader:ital,opsz,wght@0,6..72,200..800;1,6..72,200..800&family=Inter:wght@100..900&display=swap",
        "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap",
        "https://unpkg.com/leaflet@1.9.4/dist/leaflet.css",
        "/style/global.css",
    ]
)
_close_dd = AuthState.close_nav_dropdown
app.add_page(landing_page, route="/", title="PTG Retail Platform | Thailand's Premier Retail Marketplace", on_load=_close_dd)
app.add_page(pricing_page, route="/pricingpage", title="PTG Retail Platform | Pricing", on_load=_close_dd)
app.add_page(explore_page, route="/explorepage", title="PTG Retail Platform | Explore Locations", on_load=_close_dd)
app.add_page(login_page, route="/loginpage", title="PTG Retail Platform | Sign In", on_load=_close_dd)
app.add_page(
    station_detail_page,
    route="/stationdetailpage/[station_id]",
    title="PTG Retail Platform | Station",
    on_load=_close_dd,
)
app.add_page(checkout_growth_page, route="/checkoutpage/growth", title="PTG Retail Platform | Checkout — Growth Plan", on_load=_close_dd)
app.add_page(checkout_pro_page, route="/checkoutpage/pro", title="PTG Retail Platform | Checkout — Pro Plan", on_load=_close_dd)
app.add_page(create_account_page, route="/createaccountpage", title="PTG Retail Platform | Create Account", on_load=_close_dd)

# ── Retailer Backoffice (auth-protected) ──────────────────────────────
_auth = AuthState.require_auth
app.add_page(retailer_dashboard_page, route="/retailerdashboard", title="PTG Retailer | Dashboard", on_load=_auth)
app.add_page(performance_page, route="/retailerperformance", title="PTG Retailer | Performance", on_load=_auth)
app.add_page(ml_predictions_page, route="/retailerml", title="PTG Retailer | ML Growth Intelligence", on_load=_auth)
app.add_page(submit_store_data_page, route="/retailersubmitdata", title="PTG Retailer | Submit Store Data", on_load=_auth)
app.add_page(my_applications_page, route="/retailerapplications", title="PTG Retailer | My Applications", on_load=_auth)
app.add_page(ai_advisor_page, route="/retaileraiadvisor", title="PTG Retailer | AI Advisor", on_load=_auth)
app.add_page(approved_docs_page, route="/retailerapprovedocs", title="PTG Retailer | Application Approved", on_load=_auth)
app.add_page(schedule_chat_page, route="/retailerschedulechat", title="PTG Retailer | Schedule Walkthrough", on_load=_auth)
app.add_page(booking_confirm_page, route="/retailerbookingconfirm", title="PTG Retailer | Booking Confirmed", on_load=_auth)
app.add_page(explore_location_page, route="/retailerexplorelocation", title="PTG Retailer | Explore Location", on_load=_auth)
app.add_page(slot_selection_page, route="/retailerslotselection", title="PTG Retailer | Slot Selection", on_load=_auth)
app.add_page(confirm_apply_page, route="/retailerconfirmapply", title="PTG Retailer | Confirm & Apply", on_load=_auth)
app.add_page(retailer_profile_setup_page, route="/retailerprofilesetup", title="PTG Retailer | Profile Setup", on_load=_auth)

# ── Landlord Backoffice (auth-protected) ──────────────────────────────────
_landlord_auth = AuthState.require_landlord_auth
app.add_page(landlord_overview_page, route="/landlorddashboard", title="PTG Landlord | Overview", on_load=_landlord_auth)
app.add_page(landlord_my_stations_page, route="/landlordstations", title="PTG Landlord | My Stations", on_load=_landlord_auth)
app.add_page(landlord_edit_station_page, route="/landlordeditstations", title="PTG Landlord | Edit Station", on_load=_landlord_auth)
app.add_page(landlord_applications_page, route="/landlordapplications", title="PTG Landlord | Applications", on_load=_landlord_auth)
app.add_page(landlord_tenants_page, route="/landlordtenants", title="PTG Landlord | Active Tenants", on_load=_landlord_auth)
app.add_page(landlord_revenue_page, route="/landlordrevenue", title="PTG Landlord | Revenue Portfolio", on_load=_landlord_auth)
app.add_page(landlord_ai_advisor_page, route="/landlordaiadvisor", title="PTG Landlord | AI Advisor", on_load=_landlord_auth)
