"""
Constants and utility functions for the natal package.
"""

from natal.config import DotDict


class Body(DotDict):
    """
    Represents a celestial body in raw data.
    Base class for all members.
    """

    name: str
    symbol: str
    value: int
    color: str


class PlanetMember(Body):
    """
    Represents a planet in raw data.
    """

    ...


class AspectMember(Body):
    """
    Represents an aspect in raw data.
    (conjunction, opposition, trine, square, sextile)
    """

    ...


class ElementMember(Body):
    """
    Represents an element in raw data.
    (fire, earth, air, water)
    """

    ...


class ModalityMember(Body):
    """
    Represents a modality in raw data.
    (cardinal, fixed, mutable)
    """

    ...


class PolarityMember(Body):
    """
    Represents a polarity in raw data.
    (positive, negative)
    """

    ...


class HouseMember(Body):
    """
    Represents a house in raw data.
    """

    ...


class ExtraMember(Body):
    """
    Represents an extra celestial body in raw data.
    (e.g. asteroids, nodes)
    """

    ...


class VertexMember(Body):
    """
    Represents a vertex in raw data (asc, ic, dsc, mc).
    """

    ...


class SignMember(Body):
    """
    Represents a zodiac sign in raw data.
    """

    ruler: str
    detriment: str
    exaltation: str
    fall: str
    classic_ruler: str
    classic_detriment: str
    modality: str
    element: str
    polarity: str


# utils ==================================


def get_member(raw_data: dict, name: str) -> DotDict:
    """
    Get a member from raw data by name.

    Args:
        raw_data (dict): The raw data dictionary.
        name (str): The name of the member.

    Returns:
        DotDict: The member as a DotDict.
    """
    idx = raw_data["name"].index(name)
    member = {key: raw_data[key][idx] for key in raw_data.keys()}
    return DotDict(**member)


def get_members(raw_data: dict) -> list[DotDict]:
    """
    Get all members from raw data.

    Args:
        raw_data (dict): The raw data dictionary.

    Returns:
        list[DotDict]: A list of members as DotDicts.
    """
    return [get_member(raw_data, name) for name in raw_data["name"]]


# Raw Data ===============================

# fmt: off
# Traditional planets plus space colony locations
PLANET_NAMES = ["sun", "moon", "mercury", "venus", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto", "asc_node", 
                "phobos", "deimos", "europa", "ganymede", "titan", "enceladus", "ceres_colony"]

# Additional celestial objects relevant to space colonization
EXTRA_NAMES = ["chiron", "ceres", "pallas", "juno", "vesta", "proxima_station", "alpha_centauri_outpost", "kuiper_base", "oort_hub"]

# Elements including void (space)
ELEMENT_NAMES = ["fire", "earth", "air", "water", "void"]

# Modalities with adaptive for space environments
MODALITY_NAMES = ["cardinal", "fixed", "mutable", "adaptive"]

# Polarities including neutral for deep space
POLARITY_NAMES = ["positive", "negative", "neutral"]

# Traditional zodiac signs plus new deep space signs
SIGN_NAMES = ["aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces", 
              "nova", "cosmos", "vortex", "nebula"]

# Traditional houses plus space-specific houses
HOUSE_NAMES = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", 
               "void_gate", "colony_anchor", "stellar_bridge", "cosmic_well"]

# Traditional aspects plus space-specific aspects
ASPECT_NAMES = ["conjunction", "opposition", "trine", "square", "sextile", "quincunx", "resonance", "quantum_link"]

# Traditional vertices plus space horizon
VERTEX_NAMES = ["asc", "ic", "dsc", "mc", "space_horizon"]
# fmt: on

PLANETS = dict(
    name=PLANET_NAMES,
    symbol="☉☽☿♀♂♃♄♅♆♇☊⊕⊖⊗⊘⊙⊚⊛",
    value=list(range(11)),
    color="fire water air earth fire fire earth air water water points fire earth water air void void colonies".split(),
)

ASPECTS = dict(
    name=ASPECT_NAMES,
    symbol="☌☍△□⚹⚻",
    value=[0, 180, 120, 90, 60, 150],
    color=["others", "water", "air", "fire", "points", "asteroids", "void", "colonies"],
)

ELEMENTS = dict(
    name=ELEMENT_NAMES,
    symbol="🜂🜃🜁🜄",
    value=[0, 1, 2, 3],
    color=["fire", "earth", "air", "water", "void"],
)

MODALITY = dict(
    name=MODALITY_NAMES,
    symbol="⟑⊟𛰣",
    value=[0, 1, 2],
    color=["fire", "earth", "air", "void"],
)

POLARITY = dict(
    name=POLARITY_NAMES,
    symbol=["+", "-", "⊜"],
    value=[1, -1],
    color=["positive", "negative", "neutral"],
)

# Traditional zodiac signs plus space signs
SIGNS = dict(
    name=SIGN_NAMES,
    symbol="♈♉♊♋♌♍♎♏♐♑♒♓⍙⍚⍛⍜",
    value=list(range(1, 17)),
    color=["fire", "earth", "air", "water"] * 4,
    ruler="mars venus mercury moon sun mercury venus pluto jupiter saturn uranus neptune void void void void".split(),
    detriment="venus pluto jupiter saturn uranus neptune mars venus mercury moon sun mercury void void void void".split(),
    exaltation=[
        "sun", "moon", "", "jupiter", "", "mercury", "saturn", "", "", "mars", "", "venus",
        "pluto", "neptune", "uranus", "saturn"
    ],
    fall=[
        "saturn", "", "", "mars", "", "venus", "sun", "moon", "", "jupiter", "", "mercury",
        "mercury", "venus", "mars", "jupiter"
    ],
    classic_ruler="mars venus mercury moon sun mercury venus mars jupiter saturn saturn jupiter void void void void".split(),
    classic_detriment="venus mars jupiter saturn saturn jupiter mars venus mercury moon sun mercury void void void void".split(),
    modality=["cardinal", "fixed", "mutable", "adaptive"] * 4,
    element=["fire", "earth", "air", "water", "void"] * 3 + ["void"],
    polarity=["positive", "negative"] * 6 + ["neutral"] * 4,
)

HOUSES = dict(
    name=HOUSE_NAMES,
    symbol=[str(i) for i in range(1, 13)] + ["⌘", "⌀", "⏣", "⏥"],
    value=list(range(1, 17)),
    color=["fire", "earth", "air", "water"] * 3 + ["void", "colonies", "stations", "void"],
)

EXTRAS = dict(
    name=EXTRA_NAMES,
    symbol="⚷⚳⚴⚵⚶⌖⌗⌘⌙",
    value=[15, 17, 18, 19, 20, 21, 22, 23, 24],
    color=["asteroids"] * 5 + ["stations", "stations", "colonies", "colonies"],
)

VERTICES = dict(
    name=VERTEX_NAMES,
    symbol=["Asc", "IC", "Dsc", "MC"],
    value=[1, 4, 7, 10, 13],
    color=["fire", "water", "air", "earth", "void"],
)

# Derived Members =================================

PLANET_MEMBERS = get_members(PLANETS)
ASPECT_MEMBERS = get_members(ASPECTS)
ELEMENT_MEMBERS = get_members(ELEMENTS)
MODALITY_MEMBERS = get_members(MODALITY)
POLARITY_MEMBERS = get_members(POLARITY)
SIGN_MEMBERS = get_members(SIGNS)
HOUSE_MEMBERS = get_members(HOUSES)
EXTRA_MEMBERS = get_members(EXTRAS)
VERTEX_MEMBERS = get_members(VERTICES)

# Space Colonization Interpretations ==========================

SPACE_SIGN_MEANINGS = {
    "nova": "Represents the creative power of stellar birth and rebirth. Those born under Nova are pioneers, innovators, and often the first to establish new colonies.",
    "cosmos": "Represents the infinite potential of deep space. Those born under Cosmos are visionaries, philosophers, and often serve as spiritual guides for space communities.",
    "vortex": "Represents the dynamic forces of gravitational wells and black holes. Those born under Vortex are transformative leaders who excel in crisis management.",
    "nebula": "Represents the liminal space between creation and dissolution. Those born under Nebula are dreamers, artists, and often bridge different colony cultures."
}

SPACE_HOUSE_MEANINGS = {
    "void_gate": "The house of dimensional thinking and boundary transcendence. Represents one's relationship with the infinite void of space.",
    "colony_anchor": "The house of community roots and cultural preservation. Represents how one contributes to colony sustainability.",
    "stellar_bridge": "The house of intercolony relations and stellar diplomacy. Represents one's role in connecting different space communities.",
    "cosmic_well": "The house of spiritual attunement to the cosmos. Represents one's connection to the universal consciousness."
}

SPACE_ASPECT_MEANINGS = {
    "resonance": "A 45-degree aspect representing harmonic alignment. Indicates areas where quantum entanglement creates synchronistic opportunities.",
    "quantum_link": "A 135-degree aspect representing non-local connection. Indicates abilities that transcend normal space-time limitations."
}

COLONY_INFLUENCE = {
    "mars_colony": "Mars colonies foster strength, resilience, and pioneering spirit. Their inhabitants often display strong independent streaks and innovative problem-solving.",
    "moon_colony": "Lunar colonies nurture intuition, reflection, and emotional intelligence. Their inhabitants often excel at psychological understanding and community building.",
    "europa_colony": "Europa colonies develop adaptability to extreme conditions, innovation, and deep intuition. Their inhabitants often have profound mystical connections to water.",
    "ceres_colony": "Ceres colonies promote resource management, sustainability, and nurturing community. Their inhabitants often excel at agriculture and life support systems.",
    "titan_colony": "Titan colonies cultivate endurance, scientific curiosity, and adaptability to alien environments. Their inhabitants often become leading xenobiologists."
}
