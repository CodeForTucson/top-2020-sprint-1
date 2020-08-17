class DisplayMap:
    """ Display maps for Oceanic Affect game.

    This class contains methods to display and update maps for the 
    gameboard of Oceanic Affect.

    Attributes:
        None

    Usage:
        map = DisplayMap()
        map.display_basemap()
    """

    import geopandas as gp

    def display_basemap:
        """ Display the basemap using Geopandas. """
        world = gp.read_file(gp.datasets.get_path('naturalearth_lowres'))
        world.plot()
