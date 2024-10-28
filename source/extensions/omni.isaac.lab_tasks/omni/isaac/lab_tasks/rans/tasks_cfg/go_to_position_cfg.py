from omni.isaac.lab.utils import configclass
from dataclasses import MISSING

from .task_core_cfg import TaskCoreCfg

import math


@configclass
class GoToPositionCfg(TaskCoreCfg):
    """Configuration for the GoToPosition task."""

    # Initial conditions
    spawn_min_dist: float = 0.5
    """Minimal distance between the spawn pose and the target pose in m. Defaults to 0.5 m."""
    spawn_max_dist: float = 5.0
    """Maximal distance between the spawn pose and the target pose in m. Defaults to 5.0 m."""
    spawn_min_heading_dist: float = 0.0
    """Minimal angle between the spawn orientation and the angle required to be looking at the target in rad.
    Defaults to 0.0 rad."""
    spawn_max_heading_dist: float = math.pi
    """Maximal angle between the spawn orientation and the angle required to be looking at the target in rad.
    Defaults to pi rad."""
    spawn_min_lin_vel: float = 0.0
    """Minimal linear velocity at spawn pose in m/s. Defaults to 0.0 m/s."""
    spawn_max_lin_vel: float = 0.0
    """Maximal linear velocity at spawn pose in m/s. Defaults to 0.0 m/s."""
    spawn_min_ang_vel: float = 0.0
    """Minimal angular velocity at spawn in rad/s. Defaults to 0.0 rad/s."""
    spawn_max_ang_vel: float = 0.0
    """Maximal angular velocity at spawn in rad/s. Defaults to 0.0 rad/s."""

    # Goal spawn
    goal_max_dist_from_origin: float = 0.0
    """Maximal distance from the origin of the environment. Defaults to 0.0."""

    # Tolerance
    position_tolerance: float = 0.01
    """Tolerance for the position of the robot. Defaults to 1cm."""
    maximum_robot_distance: float = 10.0
    """Maximal distance between the robot and the target pose. Defaults to 10 m."""
    reset_after_n_steps_in_tolerance: int = 100
    """Reset the environment after n steps in tolerance. Defaults to 100 steps."""

    # Reward Would be good to have a config for each reward type
    position_exponential_reward_coeff: float = 0.25
    linear_velocity_min_value: float = 0.5
    linear_velocity_max_value: float = 2.0
    angular_velocity_min_value: float = 0.5
    angular_velocity_max_value: float = 20.0
    boundary_exponential_reward_coeff: float = 1.0
    position_weight: float = 1.0
    linear_velocity_weight: float = -0.05
    angular_velocity_weight: float = -0.05
    boundary_weight: float = -10.0
