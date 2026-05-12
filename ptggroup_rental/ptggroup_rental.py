import reflex as rx
from pages.explorepage.explorePage import explore_page
from pages.landingpage.landingPage import landing_page
from pages.loginpage.loginpage import login_page
from pages.pricingpage.pricingPage import pricing_page
from pages.stationdetailpage.stationDetailsPage import station_detail_page
from pages.checkoutpage.checkoutPage import checkout_growth_page, checkout_pro_page
from pages.createaccountpage.createAccountPage import create_account_page


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
