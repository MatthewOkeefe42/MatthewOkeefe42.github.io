# location_coordinates.py

# Dictionary mapping location names to their coordinates (X, Y) and image URLs
CAMPUS_LOCATIONS = {
    # Academic & Campus Buildings
    "Academic Center": {
        "coords": (43.04079252674532, -71.45128059685808),
        "image_url": "https://campus-images.edu/academic-center.jpg"
    },
    "Admissions Building": {
        "coords": (43.03803555575935, -71.45294119388656),
        "image_url": "https://campus-images.edu/admissions-building.jpg"
    },
    "Arts Center - Gallery": {
        "coords": (43.0410286, -71.4561094),
        "image_url": "https://campus-images.edu/arts-center-gallery.jpg"
    },
    "Library - Room 302": {
        "coords": (43.03895639005512, -71.45193321720352),
        "image_url": "https://campus-images.edu/library.jpg"
    },
    "Science Building - Auditorium": {
        "coords": (0, 0),
        "image_url": "https://campus-images.edu/science-building.jpg"
    },
    "SETA Building": {
        "coords": (43.04158749788569, -71.45294632609152),
        "image_url": "https://campus-images.edu/seta-building.jpg"
    },
    "Technology Center - Lab 105": {
        "coords": (43.0416681153709, -71.45287590196317),
        "image_url": "https://campus-images.edu/technology-center.jpg"
    },
    "Wolak Library Learning Commons - 204": {
        "coords": (43.03895639005512, -71.45193321720352),
        "image_url": "https://campus-images.edu/wolak-library.jpg"
    },
    "Wolak Library Learning Commons - Makerspace": {
        "coords": (43.03895639005512, -71.45193321720352),
        "image_url": "https://campus-images.edu/wolak-makerspace.jpg"
    },
    # Student & Recreational Buildings
    "Campus Center - Room 101": {
        "coords": (0, 0),
        "image_url": "https://campus-images.edu/campus-center.jpg"
    },
    "Dining Center, Banquet Hall, or Virtual": {
        "coords": (43.039651320989094, -71.4518713963412),
        "image_url": "https://campus-images.edu/dining-center.jpg"
    },
    "Gustafson Center": {
        "coords": (43.03785132532583, -71.45302555235365),
        "image_url": "https://campus-images.edu/gustafson-center.jpg"
    },
    "Recreation Center": {
        "coords": (0, 0),
        "image_url": "https://campus-images.edu/recreation-center.jpg"
    },
    "Student Center - Interfaith Prayer Room": {
        "coords": (43.03975643321055, -71.45383296874257),
        "image_url": "https://campus-images.edu/interfaith-prayer-room.jpg"
    },
    "Student Center - Last Chapter Pub": {
        "coords": (43.03957561167002, -71.45406670099402),
        "image_url": "https://campus-images.edu/last-chapter-pub.jpg"
    },
    "Student Union - Conference Room A": {
        "coords": (0, 0),
        "image_url": "https://campus-images.edu/student-union.jpg"
    },
    "Wellness Center": {
        "coords": (43.03953752556915, -71.45401580312473),
        "image_url": "https://campus-images.edu/wellness-center.jpg"
    },
    "William S. and Joan Green Center": {
        "coords": (43.04030555285005, -71.4534730449116),
        "image_url": "https://campus-images.edu/green-center.jpg"
    },
    # Halls (Residential & Administrative)
    "Belknap Hall": {
        "coords": (43.03851473239147, -71.45390096294993),
        "image_url": "https://campus-images.edu/belknap-hall.jpg"
    },
    "Conway Hall": {
        "coords": (43.03985275107877, -71.44551791359837),
        "image_url": "https://campus-images.edu/conway-hall.jpg"
    },
    "Hampton Hall": {
        "coords": (43.04030902199646, -71.44920337165216),
        "image_url": "https://campus-images.edu/hampton-hall.jpg"
    },
    "Kingston Hall": {
        "coords": (43.04075483657583, -71.45470192227421),
        "image_url": "https://campus-images.edu/kingston-hall.jpg"
    },
    "Lincoln Hall": {
        "coords": (43.04041949746448, -71.4455533300823),
        "image_url": "https://campus-images.edu/lincoln-hall.jpg"
    },
    "Monadnock Hall": {
        "coords": (43.03867761612416, -71.45026056189342),
        "image_url": "https://campus-images.edu/monadnock-hall.jpg"
    },
    "New Castle Hall": {
        "coords": (43.03963660223768, -71.45671438655738),
        "image_url": "https://campus-images.edu/new-castle-hall.jpg"
    },
    "Tuckerman Hall": {
        "coords": (43.03929201786349, -71.44876347450277),
        "image_url": "https://campus-images.edu/tuckerman-hall.jpg"
    },
    "Washington Hall": {
        "coords": (43.041887023543666, -71.45382835555607),
        "image_url": "https://campus-images.edu/washington-hall.jpg"
    },
    "Webster Hall": {
        "coords": (43.043790906413065, -71.45105362233738),
        "image_url": "https://campus-images.edu/webster-hall.jpg"
    },
    "Windsor Hall": {
        "coords": (43.04006801938079, -71.44826980719442),
        "image_url": "https://campus-images.edu/windsor-hall.jpg"
    },
    "Ford House": {
        "coords": (43.03838515387062, -71.4531353504291),
        "image_url": "https://campus-images.edu/ford-house.jpg"
    },
    "Morissey House": {
        "coords": (43.03856453180262, -71.45296503017393),
        "image_url": "https://campus-images.edu/morissey-house.jpg"
    },
    "Madison House": {
        "coords": (43.04408598711226, -71.44953617600271),
        "image_url": "https://campus-images.edu/madison-house.jpg"
    },
    # Fields & Courts
    "Athletic Complex": {
        "coords": (43.03843863241567, -71.45573147892655),
        "image_url": "https://campus-images.edu/athletic-complex.jpg"
    },
    "Athletics Field": {
        "coords": (43.0385467, -71.4555932),
        "image_url": "https://campus-images.edu/athletics-field.jpg"
    },
    "Larkin Field": {
        "coords": (43.039143737738094, -71.45532052688897),
        "image_url": "https://campus-images.edu/larkin-field.jpg"
    },
    "Mark A Ouellette Stadium": {
        "coords": (43.038552176666045, -71.4437020635649),
        "image_url": "https://campus-images.edu/ouellette-stadium.jpg"
    },
    "Penman Field": {
        "coords": (43.042497132798, -71.44960525417423),
        "image_url": "https://campus-images.edu/penman-field.jpg"
    },
    "Sand Courts": {
        "coords": (43.04099951380543, -71.44645805049011),
        "image_url": "https://campus-images.edu/sand-courts.jpg"
    },
    "SNHU Tennis Court": {
        "coords": (43.03652259295217, -71.44487682920571),
        "image_url": "https://campus-images.edu/tennis-court.jpg"
    },
    "Softball Field": {
        "coords": (43.04194053934908, -71.44870961729204),
        "image_url": "https://campus-images.edu/softball-field.jpg"
    },
    # Other Campus Locations
    "Campus Green": {
        "coords": (43.0401567, -71.4540823),
        "image_url": "https://campus-images.edu/campus-green.jpg"
    },
    "Public Safety": {
        "coords": (43.04101727243464, -71.45217641596051),
        "image_url": "https://campus-images.edu/public-safety.jpg"
    }
}

def normalize_location(location):
    """
    Normalize location strings to improve matching.
    - Converts to lowercase
    - Replaces various separators with spaces
    - Removes extra spaces
    """
    location = location.lower()
    # Replace various separators with spaces
    for char in ['-', '_', ',', ';', ':', '/']: 
        location = location.replace(char, ' ')
    # Remove double spaces
    while '  ' in location:
        location = location.replace('  ', ' ')
    return location.strip()

def get_location_info(location_name):
    """
    Retrieve coordinates and image URL for a given location name.
    Uses a flexible matching approach to handle variations in naming.
    Returns tuple of (x_coord, y_coord, image_url) if found, or (None, None, None) if not found.
    """
    if not location_name:
        return (None, None, None)
    
    # Try exact match first
    if location_name in CAMPUS_LOCATIONS:
        location_data = CAMPUS_LOCATIONS[location_name]
        return (location_data["coords"][0], location_data["coords"][1], location_data["image_url"])
    
    # Normalize the input location name
    normalized_location = normalize_location(location_name)
    
    # Create normalized versions of all dictionary keys
    normalized_locations = {normalize_location(key): {"coords": value["coords"], "image_url": value["image_url"]} 
                           for key, value in CAMPUS_LOCATIONS.items()}
    
    # Check for exact normalized match
    if normalized_location in normalized_locations:
        location_data = normalized_locations[normalized_location]
        return (location_data["coords"][0], location_data["coords"][1], location_data["image_url"])
    
    # Try to match key parts of the location (building names, etc.)
    location_parts = normalized_location.split()
    
    # First look for multi-word matches starting from the longest possible match
    best_match = None
    best_match_words = 0
    
    for known_location, location_data in normalized_locations.items():
        known_parts = known_location.split()
        
        # Check if any subset of words from input matches known location
        for i in range(len(location_parts)):
            for j in range(i+1, len(location_parts)+1):
                test_phrase = " ".join(location_parts[i:j])
                if test_phrase in known_location and j-i > best_match_words:
                    best_match = location_data
                    best_match_words = j-i
        
        # Check if any subset of words from known location matches input
        for i in range(len(known_parts)):
            for j in range(i+1, len(known_parts)+1):
                test_phrase = " ".join(known_parts[i:j])
                if test_phrase in normalized_location and j-i > best_match_words:
                    best_match = location_data
                    best_match_words = j-i
    
    if best_match:
        return (best_match["coords"][0], best_match["coords"][1], best_match["image_url"])
    
    # As a last resort, look for individual key words
    important_words = ["center", "hall", "building", "library", "field", "room", "lab", "house", "court"]
    for word in important_words:
        if word in normalized_location:
            for known_loc, location_data in normalized_locations.items():
                if word in known_loc:
                    return (location_data["coords"][0], location_data["coords"][1], location_data["image_url"])
    
    # Return None if no match found
    return (None, None, None)

# For backward compatibility
def get_coordinates(location_name):
    """Legacy function that returns just the coordinates"""
    x_coord, y_coord, _ = get_location_info(location_name)
    return (x_coord, y_coord)

# Test function - uncomment to debug
def test_location_matching():
    """Test the location matching with various input formats"""
    test_locations = [
        "Student Center- Interfaith Prayer Room",
        "Library- Room 302",
        "Technology Center- Lab 105",
        "Arts Center- Gallery",
        "Wolak Library Learning Commons",
        "Kingston Hall - Room 204"
    ]
    
    print("Testing location matching:")
    for loc in test_locations:
        x_coord, y_coord, image_url = get_location_info(loc)
        print(f"{loc} => Coords: ({x_coord}, {y_coord}), Image: {image_url}")

# Uncomment to run tests
# test_location_matching()