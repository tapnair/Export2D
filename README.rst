Export2D
========
Export Fusion 360 model faces as PDF or DXF files

.. image:: resources/readMeCover.png

Usage
-----
Select multiple faces and export a single or multiple  DXF or PDF files.

Optionally you can define an offset. This would allow you to compensate for a laser kerf for example.

Note: All DXF objects will be moved to the origin based on the face's orientation.
This may give somewhat unpredictable results.
Modification will be likely necessary.

Installation
------------
1. `Download the latest distribution <https://github.com/tapnair/Export2D/raw/master/dist/__LATEST__/Export2D.zip>`_
2. Unzip the archive to a permanent location on your computer
3. It is important that the directory be named *Export2D*. If you have previously downloaded this or otherwise, make sure the latest version has exactly that directory name.

Requirements
^^^^^^^^^^^^
Credit where credit is due!!!

This sample add-in is built upon the `ezdxf library <https://github.com/mozman/ezdxf/blob/master/docs/source/introduction.rst>`_

Licence
-------
`MIT License`_

.. _MIT License: ./LICENSE

Authors
-------
`Export2D` was written by `Patrick Rainsberry <patrick.rainsberry@autodesk.com>`_.

See more useful `Fusion 360 Utilities`_

.. _Fusion 360 Utilities: https://tapnair.github.io/index.html

