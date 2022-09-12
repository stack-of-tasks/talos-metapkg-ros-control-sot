 This metapackage allows starting the stack of tasks for TALOS.

[![Pipeline status](https://gitlab.laas.fr/stack-of-tasks/talos-metapkg-ros-control-sot/badges/master/pipeline.svg)](https://gitlab.laas.fr/stack-of-tasks/talos-metapkg-ros-control-sot/commits/master)
[![Coverage report](https://gitlab.laas.fr/stack-of-tasks/talos-metapkg-ros-control-sot/badges/master/coverage.svg?job=doc-coverage)](https://gepettoweb.laas.fr/doc/stack-of-tasks/talos-metapkg-ros-control-sot/master/coverage/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/stack-of-tasks/talos-metapkg-ros-control-sot/master.svg)](https://results.pre-commit.ci/latest/github/stack-of-tasks/talos-metapkg-ros-control-sot)

## Introduction

Two methods to use the SoT with TALOS are possible:

 1.  One based on roscontrol_sot which is using the roscontrol interface. The SoT is then acting as a Controller object interacting with the hardware interface. This is was is used with Gazebo and on the real robot.
 2. One based on geometric-simu. This software is simply a taking the control provided by the SoT and integrates it using a Euler scheme. The order of integration is chosen automatically according to the control law.

## Using roscontrol_sot

### On Gazebo

To start the SoT in position mode control:
    roslaunch roscontrol_sot_talos sot_talos_controller_gazebo.launch

To start the SoT in effort mode control:
	roslaunch roscontrol_sot_talos sot_talos_controller_gazebo_effort.launch

### On the real robot

To start the SoT in position mode control:
``
roslaunch roscontrol_sot_talos sot_talos_controller.launch
``
To start the SoT in effort mode control:
``
roslaunch roscontrol_sot_talos sot_talos_controller_effort.launch
``

## Using geometric_simu

``
roslaunch sot_pyrene_bringup geometric_simu.launch
``



