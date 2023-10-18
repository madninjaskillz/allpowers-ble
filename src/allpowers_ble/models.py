from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=False)
class AllpowersState:
    """State model for Allpowers devices."""

    ac_on: bool = False
    dc_on: bool = False
    usb_on: bool = False
    light_on: bool = False
    f50hz: bool = False
    percent_remain: int = 0
    minutes_remain: int = 0
    watts_import: int = 0
    watts_export: int = 0
