#!/usr/bin/env python
# Copyright 2017 Opera Software AS. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""This script generates a clang tarball to be sent to the nodes in an icecc
cluster when doing a distributed build of chromium. The tarball is created from
the clang compiler in the chromium checkout.

The generated tarball is stored in src/icecc-tarball/clang.tar.gz, which is
expected by the icecc-ninja script. Running this scripts deletes the old tarball
before generating the new one.

To make sure the tarball is up-to-date with the current checkout, add this
custom hook to the .gclient file:

  "custom_hooks": [ {"pattern": ".", "action": ["icecc-create-env.py"] } ]

That will force a regeneration of the tarball when running "gclient runhooks".
"""

import os
import shutil
import subprocess

clang_path = os.path.join(os.getcwd(), "src", "third_party", "llvm-build", "Release+Asserts", "bin", "clang")
tarball_dir = os.path.join(os.getcwd(), "src", "icecc-tarball")

# Remove old tarball and re-create the directory.

if os.path.exists(tarball_dir):
    shutil.rmtree(tarball_dir)
os.makedirs(tarball_dir)

# Generate tarball.

subprocess.check_output(["icecc-create-env", "--clang", clang_path], cwd=tarball_dir);

# Change name of generated tarball to something well known.

tarball_generated = os.path.join(tarball_dir, os.listdir(tarball_dir)[0])
tarball_final = os.path.join(tarball_dir, "clang.tar.gz")

os.rename(tarball_generated, tarball_final)
