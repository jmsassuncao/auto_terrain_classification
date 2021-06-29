# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AutoTerrainClassification
                                 A QGIS plugin
 This plugin classifies sentinel 2 satellite imagery into 9 major terrain classes using machine learning algorithms for land use applications.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2020-04-13
        copyright            : (C) 2020 by Jorge Assunção
        email                : jms.assuncao@fct.unl.pt
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'Jorge Assunção'
__date__ = '2020-04-13'
__copyright__ = '(C) 2020 by Jorge Assunção'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load AutoTerrainClassification class from file AutoTerrainClassification.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .auto_terrain_classification import AutoTerrainClassificationPlugin
    return AutoTerrainClassificationPlugin(iface)