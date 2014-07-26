# -*- coding: utf-8 -*-
"""Test docker API."""


import unittest
import docker


class TestDockerClient(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.docker = docker.Client()

    def test_info(self):
        assert self.docker.info().get('KernelVersion', False)
