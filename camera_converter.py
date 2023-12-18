import json
import os
import re
import argparse
from os import path
import time

import numpy as np

# C:\Users\andre\Downloads\base.ingp


def UEMoveTransform(m, x, y, z):
    m[0][3] = m[0][3]+x
    m[1][3] = m[1][3]+y
    m[2][3] = m[2][3]+z


def UEScaleTransform(m, s):
    m[0][3] = m[0][3]*s
    m[1][3] = m[1][3]*s
    m[2][3] = m[2][3]*s


def UE_to_iNGP(m):
    m[0][0], m[0][1], m[0][2] = m[0][1], m[0][2], -m[0][0]
    m[1][0], m[1][1], m[1][2] = m[1][1], m[1][2], -m[1][0]
    m[2][0], m[2][1], m[2][2] = m[2][1], m[2][2], -m[2][0]
    m[0][:] = [-m[0][0], -m[0][1], -m[0][2], -m[0][3]]


def main():

    modifiedOn = -1
    transforms_calc_path = os.path.join('build', "transform.json")

    if not path.exists(transforms_calc_path):
        print(f"Failed to find file: {transforms_calc_path}")
        return
    try:
        while (True):
            time.sleep(0.2)
            modified = os.path.getmtime(transforms_calc_path)
            if modified != modifiedOn:
                modifiedOn = modified
                with open(transforms_calc_path, 'r') as f:
                    transforms = json.load(f)

                    m = transforms["transform_matrix"]
                    print(m)
                    UEMoveTransform(m, -0.25, 0, 0)
                    print(m)
                    UEScaleTransform(m, 32)
                    print(m)
                    UE_to_iNGP(m)
                    print(m)
                transforms["transform_matrix"] = m
                camera_transform_path = os.path.join(
                    'build', "camera_transform.json")
                with open(camera_transform_path, 'w') as f:
                    f.write(json.dumps(transforms, indent=2))
    except EnvironmentError:  # parent of IOError, OSError *and* WindowsError where available
        print('error')


if __name__ == "__main__":

    main()
