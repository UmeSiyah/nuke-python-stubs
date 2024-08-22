# Copyright (c) 2022 The Foundry Visionmongers Ltd. All Rights Reserved.

import hiero.ui
from hiero.ui.FnUIProperty import UIPropertyFactory
from hiero.ui.FnTaskUIFormLayout import TaskUIFormLayout

from .FnOTIOExportTask import OTIOExportTask, OTIOExportPreset


class OTIOExportUI(hiero.ui.TaskUIBase):
    """ UI for OTIO file export.
    Currently empty until we need to add some parameters to the export.
    """

    def __init__(self, preset):
        hiero.ui.TaskUIBase.__init__(self, OTIOExportTask, preset, 'OTIO Exporter')

    def populateUI(self, widget, exportTemplate):
        formLayout = TaskUIFormLayout()
        widget.layout().addLayout(formLayout)

        # Link to rendered media
        key, value, label = 'writeCompRenderPaths', True, 'Replace comp with rendered media'
        tooltip = 'Turning on will link the clip to the media. Turning it off will link the clip to the .nk'
        propertyWidget = UIPropertyFactory.create(type(value), key=key, value=value, dictionary=self._preset.properties(),
                                                  label=label, tooltip=tooltip)
        formLayout.addRow(label, propertyWidget)

        # Export effects
        key, value, label = 'includeEffects', True, 'Include Effects'
        tooltip = 'Enable to include soft effects in the exported OTIO file'
        propertyWidget = UIPropertyFactory.create(type(value), key=key, value=value, dictionary=self._preset.properties(),
                                                  label=label, tooltip=tooltip)
        formLayout.addRow(label, propertyWidget)


hiero.ui.taskUIRegistry.registerTaskUI(OTIOExportPreset, OTIOExportUI)
