# 2019_STMhero

## Overview

This projec is mostly based on the idea of Guitar Hero and is based on two parts:
- the guitar itself along with its software
- desktop Python-based application

### The hardware

We used photoresistors to create an imitation of strings and buttons to trigger a proper line in the destop app. Dragging was based on an accelerometer. We used:

- STM32CubeMX
- SystemWorkbench for STM32 environment
- STM32F407 board
- PyCharm

### How to run

To run Desktop Application you need to install:
- python 3.x
- pygame library
- pyserial library

Then proceed as in a standard Python compilation.

### Attributions

- Virtual COM Port: https://github.com/xenovacivus/STM32DiscoveryVCP
- Python pygame library: https://www.pygame.org
- Python pyserial library: https://pythonhosted.org/pyserial/

## Credits

The project was conducted during the Microprocessor Lab course held by the Institute of Control and Information Engineering, Poznan University of Technology.

Contractors: Konrad Kęciński, Karol Kobaka

Supervisor: Tomasz Mańkowski
