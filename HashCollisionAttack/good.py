#!/usr/bin/env python3
# coding: iso-8859-1

MSG = bytes(r"""
                                                              ���		F��m 2��x�}q���H.�8�*&
��#�p�8�k�edÙ���'�X�~pO��D��;��r�1
U�֩�x���1B_�����V[�K�̚_Y/�D�*"��#[�Wb�^-��L.
""", "iso-8859-1")
from hashlib import sha256
if "1B" in MSG.decode("iso-8859-1"):
    print("I come in peace.")
else:
    print("Prepare to be destroyed!")
