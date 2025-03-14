
import numpy as np
import matplotlib.pyplot as plt


class CMapScheme():
    """
    A class to store a collection of colormaps.

    Parameters
    ----------
    cmap_dict : dictionary of {name: cmap}
        A dictionary of colormaps to store.
    name : str, optional
        The name of the scheme.
    
    Attributes
    ----------
    cmaps : dictionary of {name: cmap}
        A dictionary of colormaps.
    name : str
        The name of the scheme.
    n_maps : int
        The number of colormaps in the scheme.

    Methods
    -------
    display()
        Display the colormaps in the scheme.
    """
    def __init__(self, cmap_dict, name=None):
        self.cmaps = cmap_dict
        self.name = name
        self.cmap_names = list(cmap_dict.keys())
        self.n_maps = len(cmap_dict)

    def __getitem__(self, key):
        """Allow indexing by integer or colormap name (string)."""

        if not isinstance(key, (int, str)):
            raise TypeError("Key must be an integer or string.")

        if isinstance(key, int):
            # Allow negative indices too.
            try:
                key = self.cmap_names[key]
            except IndexError:
                raise IndexError("Index out of range.")

        elif key not in self.cmap_names:
            raise KeyError(f"Colormap '{key}' not found.")
        
        return self.cmaps[key]
    


    def display(self):
        _display_scheme(self.cmaps)



def _display_scheme(cmap_scheme):
    """
    Display a list of colormaps in a single figure.
    
    Parameters
    ----------
    cmap_scheme : dictionary of {name: cmap}
        A dictionary of colormaps to display.
    
    Returns
    -------
    None
    """

    n = len(cmap_scheme)
    fig, axes = plt.subplots(n, 1, figsize=(6, n * 1))
    # Create a horizontal gradient image
    gradient = np.linspace(0, 1, 256).reshape(1, -1)
    
    for ax, (name, cmap) in zip(np.atleast_1d(axes), cmap_scheme.items()):
        ax.imshow(gradient, aspect='auto', cmap=cmap)
        ax.set_axis_off()
        ax.set_title(name, fontsize=18)
    
    plt.tight_layout()
    plt.show()
    return None

