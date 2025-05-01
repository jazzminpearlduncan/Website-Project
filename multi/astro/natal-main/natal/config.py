from enum import StrEnum
from pydantic import BaseModel
from types import SimpleNamespace
from typing import Any, Iterator, Literal, Mapping

ThemeType = Literal["light", "dark", "mono", "space"]
LocationType = Literal["earth", "mars", "moon", "station", "deep_space"]


class Dictable(Mapping):
    """
    Protocols for subclasses to behave like a dict.
    """

    def __getitem__(self, key: str):
        return getattr(self, key)

    def __setitem__(self, key: str, value: Any) -> None:
        setattr(self, key, value)

    def __iter__(self) -> Iterator[str]:
        return iter(self.self.model_fields)

    def __len__(self) -> int:
        return len(self.__dict__)

    def update(self, other: Mapping[str, Any] | None = None, **kwargs) -> None:
        """
        Update the attributes with elements from another mapping or from key/value pairs.

        Args:
            other (Mapping[str, Any] | None): A mapping object to update from.
            **kwargs: Additional key/value pairs to update with.
        """
        if other is not None:
            for key, value in other.items():
                setattr(self, key, value)
        for key, value in kwargs.items():
            setattr(self, key, value)


class DotDict(SimpleNamespace, Dictable):
    """
    Extends SimpleNamespace to allow for unpacking and subscript notation access.
    """

    pass


class ModelDict(BaseModel, Dictable):
    """
    Extends BaseModel to allow for unpacking and subscript notation access.
    """

    # override to return keys, otherwise BaseModel.__iter__ returns key value pairs
    def __iter__(self) -> Iterator[str]:
        return iter(self.__dict__)


class HouseSys(StrEnum):
    Placidus = "Pl"
    Koch = "K"
    Equal = "E"
    Campanus = "C"
    Regiomontanus = "R"
    Porphyry = "P"
    Whole_Sign = "W"
    
    Colony_Centric = "CC"
    Space_Adaptive = "S"

class Orb(ModelDict):
    """default orb for natal chart"""

    conjunction: int = 7
    opposition: int = 6
    trine: int = 6
    square: int = 6
    sextile: int = 5
    quincunx: int = 0
    
    quantum_link: int = 3


class Theme(ModelDict):
    """
    Default colors for the chart.
    """

    fire: str = "#ef476f"  # fire, square, Asc
    earth: str = "#ffd166"  # earth, MC
    air: str = "#06d6a0"  # air, trine
    water: str = "#81bce7"  # water, opposition
    
    void: str = "#6c757d"  # void element (space)

    points: str = "#118ab2"  # lunar nodes, sextile

    asteroids: str = "#AA96DA"  # asteroids, quincunx
    colonies: str = "#5a189a"  # space colonies
    stations: str = "#7209b7"  # space stations
    
    positive: str = "#FFC0CB"  # positive
    negative: str = "#AD8B73"  # negative
    others: str = "#FFA500"  # conjunction
    
    transparency: float = 0.1
    foreground: str
    background: str
    dim: str


class LightTheme(Theme):
    """
    Default light colors.
    """

    foreground: str = "#758492"
    background: str = "#FFFDF1"
    dim: str = "#A4BACD"


class DarkTheme(Theme):
    """
    Default dark colors.
    """

    foreground: str = "#F7F3F0"
    background: str = "#343a40"
    dim: str = "#515860"
    
    
class SpaceTheme(Theme):
    """
    Space-themed colors.
    """

    foreground: str = "#d8e2dc"
    background: str = "#080f29"
    dim: str = "#1b263b"
    fire: str = "#ff4d6d"
    earth: str = "#ffb703"
    air: str = "#52b788"
    water: str = "#4cc9f0"
    void: str = "#7209b7"
    colonies: str = "#f72585"
    stations: str = "#4361ee"


class Display(ModelDict):
    """
    Display settings for celestial bodies.
    """

    sun: bool = True
    moon: bool = True
    mercury: bool = True
    venus: bool = True
    mars: bool = True
    jupiter: bool = True
    saturn: bool = True
    uranus: bool = True
    neptune: bool = True
    pluto: bool = True
    
    asc_node: bool = True
    chiron: bool = False
    ceres: bool = False
    pallas: bool = False
    juno: bool = False
    vesta: bool = False
    asc: bool = True
    ic: bool = False
    dsc: bool = False
    mc: bool = True
    
    # Mars moons
    phobos: bool = False
    deimos: bool = False
    
    # Outer planet moons
    europa: bool = False
    ganymede: bool = False
    titan: bool = False
    enceladus: bool = False
    
    # Space colonies
    ceres_colony: bool = False
    proxima_station: bool = False
    alpha_centauri_outpost: bool = False
    kuiper_base: bool = False
    oort_hub: bool = False
    
    # Space horizon point
    space_horizon: bool = False



class Chart(ModelDict):
    """
    Chart configuration settings.
    """

    stroke_width: int = 1
    stroke_opacity: float = 1
    font: str = "sans-serif"
    font_size_fraction: float = 0.55
    inner_min_degree: float = 9
    outer_min_degree: float = 8
    margin_factor: float = 0.04
    ring_thickness_fraction: float = 0.15
    # hard-coded 2.2 and 600 due to the original symbol svg size = 20x20
    scale_adj_factor: float = 600
    pos_adj_factor: float = 2.2

    # Space colonization specific settings
    show_space_grid: bool = False
    colony_influence_factor: float = 0.5
    void_element_weight: float = 0.3
    
class LocationSettings(ModelDict):
    """
    Settings specific to the birth location type.
    """
    
    gravity_factor: float = 1.0  # Earth gravity = 1.0
    day_length_hours: float = 24.0  # Earth day length
    orbital_period_days: float = 365.25  # Earth year
    primary_influence: str = "sun"  # Primary celestial influence
    secondary_influence: str = "moon"  # Secondary celestial influence


class EarthSettings(LocationSettings):
    """Standard Earth settings"""
    pass


class MarsSettings(LocationSettings):
    """Mars colony settings"""
    gravity_factor: float = 0.38
    day_length_hours: float = 24.6
    orbital_period_days: float = 687.0
    primary_influence: str = "sun"
    secondary_influence: str = "mars"


class MoonSettings(LocationSettings):
    """Moon colony settings"""
    gravity_factor: float = 0.166
    day_length_hours: float = 708.0  # Lunar day
    orbital_period_days: float = 27.3
    primary_influence: str = "earth"
    secondary_influence: str = "moon"


class StationSettings(LocationSettings):
    """Space station settings"""
    gravity_factor: float = 0.0  # Zero-G
    day_length_hours: float = 1.5  # 90-minute orbit
    orbital_period_days: float = 0.0625  # Defined by station
    primary_influence: str = "void"
    secondary_influence: str = "nearest_planet"


class DeepSpaceSettings(LocationSettings):
    """Deep space colony settings"""
    gravity_factor: float = 0.0  # Zero-G or artificial
    day_length_hours: float = 24.0  # Artificial day
    orbital_period_days: float = 0.0  # No orbit
    primary_influence: str = "void"
    secondary_influence: str = "nearest_star"

class Config(ModelDict):
    """
    Package configuration model.
    """

    theme_type: ThemeType = "dark"
    house_sys: HouseSys = HouseSys.Placidus
    orb: Orb = Orb()
    light_theme: LightTheme = LightTheme()
    dark_theme: DarkTheme = DarkTheme()
    space_theme: SpaceTheme = SpaceTheme()
    location_type: LocationType = "earth"

    display: Display = Display()
    chart: Chart = Chart()

    earth_settings: EarthSettings = EarthSettings()
    mars_settings: MarsSettings = MarsSettings()
    moon_settings: MoonSettings = MoonSettings()
    station_settings: StationSettings = StationSettings()
    deep_space_settings: DeepSpaceSettings = DeepSpaceSettings()

    @property
    def theme(self) -> Theme:
        """
        Return theme colors based on the theme type.

        Returns:
            Theme: The theme colors.
        """
        match self.theme_type:
            case "light":
                return self.light_theme
            case "dark":
                return self.dark_theme
            case "space":
                return self.space_theme
            case "mono":
                kwargs = {key: "#888888" for key in self.light_theme.model_dump()}
                kwargs["background"] = "#FFFFFF"
                kwargs["transparency"] = 0
                return Theme(**kwargs)
            case _: 
                
    
    @property
    def location_settings(self) -> LocationSettings:
        """
        Return location settings based on the location type.
        
        Returns:
            LocationSettings: The location-specific settings.
        """
        match self.location_type:
            case "earth":
                return self.earth_settings
            case "mars":
                return self.mars_settings
            case "moon":
                return self.moon_settings
            case "station":
                return self.station_settings
            case "deep_space":
                return self.deep_space_settings
