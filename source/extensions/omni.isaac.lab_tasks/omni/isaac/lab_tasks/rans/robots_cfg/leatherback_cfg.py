from omni.isaac.lab.utils import configclass
from dataclasses import MISSING

from omni.isaac.lab_assets.leatherback import LEATHERBACK_CFG  # isort: skip
from omni.isaac.lab.assets import ArticulationCfg
from .robot_core_cfg import RobotCoreCfg

import math


@configclass
class LeatherbackRobotCfg(RobotCoreCfg):
    """Core configuration for a RANS task."""

    robot_cfg: ArticulationCfg = LEATHERBACK_CFG.replace(prim_path="/World/envs/env_.*/Robot")

    throttle_dof_name = [
        "Wheel__Knuckle__Front_Left",
        "Wheel__Knuckle__Front_Right",
        "Wheel__Upright__Rear_Right",
        "Wheel__Upright__Rear_Left",
    ]
    steering_dof_name = [
        "Knuckle__Upright__Front_Right",
        "Knuckle__Upright__Front_Left",
    ]

    rew_action_rate_scale = -0.12
    rew_joint_accel_scale = -2.5e-6

    steering_scale = math.pi / 4.0  # [rad]
    throttle_scale = 20.0  # [rad/s]