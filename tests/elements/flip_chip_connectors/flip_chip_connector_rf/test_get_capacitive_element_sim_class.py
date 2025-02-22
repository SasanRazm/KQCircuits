# This code is part of KQCircuits
# Copyright (C) 2023 IQM Finland Oy
#
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program. If not, see
# https://www.gnu.org/licenses/gpl-3.0.html.
#
# The software distribution should follow IQM trademark policy for open-source software
# (meetiqm.com/developers/osstmpolicy). IQM welcomes contributions to the code. Please see our contribution agreements
# for individuals (meetiqm.com/developers/clas/individual) and organizations (meetiqm.com/developers/clas/organization).

import pytest
from kqcircuits.elements.flip_chip_connectors.flip_chip_connector_rf import FlipChipConnectorRf


def test_can_create(get_simulation):
    get_simulation(FlipChipConnectorRf, face_stack=['1t1', '2b1'])


def test_ansys_export_produces_output_files(perform_test_ansys_export_produces_output_files):
    perform_test_ansys_export_produces_output_files(FlipChipConnectorRf, face_stack=['1t1', '2b1'])


@pytest.mark.skip("Sonnet export test currently breaks for multiface simulations")
def test_sonnet_export_produces_output_files(perform_test_sonnet_export_produces_output_files):
    perform_test_sonnet_export_produces_output_files(FlipChipConnectorRf, face_stack=['1t1', '2b1'])
