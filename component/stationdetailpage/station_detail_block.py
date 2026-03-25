import reflex as rx

from component.stationdetailpage.station_detail_count_up import count_up_script
from component.stationdetailpage.station_detail_header import station_detail_header
from component.stationdetailpage.station_detail_insights_section import station_insights_section
from component.stationdetailpage.station_detail_kpi_section import station_kpi_section
from component.stationdetailpage.station_detail_spaces_section import station_spaces_section
from component.stationdetailpage.station_detail_spec_table import location_specification_table
from component.stationdetailpage.station_detail_tabs import station_detail_tabs


def station_detail_content(station: dict) -> rx.Component:
    return rx.el.div(
        station_detail_header(station),
        station_detail_tabs(),
        rx.el.div(
            station_kpi_section(station),
            station_insights_section(station),
            station_spaces_section(station),
            location_specification_table(station),
            count_up_script(),
            class_name="space-y-12",
        ),
    )
