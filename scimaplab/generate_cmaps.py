import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scimaplab.cmap_scheme import CMapScheme


def hue_rotation(cmap, n_rotations, name_scheme=None):
    """
    Generate a scheme of 'parallel' colormaps by rotating the hue of an existing colormap.
    The hues of the resulting colormaps will have the same relationship as the original colormap.
    This is useful to display similar types of data (e.g. different error metrics) in a way that
    keeps them visually distinguishable but comparable.
    
    Parameters
    ----------
    cmap : str or matplotlib.colors.Colormap object
        The colormap to rotate.
    n_rotations : int
        The number of hue rotations to generate.
    name_scheme : str, optional
        The name of the colormap scheme.
    
    Returns
    -------
    CMapScheme
        A CMapScheme object containing the colormaps.
    """
    

    # If cmap is a string, convert it to an array of RGB colors
    if isinstance(cmap, str):
        cmap = plt.colormaps[cmap]
    name = cmap.name if cmap.name != '' else 'Map'
    
    # Get the RGB values of the colormap
    rgba = np.array(cmap(np.linspace(0, 1, 100)))
    # Generate hue shifts in normalized units (0 to 1)
    hue_shifts = np.linspace(0, 1, n_rotations + 1)

    # Generate a dictionary of colormaps with hue shifts
    cmaps = {}
    for i, hshift in enumerate(hue_shifts[:-1]):
        # Copy the HSV values to avoid modifying the original
        rgb_shifted = _shift_hue_rgb(rgba, hshift)
        # Create a new colormap from the shifted RGB values
        cmaps[f"{name}{i}"] = mpl.colors.LinearSegmentedColormap.from_list(f"{name}{i}", rgb_shifted)

    # Create a CMapScheme object
    name_scheme = name_scheme if name_scheme is not None else f"{name}_HueRot"
    cmaps = CMapScheme(cmaps, name=name_scheme)

    return cmaps


def _shift_hue_rgb(colors, shift):

    # Convert RGB to HSV
    hsv = np.apply_along_axis(mpl.colors.rgb_to_hsv, 1, colors[:,:3])
    # Shift the hue channel
    hsv[:, 0] = (hsv[:, 0] + shift) % 1.0
    # Convert back to RGB
    rgb_shifted = np.apply_along_axis(mpl.colors.hsv_to_rgb, 1, hsv)

    return rgb_shifted

