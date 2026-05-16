import reflex as rx

# Mock accounts — delete this dict when real DB auth is implemented
_MOCK_ACCOUNTS: dict[str, dict] = {
    "retailer@ptg.test": {
        "password": "retailer123",
        "name": "Siriporn K.",
        "type": "retailer",
        "avatar_color": "#2d5a1b",
    },
    "landlord@ptg.test": {
        "password": "landlord123",
        "name": "Wanchai P.",
        "type": "landlord",
        "avatar_color": "#466800",
    },
}


class AuthState(rx.State):
    logged_in: bool = False
    user_type: str = ""
    user_name: str = ""
    user_email: str = ""

    email_input: str = ""
    password_input: str = ""
    login_error: str = ""

    nav_dropdown_open: bool = False

    @rx.var
    def initials(self) -> str:
        return self.user_name[0].upper() if self.user_name else "?"

    def set_email(self, val: str):
        self.email_input = val
        self.login_error = ""

    def set_password(self, val: str):
        self.password_input = val
        self.login_error = ""

    def login(self):
        account = _MOCK_ACCOUNTS.get(self.email_input.strip().lower())
        if account and account["password"] == self.password_input:
            self.logged_in = True
            self.user_type = account["type"]
            self.user_name = account["name"]
            self.user_email = self.email_input.strip().lower()
            self.login_error = ""
            self.email_input = ""
            self.password_input = ""
            if account["type"] == "landlord":
                return rx.redirect("/landlorddashboard")
            return rx.redirect("/retailerdashboard")
        self.login_error = "Invalid email or password."

    def logout(self):
        self.logged_in = False
        self.user_type = ""
        self.user_name = ""
        self.user_email = ""
        self.nav_dropdown_open = False
        return rx.redirect("/loginpage")

    def require_auth(self):
        self.nav_dropdown_open = False
        if not self.logged_in:
            return rx.redirect("/loginpage")

    def require_landlord_auth(self):
        self.nav_dropdown_open = False
        if not self.logged_in or self.user_type != "landlord":
            return rx.redirect("/loginpage")

    def toggle_nav_dropdown(self):
        self.nav_dropdown_open = not self.nav_dropdown_open

    def close_nav_dropdown(self):
        self.nav_dropdown_open = False
