import asyncio

import reflex as rx


class StatsState(rx.State):
    """Animated counters for the hero stats strip."""

    active_stations: int = 0
    retailers: int = 0
    satisfaction: int = 0
    gmv_billions: int = 0

    @rx.var
    def stations_display(self) -> str:
        return f"{self.active_stations:,}"

    @rx.var
    def retailers_display(self) -> str:
        return f"{self.retailers:,}+"

    @rx.var
    def satisfaction_display(self) -> str:
        return f"{self.satisfaction}%"

    @rx.var
    def gmv_display(self) -> str:
        return f"{self.gmv_billions}"

    async def animate_stats(self):
        targets = (1247, 3890, 94, 77)
        steps = 48
        for step in range(steps + 1):
            t = step / steps
            ease = 1 - (1 - t) ** 3
            self.active_stations = min(int(round(targets[0] * ease)), targets[0])
            self.retailers = min(int(round(targets[1] * ease)), targets[1])
            self.satisfaction = min(int(round(targets[2] * ease)), targets[2])
            self.gmv_billions = min(int(round(targets[3] * ease)), targets[3])
            yield None
            await asyncio.sleep(0.03)


def _hero_stat_cell(label: str, value_el: rx.Component) -> rx.Component:
    return rx.box(
        value_el,
        rx.text(
            label,
            class_name="text-[10px] md:text-xs uppercase tracking-widest text-white/75 font-medium mt-1 text-center",
        ),
        class_name=(
            "flex flex-col items-center justify-center text-center w-full min-h-full "
            "px-4 sm:px-6 md:px-8 py-2"
        ),
    )


def hero_stats_strip() -> rx.Component:
    return rx.box(
        rx.box(
            rx.grid(
                _hero_stat_cell(
                    "Active Stations",
                    rx.text(
                        StatsState.stations_display,
                        class_name="hero-stat-value font-headline text-3xl md:text-4xl tabular-nums",
                    ),
                ),
                _hero_stat_cell(
                    "Retailers Joined",
                    rx.text(
                        StatsState.retailers_display,
                        class_name="hero-stat-value font-headline text-3xl md:text-4xl tabular-nums",
                    ),
                ),
                _hero_stat_cell(
                    "Satisfaction Rate",
                    rx.text(
                        StatsState.satisfaction_display,
                        class_name="hero-stat-value font-headline text-3xl md:text-4xl tabular-nums",
                    ),
                ),
                rx.box(
                    rx.text(
                        rx.fragment(
                            StatsState.gmv_display,
                            rx.el.span("B", class_name="text-2xl md:text-3xl font-headline ml-0.5 hero-stat-value"),
                            " ",
                            rx.el.span("THB", class_name="text-lg md:text-xl font-sans font-normal hero-stat-value-muted"),
                        ),
                        class_name="hero-stat-value font-headline text-3xl md:text-4xl tabular-nums text-center",
                    ),
                    rx.text(
                        "Total Marketplace GMV",
                        class_name="text-[10px] md:text-xs uppercase tracking-widest text-white/75 font-medium mt-1 text-center",
                    ),
                    class_name=(
                        "flex flex-col items-center justify-center text-center w-full min-h-full "
                        "px-4 sm:px-6 md:px-8 py-2"
                    ),
                ),
                class_name=(
                    "hero-stats-grid max-w-7xl mx-auto "
                    "justify-items-center items-stretch "
                    "px-2 sm:px-4"
                ),
            ),
            class_name="hero-stats-strip-glass w-full",
            on_mount=StatsState.animate_stats,
        ),
        class_name="absolute bottom-0 left-0 right-0 z-20 w-full pointer-events-none",
    )
