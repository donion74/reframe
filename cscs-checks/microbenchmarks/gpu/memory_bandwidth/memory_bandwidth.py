# Copyright 2016-2021 Swiss National Supercomputing Centre (CSCS/ETH Zurich)
# ReFrame Project Developers. See the top-level LICENSE file for details.
#
# SPDX-License-Identifier: BSD-3-Clause

import reframe.utility.sanity as sn
import reframe as rfm

import library.microbenchmarks.gpu.memory_bandwidth as mb
import cscslib.microbenchmarks.gpu.hooks as hooks


@rfm.simple_test
class GpuBandwidthCheck(mb.GpuBandwidthSingle, hooks.SetCompileOpts, hooks.SetGPUsPerNode):
    valid_systems = [
        'daint:gpu', 'dom:gpu', 'arolla:cn', 'tsa:cn',
        'ault:amdv100', 'ault:intelv100', 'ault:amda100', 'ault:amdvega'
    ]
    valid_prog_environs = ['PrgEnv-gnu']

    def __init__(self):
        if self.current_system.name in ['arolla', 'tsa']:
            self.valid_prog_environs = ['PrgEnv-gnu-nompi']

        self.reference = {
            'daint:gpu': {
                'h2d': (11.881, -0.1, None, 'GB/s'),
                'd2h': (12.571, -0.1, None, 'GB/s'),
                'd2d': (499, -0.1, None, 'GB/s')
            },
            'dom:gpu': {
                'h2d': (11.881, -0.1, None, 'GB/s'),
                'd2h': (12.571, -0.1, None, 'GB/s'),
                'd2d': (499, -0.1, None, 'GB/s')
            },
            'tsa:cn': {
                'h2d': (13.000, -0.1, None, 'GB/s'),
                'd2h': (12.416, -0.1, None, 'GB/s'),
                'd2d': (777.000, -0.1, None, 'GB/s')
            },
            'ault:amda100': {
                'h2d': (25.500, -0.1, None, 'GB/s'),
                'd2h': (26.170, -0.1, None, 'GB/s'),
                'd2d': (1322.500, -0.1, None, 'GB/s')
            },
            'ault:amdv100': {
                'h2d': (13.189, -0.1, None, 'GB/s'),
                'd2h': (13.141, -0.1, None, 'GB/s'),
                'd2d': (777.788, -0.1, None, 'GB/s')
            },
            'ault:intelv100': {
                'h2d': (13.183, -0.1, None, 'GB/s'),
                'd2h': (13.411, -0.1, None, 'GB/s'),
                'd2d': (778.200, -0.1, None, 'GB/s')
            },
            'ault:amdvega': {
                'h2d': (14, -0.1, None, 'GB/s'),
                'd2h': (14, -0.1, None, 'GB/s'),
                'd2d': (575.700, -0.1, None, 'GB/s')
            },
        }
        self.tags.update({'diagnostic', 'mch', 'craype'})


@rfm.simple_test
class MultiGpuBandwidthCheck(mb.GpuBandwidthMulti, hooks.SetCompileOpts, hooks.SetGPUsPerNode):
    valid_systems = ['tsa:cn', 'arola:cn',
                     'ault:amdv100', 'ault:intelv100',
                     'ault:amda100', 'ault:amdvega']
    valid_prog_environs = ['PrgEnv-gnu']

    def __init__(self):
        if self.current_system.name in ['arolla', 'tsa']:
            self.valid_prog_environs = ['PrgEnv-gnu-nompi']

        if self.p2p:
            self.reference = {
                'tsa:cn': {
                    'bw':   (172.5, -0.05, None, 'GB/s'),
                },
                'arola:cn': {
                    'bw':   (172.5, -0.05, None, 'GB/s'),
                },
                'ault:amda100': {
                    'bw':   (282.07, -0.1, None, 'GB/s'),
                },
                'ault:amdv100': {
                    'bw':   (5.7, -0.1, None, 'GB/s'),
                },
                'ault:intelv100': {
                    'bw':   (31.0, -0.1, None, 'GB/s'),
                },
                'ault:amdvega': {
                    'bw':   (11.75, -0.1, None, 'GB/s'),
                },
            }
        else:
            self.reference = {
                'tsa:cn': {
                    'bw': (79.6, -0.05, None, 'GB/s'),
                },
                'arola:cn': {
                    'bw': (79.6, -0.05, None, 'GB/s'),
                },
                'ault:amda100': {
                    'bw': (54.13, -0.1, None, 'GB/s'),
                },
                'ault:amdv100': {
                    'bw': (7.5, -0.1, None, 'GB/s'),
                },
                'ault:intelv100': {
                    'bw': (33.6, -0.1, None, 'GB/s'),
                },
                'ault:amdvega': {
                    'bw':   (11.75, -0.1, None, 'GB/s'),
                },
            }

        self.tags.update({'diagnostic', 'mch', 'craype'})
