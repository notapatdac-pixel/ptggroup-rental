import reflex as rx

from component.stationdetailpage.station_detail_pro_card import station_pro_insights_card
from component.stationdetailpage.station_detail_traffic_chart import traffic_trend_chart


def station_insights_section(station: dict) -> rx.Component:
    return rx.el.div(
        traffic_trend_chart(station),
        station_pro_insights_card(station),
        class_name="grid grid-cols-1 lg:grid-cols-3 gap-8 lg:items-stretch",
    )
