#%% ----- One time install -----
!pip install nglview
!pip install MDAnalysis==2.3.0
!pip install 'ipywidgets<8'   # currently bugged
!jupyter-nbextension enable nglview --py --sys-prefix

#%%
# Also available online: http://nglviewer.org/ngl/
# Demo: https://nglviewer.org/ngl/gallery/index.html
# Git & quick start: https://github.com/nglviewer/nglview
# Doku: http://nglviewer.org/nglview/latest/api.html
# Selection language: https://nglviewer.org/ngl/api/manual/selection-language.html

#%% ----- Import -----
import nglview as ngl
import MDAnalysis as MDA
import pickle

#%% ----- load -----
with open("capped_systems.pkl", "rb") as f:
    capped_systems = pickle.load(f)

i = 1
s = capped_systems[i][1]
start_u = s["start_u"]
end_u = s["end_u"]

#%%
view = ngl.show_mdanalysis(start_u)
view.clear()
view.representations = [
    {
        "type": "ball+stick",
        "params": {
            "sele": "all",
        },
    },
    {
        "type": "spacefill",
        "params": {"sele": "@0", "radiusScale": 0.6, "opacity": 0.6, "color": "orange"},
    },
    {
        "type": "spacefill",
        "params": {"sele": "@1", "radiusScale": 0.6, "opacity": 0.6, "color": "green"},
    },
    {
        "type": "surface",
        "params": {
            "sele": "NME or ACE",
            "radiusScale": 0.3,
            "opacity": 0.3,
            "color": "red",
        },
    },
    {
        "type": "label",
        "params": {"sele": "all", "color": "black", "labelType": "atomindex"},
    },
]
view

#%% ----- Simple representations -----
view = ngl.show_mdanalysis(start_u)
view
#%%
view.clear()
view.add_licorice()
view.clear()
view.add_hyperball()

#%%
view.add_surface("PRO", opacity=0.1, color="green", radiusScale=0.2)
view.add_surface("PRO or NME", opacity=0.1, color="yellow", radiusScale=0.4)
view.add_surface(opacity=0.1, color="orange", radiusScale=0.8)

#%%
view.remove_surface()
view.remove_surface()
view.remove_surface()

#%% ----- other selections -----
# Selection language:
# https://nglviewer.org/ngl/api/manual/selection-language.html

view.add_licorice(
    selection="_H",
    radiusScale=3,
    color="purple",
)
#%% ----- add_representation -----
view.add_representation(
    "spacefill",
    selection="@2,3,4,5,6,7",
    radiusScale=0.6,
)
#%%
view.clear()
view.add_representation("ball+stick")

view.add_representation(
    repr_type="surface",
    selection="PRO",
    radiusScale=0.3,
    opacity=0.3,
    color="grey",
)
view.add_label()

#%% ----- Add other universe -----
comp = view.add_component(end_u, defaultRepresentation=False)

comp.add_spacefill("@0", radiusScale=0.6, opacity=0.5, color="yellow")

#%% ----- Trajectory -----
trr = "vmd_out.trr"
gro = "vmd_out.gro"

u = MDA.Universe(gro, trr)

view = ngl.show_mdanalysis(u)
view

#%% ----- Unitcell -----
view.add_unitcell()

#%% ----- Label -----
view.add_representation("label", color="black", labelType="atomindex")

#%% ----- Highlight -----
view.add_representation(
    "spacefill", selection="@12", radiusScale=0.6, opacity=0.6, color="yellow"
)

view.remove_label()


#%% ----- GUI -----
view = ngl.show_mdanalysis(end_u.atoms, gui=True, style="ngl")
view.clear()
view.representations = [
    {
        "type": "ball+stick",
        "params": {
            "sele": "all",
        },
    },
    {
        "type": "spacefill",
        "params": {"sele": "@0", "radiusScale": 0.6, "opacity": 0.6, "color": "orange"},
    },
    {
        "type": "spacefill",
        "params": {"sele": "@1", "radiusScale": 0.6, "opacity": 0.6, "color": "green"},
    },
]
view

#%% ----- PDB ------
view = ngl.show_pdbid("3pqr")
view

# %%
