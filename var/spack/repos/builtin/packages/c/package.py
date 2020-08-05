# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

class C(Package):
    """Virtual package for the C language."""
    homepage = 'http://open-std.org/JTC1/SC22/WG14/www/standards'
    virtual = True

    def test(self):
        test_source = os.path.join(self.test_dir, 'data', 'c')

        for test in os.listdir(test_source):
            filepath = os.path.join(test_source, test)
            exe_name = '%s.exe' % test

            cc_exe = os.environ['CC']
            cc_opts = ['-o', exe_name, filepath]
            compiled = self.run_test(cc_exe, options=cc_opts, installed=True)

            if compiled:
                expected = ['Hello world', 'YES!']
                self.run_test(exe_name, expected=expected)