# Challenge #37 - Beginner
# Image Search (case-insensitive)
# Objective: Practice list filtering, string containment, and case normalization.

"""
Given a list of image names and a search term,
return all image names that contain the term (case-insensitive),
keeping their original order.
"""

def image_search(images, term):
    """
    Return all image names that contain the given search term (case-insensitive).
    """
    term = term.lower()  # normalize search term
    
    result = []
    for img in images:
        if term in img.lower():  # case-insensitive containment check
            result.append(img)
    return result


# Example test
images = ["Sunset.png", "ocean_view.jpg", "CityNight.PNG", "sunrise-photo.jpeg"]
print(image_search(images, "sun"))
