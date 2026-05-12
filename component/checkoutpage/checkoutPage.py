import reflex as rx
import os
from component.landingpage.footer import footer
from component.landingpage.nav_bar import nav_bar
from component.checkoutpage.checkout_payment_form import checkout_payment_form
from component.checkoutpage.checkout_plan_summary import checkout_plan_summary

# Replace with your live Stripe publishable key before going to production.
_STRIPE_PK = os.getenv("STRIPE_PUBLISHABLE_KEY") or ""

_STRIPE_INIT_JS = """
(function () {
  function mountStripe() {
    if (typeof Stripe === 'undefined') {
      setTimeout(mountStripe, 100);
      return;
    }
    var mountEl = document.getElementById('ptg-stripe-card-element');
    if (!mountEl || mountEl.dataset.stripeMounted) return;
    mountEl.dataset.stripeMounted = '1';

    var stripe = Stripe('{pk}');
    var elements = stripe.elements();
    var card = elements.create('card', {
      style: {
        base: {
          fontSize: '14px',
          fontFamily: '"DM Sans", sans-serif',
          color: '#191c1c',
          '::placeholder': { color: '#9e9890' }
        },
        invalid: { color: '#ba1a1a' }
      }
    });
    card.mount('#ptg-stripe-card-element');

    card.on('change', function (event) {
      var errEl = document.getElementById('ptg-stripe-card-errors');
      if (event.error) {
        errEl.textContent = event.error.message;
        errEl.classList.remove('hidden');
      } else {
        errEl.textContent = '';
        errEl.classList.add('hidden');
      }
    });

    // Wire every pay button on this page.
    document.querySelectorAll('[id^="ptg-pay-btn-"]').forEach(function (btn) {
      btn.addEventListener('click', async function () {
        btn.disabled = true;
        btn.textContent = 'Processing…';
        try {
          // Exchange clientSecret from your backend:
          //   POST /api/create-payment-intent  →  { clientSecret }
          var res = await fetch('/api/create-payment-intent', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ plan: btn.id.replace('ptg-pay-btn-', '') })
          });
          var data = await res.json();
          var result = await stripe.confirmCardPayment(data.clientSecret, {
            payment_method: { card: card }
          });
          if (result.error) {
            var errEl = document.getElementById('ptg-stripe-card-errors');
            errEl.textContent = result.error.message;
            errEl.classList.remove('hidden');
            btn.disabled = false;
            btn.textContent = btn.dataset.label || 'Pay';
          } else {
            window.location.href = '/payment-success';
          }
        } catch (e) {
          console.error('Payment error:', e);
          btn.disabled = false;
          btn.textContent = btn.dataset.label || 'Pay';
        }
      });
    });
  }
  mountStripe();
})();
""".replace("{pk}", _STRIPE_PK)


def checkout_page_component(plan: dict) -> rx.Component:
    return rx.box(
        nav_bar(),
        rx.el.main(
            rx.el.a(
                rx.hstack(
                    rx.el.span("arrow_back", class_name="material-symbols-outlined text-base"),
                    rx.text(
                        "BACK TO PRICING",
                        class_name="text-xs font-bold uppercase tracking-widest",
                    ),
                    class_name="flex items-center gap-1.5",
                ),
                href="/pricingpage",
                class_name=(
                    "inline-flex items-center gap-2 text-primary hover:text-primary/70 "
                    "transition-colors no-underline mb-8"
                ),
            ),
            rx.el.div(
                checkout_plan_summary(plan),
                checkout_payment_form(plan),
                class_name="grid md:grid-cols-[2fr_3fr] gap-8 items-start",
            ),
            class_name="max-w-6xl mx-auto px-8 pt-32 pb-20",
        ),
        footer(),
        # Stripe.js — load before the inline init script
        rx.script(src="https://js.stripe.com/v3/"),
        rx.script(_STRIPE_INIT_JS),
        class_name="bg-background text-on-surface min-h-screen",
    )
