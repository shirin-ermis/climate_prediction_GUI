def get_albedo(cloud_cover):
    """Function calculates albedo of the planet
    using cloud cover
    
    Assumptions:
    - open ocean underneath clouds only
    - cloud albedo of 75% (marine stratocumulus, 
        source: https://en.wikipedia.org/wiki/Cloud_albedo)
    - open ocean albedo 6% (source: https://en.wikipedia.org/wiki/Albedo)"""

    alpha = cloud_cover * 0.75 + (1 - cloud_cover) * 0.06
    return alpha
