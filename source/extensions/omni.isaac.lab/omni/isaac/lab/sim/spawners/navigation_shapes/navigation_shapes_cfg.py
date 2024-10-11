# Copyright (c) 2024, Antoine Richard
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

from collections.abc import Callable
from dataclasses import MISSING

from omni.isaac.lab.sim.spawners import materials
from omni.isaac.lab.sim.spawners.spawner_cfg import RigidObjectSpawnerCfg

# from omni.isaac.lab.sim import schemas
from omni.isaac.lab.utils import configclass

from . import navigation_shapes


@configclass
class NavigationShapeCfg(RigidObjectSpawnerCfg):
    """Configuration parameters for a USD Geometry or Geom prim."""

    visual_material_path: str = "material"
    """Path to the visual material to use for the prim. Defaults to "material".

    If the path is relative, then it will be relative to the prim's path.
    This parameter is ignored if `visual_material` is not None.
    """
    visual_material: materials.VisualMaterialCfg | None = None
    """Visual material properties.

    Note:
        If None, then no visual material will be added.
    """


@configclass
class PinSphereCfg(NavigationShapeCfg):
    """Configuration parameters for a a pin with a sphere prim on top.

    See :meth:`spawn_pin_sphere` for more information.
    """

    func: Callable = navigation_shapes.spawn_pin_with_sphere

    sphere_radius: float = MISSING
    """Radius of the sphere on top of the pin (in m)."""
    pin_radius: float = MISSING
    """Radius of the pin (in m)."""
    pin_length: float = MISSING
    """Length of the pin (in m)."""


@configclass
class DiamondCfg(NavigationShapeCfg):
    """Configuration parameters for a diamond mesh (similar to the sims).

    See :meth:`spawn_diamond` for more information.
    """

    func: Callable = navigation_shapes.spawn_diamond

    diamond_height: float = MISSING
    """Height of the diamond (in m)."""
    diamond_width: float = MISSING
    """Width of the diamond (in m)."""


@configclass
class BiColorDiamondCfg(NavigationShapeCfg):
    """Configuration parameters for a diamond mesh (similar to the sims).

    See :meth:`spawn_diamond` for more information.
    """

    func: Callable = navigation_shapes.spawn_bicolor_diamond

    diamond_height: float = MISSING
    """Height of the diamond (in m)."""
    diamond_width: float = MISSING
    """Width of the diamond (in m)."""
    front_material_path: str = "material_front"
    """Path to the visual material to use for the front of the prim. Defaults to "material".

    If the path is relative, then it will be relative to the prim's path.
    This parameter is ignored if `front_material` is not None.
    """
    front_material: materials.VisualMaterialCfg | None = None
    back_material_path: str = "material_back"
    """Path to the visual material to use for the back of the prim. Defaults to "material".

    If the path is relative, then it will be relative to the prim's path.
    This parameter is ignored if `back_material` is not None.
    """
    """Front material properties."""
    back_material: materials.VisualMaterialCfg | None = None
    """Back material properties."""


@configclass
class PinDiamondCfg(NavigationShapeCfg):
    """Configuration parameters for a pin with a diamond mesh on top (similar to the sims).

    See :meth:`spawn_pin_diamond` for more information.
    """

    func: Callable = navigation_shapes.spawn_pin_with_diamond

    diamond_height: float = MISSING
    """Height of the diamond (in m)."""
    diamond_width: float = MISSING
    """Width of the diamond (in m)."""
    pin_radius: float = MISSING
    """Radius of the pin (in m)."""
    pin_length: float = MISSING
    """Length of the pin (in m)."""


@configclass
class ArrowCfg(NavigationShapeCfg):
    """Configuration parameters for a pin with an arrow mesh on top.

    See :meth:`spawn_pin_arrow` for more information.
    """

    func: Callable = navigation_shapes.spawn_arrow

    arrow_body_radius: float = MISSING
    """Radius of the arrow's body (in m)."""
    arrow_body_length: float = MISSING
    """Length of the arrow's body (in m)."""
    arrow_head_radius: float = MISSING
    """Radius of the arrow's head (in m)."""
    arrow_head_length: float = MISSING
    """Length of the arrow's head (in m)."""


@configclass
class PinArrowCfg(NavigationShapeCfg):
    """Configuration parameters for a pin with an arrow mesh on top.

    See :meth:`spawn_pin_arrow` for more information.
    """

    func: Callable = navigation_shapes.spawn_pin_with_arrow

    arrow_body_radius: float = MISSING
    """Radius of the arrow's body (in m)."""
    arrow_body_length: float = MISSING
    """Length of the arrow's body (in m)."""
    arrow_head_radius: float = MISSING
    """Radius of the arrow's head (in m)."""
    arrow_head_length: float = MISSING
    """Length of the arrow's head (in m)."""
    pin_radius: float = MISSING
    """Radius of the pin (in m)."""
    pin_length: float = MISSING
    """Length of the pin (in m)."""