# Copyright (c) 2009 The Foundry Visionmongers Ltd.  All Rights Reserved.

import os
import enum
import os.path
from enum import IntEnum

import nukescripts
import nuke_internal as nuke

# Define the tool menus. This file is loaded by menu.py.


def setup_toolbars():
    # This is not currently used but when we support a text-only mode we'll need it.
    # size = nuke.numvalue("preferences.toolbarTextSize")

    # Use the following options to set the shortcut context in the call to menu addCommand.
    # Setting the shortcut context to a widget will mean the shortcut will only be triggered
    # if that widget (or it's children) has focus. If no shortcut context is specified the
    # default context is window context i.e. it can be triggered from anywhere in the window.
    # The enum is defined in nk_menu_python_add_item in PythonObject.cpp
    windowContext = 0
    applicationContext = 1
    dagContext = 2

    # Enumerate possible menu item tags. It defaults to MenuItemTag.NoTag, if not specified.
    @enum.unique
    class MenuItemTag(IntEnum):
        NoTag = 0
        Beta = 1
        Classic = 2

    # Enumerate possible menu item tag targets - widgets where the tag should be present.
    # It defaults to MenuItemTagTargetFlag.All, if not specified.
    @enum.unique
    class MenuItemTagTargetFlag(IntEnum):
        Unknown = 0
        ToolbarMenu = 1
        TabMenu = 2
        ContextMenu = 4
        All = 7

    # Get the top-level toolbar
    toolbar = nuke.menu('Nodes')
    assist = nuke.env['assist']

    # The "Image" menu
    m = toolbar.addMenu('Image', 'ToolbarImage.png')
    m.addCommand('Read', 'with nuke.lastHitGroup():\n  nukescripts.create_read()',
                 'r', icon='Read.png', shortcutContext=dagContext)
    m.addCommand('Write', "nukescripts.createNodeLocal(\"Write\")",
                 'w', icon='Write.png', shortcutContext=dagContext)
    m.addCommand('Profile', "nukescripts.createNodeLocal(\"Profile\")",
                 icon='Write.png', shortcutContext=dagContext)
    if not assist:
        m.addCommand('UDIM import', 'with nuke.lastHitGroup():\n  nukescripts.udim_import()',
                     'u', icon='Read.png', shortcutContext=dagContext)
    m.addCommand('UnrealReader', "nukescripts.createNodeLocal(\"UnrealReader\")", icon='Read.png')
    m.addCommand('Constant', "nukescripts.createNodeLocal(\"Constant\")", icon='Constant.png')
    m.addCommand('CheckerBoard', "nukescripts.createNodeLocal(\"CheckerBoard2\")",
                 icon='CheckerBoard.png')
    m.addCommand('ColorBars', "nukescripts.createNodeLocal(\"ColorBars\")", icon='ColorBars.png')
    m.addCommand('ColorWheel', "nukescripts.createNodeLocal(\"ColorWheel\")", icon='ColorWheel.png')
    if not assist:
        m.addCommand(
            'CurveTool', 'with nuke.lastHitGroup():\n  nukescripts.createCurveTool()', icon='CurveTool.png')
    m.addCommand('Viewer', "nukescripts.createNodeLocal(\"Viewer\")", icon='Viewer.png')
    # m.addCommand("Proxy", "nuke.knob(\"root.proxy\", \"!root.proxy\")", icon="proxyfullres.png")

    # The "Draw" menu
    m = toolbar.addMenu('Draw', 'ToolbarDraw.png')
    m.addCommand('Roto', '''nukescripts.createNodeLocal("Roto")''',
                 'o', icon='Roto.png', shortcutContext=dagContext)
    m.addCommand('RotoPaint', "nukescripts.createNodeLocal(\"RotoPaint\")",
                 'p', icon='RotoPaint.png', shortcutContext=dagContext)

    m.addCommand('@;RotoBranch', "nukescripts.createNodeLocal(\"Roto\")",
                 '+o', shortcutContext=dagContext)
    m.addCommand('@;RotoPaintBranch', "nukescripts.createNodeLocal(\"RotoPaint\")",
                 '+p', shortcutContext=dagContext)

    m.addCommand('Dither', "nukescripts.createNodeLocal(\"Dither\")", icon='Dither.png')
    m.addCommand('DustBust', "nukescripts.createNodeLocal(\"DustBust\")", icon='DustBust.png')
    m.addCommand('Grain', "nukescripts.createNodeLocal(\"Grain2\")", icon='Grain.png')
    m.addCommand('ScannedGrain', "nukescripts.createNodeLocal(\"ScannedGrain\")",
                 icon='ScannedGrain.png')
    m.addCommand('Glint', "nukescripts.createNodeLocal(\"Glint\")", icon='Glint.png')
    m.addCommand('Grid', "nukescripts.createNodeLocal(\"Grid\")", icon='Grid.png')
    m.addCommand('Flare', "nukescripts.createNodeLocal(\"Flare\")", icon='Flare.png')
    m.addCommand('LightWrap', "nukescripts.createNodeLocal(\"LightWrap\")", icon='LightWrap.png')
    m.addCommand('MarkerRemoval', "nukescripts.createNodeLocal(\"MarkerRemoval\")",
                 icon='MarkerRemoval.png')
    m.addCommand('Noise', "nukescripts.createNodeLocal(\"Noise\")", icon='Noise.png')
    m.addCommand('Radial', "nukescripts.createNodeLocal(\"Radial\")", icon='Radial.png')
    m.addCommand('Ramp', "nukescripts.createNodeLocal(\"Ramp\")", icon='Ramp.png')
    m.addCommand('Rectangle', "nukescripts.createNodeLocal(\"Rectangle\")", icon='Rectangle.png')
    m.addCommand('Sparkles', "nukescripts.createNodeLocal(\"Sparkles\")", icon='Sparkles.png')
    m.addCommand('Text', "nukescripts.createNodeLocal(\"Text2\")", icon='Text.png')

    m = toolbar.addMenu('Time', 'ToolbarTime.png')
    m.addCommand('Add 3:2 pulldown', "nukescripts.createNodeLocal(\"add32p\")", icon='Add32.png')
    m.addCommand('Remove 3:2 pulldown',
                 "nukescripts.createNodeLocal(\"remove32p\")", icon='Remove32.png')
    m.addCommand('AppendClip', "nukescripts.createNodeLocal(\"AppendClip\")", icon='AppendClip.png')
    m.addCommand('FrameBlend', "nukescripts.createNodeLocal(\"FrameBlend\")", icon='FrameBlend.png')
    m.addCommand('FrameHold', "nukescripts.createNodeLocal(\"FrameHold\")", icon='FrameHold.png')
    m.addCommand('FrameRange', "nukescripts.createNodeLocal(\"FrameRange\")", icon='FrameRange.png')
    if not assist:
        m.addCommand(
            'Kronos', 'with nuke.lastHitGroup():\n  nukescripts.createKronos()', icon='Oflow.png')
    m.addCommand('OFlow', 'with nuke.lastHitGroup():\n  nukescripts.createOFlow()', icon='Oflow.png')
    m.addCommand('Retime', "nukescripts.createNodeLocal(\"Retime\")", icon='Retime.png')
    m.addCommand('TemporalMedian', "nukescripts.createNodeLocal(\"TemporalMedian\")",
                 icon='TemporalMedian.png')
    m.addCommand('TimeBlur', "nukescripts.createNodeLocal(\"TimeBlur\")", icon='TimeBlur.png')
    m.addCommand('NoTimeBlur', "nukescripts.createNodeLocal(\"NoTimeBlur\")", icon='NoTimeBlur.png')
    m.addCommand('TimeEcho', "nukescripts.createNodeLocal(\"TimeEcho\")", icon='TimeEcho.png')
    m.addCommand('TimeOffset', "nukescripts.createNodeLocal(\"TimeOffset\")", icon='TimeOffset.png')

    if not assist:
        m.addCommand(
            'TimeWarp', 'with nuke.lastHitGroup():\n  nukescripts.create_time_warp()', icon='TimeWarp.png')
    m.addCommand('TimeClip', "nukescripts.createNodeLocal(\"TimeClip\")")

    m.addCommand('SmartVector', "nukescripts.createNodeLocal(\"SmartVector\")",
                 icon='SmartVector.png')
    m.addCommand('VectorToMotion', "nukescripts.createNodeLocal(\"VectorToMotion\")",
                 icon='VectorToMotion.png')
    m.addCommand('VectorGenerator', "nukescripts.createNodeLocal(\"VectorGenerator\")")

    # The "Channel" menu
    m = toolbar.addMenu('Channel', 'ToolbarChannel.png')
    m.addCommand('Shuffle', "nukescripts.createNodeLocal(\"Shuffle2\")", icon='Shuffle.png')
    m.addCommand('Copy', "nukescripts.createNodeLocal(\"Copy\")",
                 'k', icon='CopyNode.png', shortcutContext=dagContext)
    m.addCommand('@;CopyBranch', "nukescripts.createNodeLocal(\"Copy\")",
                 '+k', shortcutContext=dagContext)
    m.addCommand('ChannelMerge', "nukescripts.createNodeLocal(\"ChannelMerge\")",
                 icon='ChannelMerge.png')
    m.addCommand('Add', "nukescripts.createNodeLocal(\"AddChannels\")", icon='Add.png')
    m.addCommand('Remove', "nukescripts.createNodeLocal(\"Remove\")", icon='Remove.png')

    # The "Color" menu
    m = toolbar.addMenu('Color', 'ToolbarColor.png')

    n = m.addMenu('Math', 'ColorMath.png')
    n.addCommand('Add', "nukescripts.createNodeLocal(\"Add\")", icon='ColorAdd.png')
    n.addCommand('Multiply', "nukescripts.createNodeLocal(\"Multiply\")", icon='ColorMult.png')
    n.addCommand('Gamma', "nukescripts.createNodeLocal(\"Gamma\")", icon='ColorGamma.png')
    n.addCommand('ClipTest', "nukescripts.createNodeLocal(\"ClipTest\")", icon='ClipTest.png')
    n.addCommand('ColorMatrix', "nukescripts.createNodeLocal(\"ColorMatrix\")",
                 icon='ColorMatrix.png')
    n.addCommand('Expression', "nukescripts.createNodeLocal(\"Expression\")", icon='Expression.png')

    n = m.addMenu('OCIO', 'OCIO.png')
    n.addCommand('OCIO CDLTransform',
                 "nukescripts.createNodeLocal(\"OCIOCDLTransform\")", icon='OCIO.png')
    n.addCommand('OCIO ColorSpace', "nukescripts.createNodeLocal(\"OCIOColorSpace\")", icon='OCIO.png')
    n.addCommand('OCIO Display', "nukescripts.createNodeLocal(\"OCIODisplay\")", icon='OCIO.png')
    n.addCommand('OCIO FileTransform',
                 "nukescripts.createNodeLocal(\"OCIOFileTransform\")", icon='OCIO.png')
    n.addCommand('OCIO LogConvert', "nukescripts.createNodeLocal(\"OCIOLogConvert\")", icon='OCIO.png')
    n.addCommand('OCIO LookTransform',
                 "nukescripts.createNodeLocal(\"OCIOLookTransform\")", icon='OCIO.png')
    n.addCommand('OCIO NamedTransform', "nukescripts.createNodeLocal(\"OCIONamedTransform\")",
                 icon='OCIO.png', nodeClass='OCIONamedTransform')

    n = m.addMenu('3D LUT', 'Toolbar3DLUT.png')
    n.addCommand('CMSTestPattern', "nukescripts.createNodeLocal(\"CMSTestPattern\")",
                 icon='CMSTestPattern.png')
    n.addCommand('GenerateLUT', "nukescripts.createNodeLocal(\"GenerateLUT\")",
                 icon='GenerateLUT.png')
    n.addCommand('Vectorfield (Apply 3D LUT)',
                 "nukescripts.createNodeLocal(\"Vectorfield\")", icon='Vectorfield.png')

    m.addCommand('Clamp', "nukescripts.createNodeLocal(\"Clamp\")", icon='Clamp.png')
    m.addCommand('ColorLookup', "nukescripts.createNodeLocal(\"ColorLookup\")",
                 icon='ColorLookup.png')
    m.addCommand('Colorspace', "nukescripts.createNodeLocal(\"Colorspace\")", icon='ColorSpace.png')
    m.addCommand('ColorTransfer', "nukescripts.createNodeLocal(\"ColorTransfer\")",
                 icon='ColorTransfer.png')
    m.addCommand('ColorCorrect', "nukescripts.createNodeLocal(\"ColorCorrect\")",
                 'c', icon='ColorCorrect.png', shortcutContext=dagContext)
    m.addCommand('@;ColorCorrectBranch', "nukescripts.createNodeLocal(\"ColorCorrect\")", '+c')
    m.addCommand('Crosstalk', "nukescripts.createNodeLocal(\"CCrosstalk\")", icon='Crosstalk.png')
    m.addCommand('Exposure', "nukescripts.createNodeLocal(\"EXPTool\")", icon='Exposure.png')
    m.addCommand('Grade', "nukescripts.createNodeLocal(\"Grade\")",
                 'g', icon='Grade.png', shortcutContext=dagContext)
    m.addCommand('@;GradeBranch', "nukescripts.createNodeLocal(\"Grade\")",
                 '+g', shortcutContext=dagContext)
    m.addCommand('Histogram', "nukescripts.createNodeLocal(\"Histogram\")", icon='Histogram.png')
    m.addCommand('HistEQ', "nukescripts.createNodeLocal(\"HistEQ\")", icon='HistEQ.png')
    m.addCommand('HueCorrect', "nukescripts.createNodeLocal(\"HueCorrect\")", icon='HueCorrect.png')
    m.addCommand('HueShift', "nukescripts.createNodeLocal(\"HueShift\")", icon='HueShift.png')
    m.addCommand('HSVTool', "nukescripts.createNodeLocal(\"HSVTool\")", icon='HSVTool.png')
    m.addCommand('Invert', "nukescripts.createNodeLocal(\"Invert\")", icon='Invert.png')
    m.addCommand('Log2Lin', "nukescripts.createNodeLocal(\"Log2Lin\")", icon='Log2Lin.png')
    m.addCommand('PLogLin', "nukescripts.createNodeLocal(\"PLogLin\")", icon='Log2Lin.png')
    m.addCommand('MatchGrade', "nukescripts.createNodeLocal(\"MatchGrade\")", icon='MatchGrade.png')
    m.addCommand('MinColor', "nukescripts.createNodeLocal(\"MinColor\")", icon='MinColor.png')
    m.addCommand('Posterize', "nukescripts.createNodeLocal(\"Posterize\")", icon='Posterize.png')
    m.addCommand('RolloffContrast', "nukescripts.createNodeLocal(\"RolloffContrast\")",
                 icon='RolloffContrast.png')
    m.addCommand('Saturation', "nukescripts.createNodeLocal(\"Saturation\")", icon='Saturation.png')
    m.addCommand('Sampler', "nukescripts.createNodeLocal(\"Sampler\")", icon='Sampler.png')
    m.addCommand('SoftClip', "nukescripts.createNodeLocal(\"SoftClip\")", icon='SoftClip.png')
    m.addCommand('Toe', "nukescripts.createNodeLocal(\"Toe2\")", icon='Toe.png')

    # The "Filter" menu
    m = toolbar.addMenu('Filter', 'ToolbarFilter.png')
    m.addCommand('Blur', "nukescripts.createNodeLocal(\"Blur\")",
                 'b', icon='Blur.png', shortcutContext=dagContext)
    m.addCommand('@;BlurBranch', "nukescripts.createNodeLocal(\"Blur\")",
                 '+b', shortcutContext=dagContext)
    m.addCommand('Bilateral', "nukescripts.createNodeLocal(\"Bilateral2\")", icon='Bilateral.png')
    m.addCommand('Bokeh', "nukescripts.createNodeLocal(\"Bokeh\")", icon='pgBokeh.png')
    m.addCommand('BumpBoss', "nukescripts.createNodeLocal(\"BumpBoss\")", icon='BumpBoss.png')
    m.addCommand('Convolve', "nukescripts.createNodeLocal(\"Convolve2\")", icon='Convolve.png')
    m.addCommand('Defocus', "nukescripts.createNodeLocal(\"Defocus\")", icon='Defocus.png')
    m.addCommand('DegrainBlue', "nukescripts.createNodeLocal(\"DegrainBlue\")",
                 icon='DegrainBlue.png')
    m.addCommand('DegrainSimple', "nukescripts.createNodeLocal(\"DegrainSimple\")",
                 icon='DegrainSimple.png')
    m.addCommand('Denoise', "nukescripts.createNodeLocal(\"Denoise2\")", icon='denoise.png')
    m.addCommand('DirBlur', "nukescripts.createNodeLocal(\"DirBlurWrapper\")", icon='DirBlur.png')
    m.addCommand('DropShadow', "nukescripts.createNodeLocal(\"DropShadow\")", icon='DropShadow.png')
    m.addCommand('EdgeBlur', "nukescripts.createNodeLocal(\"EdgeBlur\")", icon='EdgeBlur.png')
    m.addCommand('EdgeDetect', "nukescripts.createNodeLocal(\"EdgeDetectWrapper\")",
                 icon='EdgeDetect.png')
    m.addCommand('EdgeExtend', "nukescripts.createNodeLocal(\"EdgeExtend\")", icon='EdgeExtend.png')
    m.addCommand('Emboss', "nukescripts.createNodeLocal(\"Emboss\")", icon='Emboss.png')
    m.addCommand('Erode (fast)', "nukescripts.createNodeLocal(\"Dilate\")", icon='ErodeFast.png')
    m.addCommand('Erode (filter)', "nukescripts.createNodeLocal(\"FilterErode\")",
                 icon='FilterErode.png')
    m.addCommand('Erode (blur)', "nukescripts.createNodeLocal(\"Erode\")", icon='ErodeBlur.png')
    m.addCommand('Glow', "nukescripts.createNodeLocal(\"Glow2\")", icon='Glow.png')
    m.addCommand('GodRays', "nukescripts.createNodeLocal(\"GodRays\")", icon='GodRays.png')
    m.addCommand('Inpaint', "nukescripts.createNodeLocal(\"Inpaint2\")", icon='Inpaint.png')
    m.addCommand('Laplacian', "nukescripts.createNodeLocal(\"Laplacian\")", icon='Laplacian.png')
    m.addCommand('LevelSet', "nukescripts.createNodeLocal(\"LevelSet\")", icon='LevelSet.png')

    if not assist:
        m.addCommand(
            'Matrix...', 'with nuke.lastHitGroup():\n  nukescripts.create_matrix()', icon='Matrix.png')
    m.addCommand('Median', "nukescripts.createNodeLocal(\"Median\")", icon='Median.png')
    m.addCommand('MotionBlur', "nukescripts.createNodeLocal(\"MotionBlur\")",
                 icon='MotionBlur2D.png')
    m.addCommand('MotionBlur2D', "nukescripts.createNodeLocal(\"MotionBlur2D\")",
                 icon='MotionBlur2D.png')
    m.addCommand('MotionBlur3D', "nukescripts.createNodeLocal(\"MotionBlur3D\")",
                 icon='MotionBlur3D.png')
    m.addCommand('Sharpen', "nukescripts.createNodeLocal(\"Sharpen\")", icon='Sharpen.png')
    m.addCommand('Soften', "nukescripts.createNodeLocal(\"Soften\")", icon='Soften.png')
    m.addCommand('VectorBlur', "nukescripts.createNodeLocal(\"VectorBlur2\")", icon='VectorBlur.png')
    m.addCommand('VolumeRays', "nukescripts.createNodeLocal(\"VolumeRays\")", icon='VolumeRays.png')
    m.addCommand('ZDefocus', "nukescripts.createNodeLocal(\"ZDefocus2\")", icon='ZBlur.png')
    m.addCommand('ZSlice', "nukescripts.createNodeLocal(\"ZSlice\")", icon='ZSlice.png')

    # The "Keyer" menu
    m = toolbar.addMenu('Keyer', 'ToolbarKeyer.png')
    m.addCommand('ChromaKeyer', "nukescripts.createNodeLocal(\"ChromaKeyer\")",
                 icon='ChromaKeyer.png')
    m.addCommand('Cryptomatte', "nukescripts.createNodeLocal(\"Cryptomatte\")",
                 icon='Cryptomatte.png')
    m.addCommand('Encryptomatte', "nukescripts.createNodeLocal(\"Encryptomatte\")",
                 icon='Encryptomatte.png')
    m.addCommand('Difference', "nukescripts.createNodeLocal(\"Difference\")",
                 icon='DifferenceKeyer.png')
    m.addCommand('HueKeyer', "nukescripts.createNodeLocal(\"HueKeyer\")", icon='HueKeyer.png')
    if not assist:
        m.addCommand(
            'IBKColour', "with nuke.lastHitGroup():\n  nuke.tcl(\"IBKColourV3\")", icon='IBKColour.png')
        m.addCommand('IBKGizmo', "with nuke.lastHitGroup():\n  nuke.tcl(\"IBKGizmoV3\")",
                     icon='IBKGizmo.png')
    m.addCommand('Keyer', "nukescripts.createNodeLocal(\"Keyer\")", icon='Keyer.png')
    m.addCommand(
        'Keylight', 'nukescripts.createNodeLocal("OFXuk.co.thefoundry.keylight.keylight_v201")', icon='Keylight.png')
    m.addCommand('Primatte', "nukescripts.createNodeLocal(\"Primatte3\")", icon='Primatte.png')
    m.addCommand('Ultimatte', "nukescripts.createNodeLocal(\"Ultimatte\")", icon='Ultimatte.png')

    # The "Merge" menu
    m = toolbar.addMenu('Merge', 'ToolbarMerge.png')
    m.addCommand('AddMix', "nukescripts.createNodeLocal(\"AddMix\")",
                 '+a', icon='AddMix.png', shortcutContext=dagContext)
    m.addCommand('KeyMix', "nukescripts.createNodeLocal(\"Keymix\")", icon='Keymix.png')
    m.addCommand('ContactSheet', "nukescripts.createNodeLocal(\"ContactSheet\")",
                 icon='ContactSheet.png')
    m.addCommand('CopyBBox', "nukescripts.createNodeLocal(\"CopyBBox\")", icon='CopyBBox.png')
    m.addCommand('CopyRectangle', "nukescripts.createNodeLocal(\"CopyRectangle\")",
                 icon='CopyRectangle.png')
    m.addCommand('Dissolve', "nukescripts.createNodeLocal(\"Dissolve\")", icon='Dissolve.png')
    m.addCommand('LayerContactSheet', "nukescripts.createNodeLocal(\"LayerContactSheet\")",
                 icon='LayerContactSheet.png')
    m.addCommand('Merge', "nukescripts.createNodeLocal(\"Merge2\")",
                 'm', icon='Merge.png', shortcutContext=dagContext)
    m.addCommand('@;MergeBranch', "nukescripts.createNodeLocal(\"Merge2\")",
                 '+m', shortcutContext=dagContext)

    n = m.addMenu('Merges', 'Merge.png')
    if not assist:
        n.addCommand(
            'Plus', "nukescripts.createNodeLocal(\"Merge2\", \"operation plus name Plus\", False)", icon='MergePlus.png')
        n.addCommand(
            'Matte', "nukescripts.createNodeLocal(\"Merge2\", \"operation matte name Matte\", False)", icon='MergeMatte.png')
        n.addCommand(
            'Multiply', "nukescripts.createNodeLocal(\"Merge2\", \"operation multiply name Multiply\", False)", icon='MergeMultiply.png')
        n.addCommand(
            'In', "nukescripts.createNodeLocal(\"Merge2\", \"operation in name In\", False)", icon='MergeIn.png')
        n.addCommand(
            'Out', "nukescripts.createNodeLocal(\"Merge2\", \"operation out name Out\", False)", icon='MergeOut.png')
        n.addCommand(
            'Screen', "nukescripts.createNodeLocal(\"Merge2\", \"operation screen name Scrn\", False)", icon='MergeScreen.png')
        n.addCommand(
            'Max', "nukescripts.createNodeLocal(\"Merge2\", \"operation max name Max\", False)", icon='MergeMax.png')
        n.addCommand(
            'Min', "nukescripts.createNodeLocal(\"Merge2\", \"operation min name Min\", False)", icon='MergeMin.png')
        n.addCommand('Absminus', "nukescripts.createNodeLocal(\"Merge2\", \"operation difference name Difference\", False)",
                     icon='MergeDifference.png')
        m.addCommand('MergeExpression', "nukescripts.createNodeLocal(\"MergeExpression\")",
                     icon='MergeExpression.png')
    m.addCommand('Switch', "nukescripts.createNodeLocal(\"Switch\")", icon='Switch.png')
    if not assist:
        m.addCommand('TimeDissolve', "nukescripts.createNodeLocal(\"TimeDissolve\")",
                     icon='TimeDissolve.png')
    m.addCommand('Premult', "nukescripts.createNodeLocal(\"Premult\")", icon='Premult.png')
    m.addCommand('Unpremult', "nukescripts.createNodeLocal(\"Unpremult\")", icon='Unpremult.png')
    if not assist:
        m.addCommand('Blend', "nukescripts.createNodeLocal(\"Blend\")", icon='Blend.png')
        m.addCommand('ZMerge', "nukescripts.createNodeLocal(\"ZMerge\")", icon='ZMerge.png')

    # The "Transform" menu
    m = toolbar.addMenu('Transform', 'ToolbarTransform.png')
    m.addCommand('Transform', "nukescripts.createNodeLocal(\"Transform\")",
                 't', icon='2D.png', shortcutContext=dagContext)
    m.addCommand('@;Transform Branch', "nukescripts.createNodeLocal(\"Transform\")",
                 '+t', shortcutContext=dagContext)
    m.addCommand('TransformMasked', "nukescripts.createNodeLocal(\"TransformMasked\")",
                 icon='2DMasked.png')
    m.addCommand('Card3D', "nukescripts.createNodeLocal(\"Card3D\")", icon='3D.png')
    m.addCommand('AdjustBBox', "nukescripts.createNodeLocal(\"AdjBBox\")", icon='AdjBBox.png')
    m.addCommand('BlackOutside', "nukescripts.createNodeLocal(\"BlackOutside\")",
                 icon='BlackOutside.png')
    m.addCommand('CameraShake', "nukescripts.createNodeLocal(\"CameraShake3\")",
                 icon='CameraShake.png')
    m.addCommand('Crop', "nukescripts.createNodeLocal(\"Crop\")", icon='Crop.png')
    m.addCommand('CornerPin', "nukescripts.createNodeLocal(\"CornerPin2D\")", icon='CornerPin.png')
    m.addCommand('VectorCornerPin', "nukescripts.createNodeLocal(\"VectorCornerPin\")",
                 icon='VectorCornerPin.png')
    m.addCommand('SphericalTransform',
                 "nukescripts.createNodeLocal(\"SphericalTransform2\")", icon='EnvironMaps.png')
    m.addCommand('IDistort', "nukescripts.createNodeLocal(\"IDistort\")", icon='IDistort.png')
    m.addCommand('VectorDistort', "nukescripts.createNodeLocal(\"VectorDistort\")",
                 icon='VectorDistort.png')
    m.addCommand('LensDistortion', "nukescripts.createNodeLocal(\"LensDistortion2\")",
                 icon='LensDistort.png')
    m.addCommand('Mirror', "nukescripts.createNodeLocal(\"Mirror2\")", icon='Mirror.png')
    m.addCommand('Position', "nukescripts.createNodeLocal(\"Position\")", icon='Position.png')
    m.addCommand('Reformat', "nukescripts.createNodeLocal(\"Reformat\")", icon='Reformat.png')
    m.addCommand('Reconcile3D', "nukescripts.createNodeLocal(\"Reconcile3D\")",
                 icon='Reconcile3D.png')
    m.addCommand('PointsTo3D', "nukescripts.createNodeLocal(\"PointsTo3D\")", icon='PointsTo3D.png')
    m.addCommand('PlanarTracker', 'with nuke.lastHitGroup():\n  nukescripts.createPlanartracker()',
                 icon='planar_tracker.png')
    m.addCommand('Tracker', "nukescripts.createNodeLocal(\"Tracker4\")", icon='Tracker.png')
    m.addCommand('TVIScale', "nukescripts.createNodeLocal(\"TVIscale\")", icon='TVIScale.png')
    m.addCommand('GridWarp', "nukescripts.createNodeLocal(\"GridWarp3\")", icon='GridWarp.png')
    m.addCommand('GridWarpTracker', "nukescripts.createNodeLocal(\"GridWarpTracker\")",
                 icon='GridWarpTracker.png')
    m.addCommand('SplineWarp', "nukescripts.createNodeLocal(\"SplineWarp3\")", icon='SplineWarp.png')
    m.addCommand('Stabilize', "nukescripts.createNodeLocal(\"Stabilize2D\")", icon='Stabilize.png')
    m.addCommand('STMap', "nukescripts.createNodeLocal(\"STMap\")", icon='STMap.png')
    m.addCommand('Tile', "nukescripts.createNodeLocal(\"Tile\")", icon='Tile.png')

    # m.addCommand("AutoCrop", "nukescripts.autocrop()", icon="AutoCrop.png")

    # The "3D" menu
    m = toolbar.addMenu('3D', 'Cube.png')

    m3D = m.addMenu('3D', 'GeoCube_3D.png', tag=MenuItemTag.Beta)

    n = m3D.addMenu('Create', 'Create_3D.png')
    n.addCommand('GeoCard', "nukescripts.createNodeLocal(\"GeoCard\")",
                 icon='GeoCard_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('GeoCube', "nukescripts.createNodeLocal(\"GeoCube\")",
                 icon='GeoCube_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('GeoCylinder', "nukescripts.createNodeLocal(\"GeoCylinder\")",
                 icon='GeoCylinder_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('GeoExport', "nukescripts.createNodeLocal(\"GeoExport\")",
                 icon='GeoExport_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('GeoImport', "nukescripts.createNodeLocal(\"GeoImport\")",
                 icon='GeoImport_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('GeoPoints', "nukescripts.createNodeLocal(\"GeoPoints\")",
                 icon='GeoPoints_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('GeoPointsToMesh', "nukescripts.createNodeLocal(\"GeoPointsToMesh\")",
                 icon='GeoPointsToMesh_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('GeoReference', "nukescripts.createNodeLocal(\"GeoReference\")",
                 icon='GeoReference_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('GeoRevolve', "nukescripts.createNodeLocal(\"GeoRevolve\")",
                 icon='GeoRevolve_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('GeoScope', "nukescripts.createNodeLocal(\"GeoScope\")",
                 icon='GeoScope_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('GeoSphere', "nukescripts.createNodeLocal(\"GeoSphere\")",
                 icon='GeoSphere_3D.png', tag=MenuItemTag.Beta)

    n = m3D.addMenu('Lights', 'Lights_3D.png')
    n.addCommand('DirectLight', "nukescripts.createNodeLocal(\"DirectLight1\")",
                 icon='DirectLight_3D.png', tag=MenuItemTag.Beta, nodeClass='DirectLight1')
    n.addCommand('EnvironmentLight', "nukescripts.createNodeLocal(\"EnvironmentLight\")",
                 icon='EnvironmentLight_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('PointLight', "nukescripts.createNodeLocal(\"PointLight\")",
                 icon='Light_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('SpotLight', "nukescripts.createNodeLocal(\"SpotLight1\")",
                 icon='SpotLight_3D.png', tag=MenuItemTag.Beta, nodeClass='SpotLight1')

    n = m3D.addMenu('Modify', 'Modify_3D.png')
    n.addCommand('GeoBindMaterial', "nukescripts.createNodeLocal(\"GeoBindMaterial\")",
                 icon='GeoBindMaterial_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('GeoCollection', "nukescripts.createNodeLocal(\"GeoCollection\")",
                 icon='GeoCollection_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('GeoDisplace', "nukescripts.createNodeLocal(\"GeoDisplace\")",
                 icon='GeoDisplace_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('GeoDrawMode', "nukescripts.createNodeLocal(\"GeoDrawMode\")",
                 icon='GeoDrawMode_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('GeoDuplicate', "nukescripts.createNodeLocal(\"GeoDuplicate\")",
                 icon='GeoDuplicate_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('GeoInstance', "nukescripts.createNodeLocal(\"GeoInstance\")",
                 icon='GeoInstance_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('GeoIsolate', "nukescripts.createNodeLocal(\"GeoIsolate\")",
                 icon='GeoPrune_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('GeoMerge', "nukescripts.createNodeLocal(\"GeoMerge\")",
                 icon='GeoMerge_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('GeoNoise', "nukescripts.createNodeLocal(\"GeoNoise\")",
                 icon='GeoNoise_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('GeoNormals', "nukescripts.createNodeLocal(\"GeoNormals\")",
                 icon='GeoNormals_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('GeoPrune', "nukescripts.createNodeLocal(\"GeoPrune\")",
                 icon='GeoPrune_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('GeoRadialWarp', "nukescripts.createNodeLocal(\"GeoRadialWarp\")",
                 icon='GeoRadialWarp_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('GeoSelector', "nukescripts.createNodeLocal(\"GeoSelector\")",
                 icon='GeoSelector_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('GeoTransform', "nukescripts.createNodeLocal(\"GeoTransform\")",
                 icon='GeoTransform_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('GeoTrilinearWarp', "nukescripts.createNodeLocal(\"GeoTrilinearWarp\")",
                 icon='GeoTrilinearWarp_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('GeoUVProject', "nukescripts.createNodeLocal(\"GeoUVProject\")",
                 icon='GeoUVProject_3D.png', tag=MenuItemTag.Beta)

    n = m3D.addMenu('Shader', 'Shaders_3D.png')
    n.addCommand('BasicSurface', "nukescripts.createNodeLocal(\"BasicSurface\")",
                 icon='Shader_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('ConstantShader', "nukescripts.createNodeLocal(\"ConstantShader\")",
                 icon='ConstantShader_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('FillShader', "nukescripts.createNodeLocal(\"FillShader\")",
                 icon='Shader_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('MergeLayerShader', "nukescripts.createNodeLocal(\"MergeLayerShader\")",
                 icon='MergeLayerShader_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('PreviewSurface', "nukescripts.createNodeLocal(\"PreviewSurface\")",
                 icon='Shader_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('Project3DShader', "nukescripts.createNodeLocal(\"Project3DShader\")",
                 icon='Project3D_3D.png', tag=MenuItemTag.Beta)
    n.addCommand('WireframeShader', "nukescripts.createNodeLocal(\"WireframeShader\")",
                 icon='Shader_3D.png', tag=MenuItemTag.Beta)

    m3D.addCommand('Axis', "nukescripts.createNodeLocal(\"Axis4\")",
                   icon='Axis_3D.png', tag=MenuItemTag.Beta, nodeClass='Axis4')
    m3D.addCommand('Camera', "nukescripts.createNodeLocal(\"Camera4\")",
                   icon='Camera_3D.png', tag=MenuItemTag.Beta, nodeClass='Camera4')
    m3D.addCommand('CameraTracker', "nukescripts.createNodeLocal(\"CameraTracker\", \"new3D True\")",
                   icon='CameraTracker_3D.png', tag=MenuItemTag.Beta)
    m3D.addCommand('DepthGenerator', "nukescripts.createNodeLocal(\"DepthGenerator\", \"new3D True\")",
                   icon='DepthGenerator_3D.png', tag=MenuItemTag.Beta)
    m3D.addCommand('DepthToPosition', "nukescripts.createNodeLocal(\"DepthToPosition\")",
                   icon='DepthToPosition_3D.png')
    m3D.addCommand('GeoScene', "nukescripts.createNodeLocal(\"GeoScene\")",
                   icon='GeoScene_3D.png', tag=MenuItemTag.Beta)
    m3D.addCommand('GeoViewScene', "nukescripts.createNodeLocal(\"GeoViewScene\")",
                   icon='GeoViewScene_3D.png', tag=MenuItemTag.Beta)
    m3D.addCommand('PointsGenerator', "nukescripts.createNodeLocal(\"PointsGenerator\")",
                   icon='PointsGenerator_3D.png', tag=MenuItemTag.Beta)
    m3D.addCommand('ScanlineRender', "nukescripts.createNodeLocal(\"ScanlineRender2\")",
                   icon='ScanlineRender_3D.png', tag=MenuItemTag.Beta, nodeClass='ScanlineRender2')

    m3Dclassic = m.addMenu('3D Classic', 'Cube.png')

    m3Dclassic.addCommand('Axis', "nukescripts.createNodeLocal(\"Axis3\")", icon='Axis.png',
                          tag=MenuItemTag.Classic, nodeClass='Axis3', tagTarget=MenuItemTagTargetFlag.TabMenu)

    n = m3Dclassic.addMenu('Geometry', 'Geometry.png')
    n.addCommand('Card', "nukescripts.createNodeLocal(\"Card2\")", icon='Card.png',
                 tag=MenuItemTag.Classic, nodeClass='Card2', tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('Cube', "nukescripts.createNodeLocal(\"Cube\")", icon='Cube.png',
                 tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('Cylinder', "nukescripts.createNodeLocal(\"Cylinder\")", icon='Cylinder.png',
                 tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('DepthToPoints', "nukescripts.createNodeLocal(\"DepthToPoints\")",
                 icon='DepthToPoints.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('ModelBuilder', "nukescripts.createNodeLocal(\"ModelBuilder\")",
                 icon='Modeler.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('PointCloudGenerator', "nukescripts.createNodeLocal(\"PointCloudGenerator\")",
                 icon='PointCloudGenerator.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('PositionToPoints', "nukescripts.createNodeLocal(\"PositionToPoints2\")", icon='PositionToPoints.png',
                 tag=MenuItemTag.Classic, nodeClass='PositionsToPoints2', tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('PoissonMesh', "nukescripts.createNodeLocal(\"PoissonMesh\")",
                 icon='GeoPointsToMesh.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('Sphere', "nukescripts.createNodeLocal(\"Sphere\")", icon='Sphere.png',
                 tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('ReadGeo', "nukescripts.createNodeLocal(\"ReadGeo2\")", icon='ReadGeo.png',
                 tag=MenuItemTag.Classic, nodeClass='ReadGeo2', tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('WriteGeo', "nukescripts.createNodeLocal(\"WriteGeo\")", icon='WriteGeo.png',
                 tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)

    n = m3Dclassic.addMenu('Lights', 'Toolbar3DLights.png')
    n.addCommand('Light', "nukescripts.createNodeLocal(\"Light3\")", icon='PointLight.png',
                 tag=MenuItemTag.Classic, nodeClass='Light3', tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('Point', "nukescripts.createNodeLocal(\"Light\")", icon='PointLight.png',
                 tag=MenuItemTag.Classic, nodeClass='Light', tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('Direct', "nukescripts.createNodeLocal(\"DirectLight\")", icon='DirectLight.png',
                 tag=MenuItemTag.Classic, nodeClass='DirectLight', tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('Spot', "nukescripts.createNodeLocal(\"Spotlight\")", icon='SpotLight.png',
                 tag=MenuItemTag.Classic, nodeClass='SpotLight', tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('Environment', "nukescripts.createNodeLocal(\"Environment\")",
                 icon='Environment.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('Relight', "nukescripts.createNodeLocal(\"ReLight\")", icon='ReLight.png',
                 tag=MenuItemTag.Classic, nodeClass='ReLight', tagTarget=MenuItemTagTargetFlag.TabMenu)

    n = m3Dclassic.addMenu('Modify', 'Modify.png')
    n.addCommand('TransformGeo', "nukescripts.createNodeLocal(\"TransformGeo\")",
                 icon='Modify.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('MergeGeo', "nukescripts.createNodeLocal(\"MergeGeo\")", icon='Modify.png',
                 tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('CrosstalkGeo', "nukescripts.createNodeLocal(\"CrosstalkGeo\")",
                 icon='Modify.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('DisplaceGeo', "nukescripts.createNodeLocal(\"DisplaceGeo\")",
                 icon='Modify.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('EditGeo', "nukescripts.createNodeLocal(\"EditGeo\")", icon='Modify.png',
                 tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('GeoSelect', """nukescripts.createNodeLocal("GeoSelect")""",
                 icon='Modify.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('LookupGeo', "nukescripts.createNodeLocal(\"LookupGeo\")",
                 icon='Modify.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('LogGeo', "nukescripts.createNodeLocal(\"LogGeo\")", icon='Modify.png',
                 tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('Normals', "nukescripts.createNodeLocal(\"Normals\")", icon='Modify.png',
                 tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('ProceduralNoise', "nukescripts.createNodeLocal(\"ProcGeo\")", icon='Modify.png',
                 tag=MenuItemTag.Classic, nodeClass='ProcGeo', tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('RadialDistort', "nukescripts.createNodeLocal(\"RadialDistort\")",
                 icon='Modify.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('Trilinear', "nukescripts.createNodeLocal(\"Trilinear\")",
                 icon='Modify.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('UVProject', "nukescripts.createNodeLocal(\"UVProject\")",
                 icon='Modify.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n = n.addMenu('RenderMan', 'Modify.png')
    n.addCommand('ModifyRIB', "nukescripts.createNodeLocal(\"ModifyRIB\")",
                 icon='Modify.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)

    n = m3Dclassic.addMenu('Shader', 'Shaders.png')
    n.addCommand('AmbientOcclusion', "nukescripts.createNodeLocal(\"AmbientOcclusion\")",
                 icon='Shader.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('ApplyMaterial', "nukescripts.createNodeLocal(\"ApplyMaterial\")",
                 icon='Shader.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('BasicMaterial', "nukescripts.createNodeLocal(\"BasicMaterial\")",
                 icon='Shader.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('FillMat', "nukescripts.createNodeLocal(\"FillMat\")", icon='Shader.png',
                 tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('MergeMat', "nukescripts.createNodeLocal(\"MergeMat\")", icon='Shader.png',
                 tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('BlendMat', "nukescripts.createNodeLocal(\"BlendMat\")", icon='Shader.png',
                 tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('Project3D', "nukescripts.createNodeLocal(\"Project3D2\")", icon='Shader.png',
                 tag=MenuItemTag.Classic, nodeClass='Project3D2', tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('Diffuse', "nukescripts.createNodeLocal(\"Diffuse\")", icon='Shader.png',
                 tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('Emission', "nukescripts.createNodeLocal(\"Emission\")", icon='Shader.png',
                 tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('Phong', "nukescripts.createNodeLocal(\"Phong\")", icon='Shader.png',
                 tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('Specular', "nukescripts.createNodeLocal(\"Specular\")", icon='Shader.png',
                 tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('Displacement', "nukescripts.createNodeLocal(\"Displacement\")",
                 icon='Shader.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    if not assist:
        n.addCommand('UVTile', 'with nuke.lastHitGroup():\n  nukescripts.createUVTile()', icon='Shader.png',
                     tag=MenuItemTag.Classic, nodeClass='UVTile2', tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('Wireframe', "nukescripts.createNodeLocal(\"Wireframe\")",
                 icon='Shader.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('Transmission', "nukescripts.createNodeLocal(\"Transmission\")",
                 icon='Shader.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n = n.addMenu('RenderMan', 'Shaders.png')
    n.addCommand('Reflection', "nukescripts.createNodeLocal(\"Reflection\")",
                 icon='Shader.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    n.addCommand('Refraction', "nukescripts.createNodeLocal(\"Refraction\")",
                 icon='Shader.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)

    m3Dclassic.addCommand('Camera', "nukescripts.createNodeLocal(\"Camera3\")", icon='Camera.png',
                          tag=MenuItemTag.Classic, nodeClass='Camera3', tagTarget=MenuItemTagTargetFlag.TabMenu)
    m3Dclassic.addCommand('CameraTracker', "nukescripts.createNodeLocal(\"CameraTracker\")",
                          icon='CameraTracker.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    m3Dclassic.addCommand('DepthGenerator', "nukescripts.createNodeLocal(\"DepthGenerator\")",
                          icon='DepthGenerator.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    m3Dclassic.addCommand(
        'DepthToPosition', "nukescripts.createNodeLocal(\"DepthToPosition\")", icon='DepthToPosition.png')
    m3Dclassic.addCommand('Scene', "nukescripts.createNodeLocal(\"Scene\")", icon='Scene.png',
                          tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    m3Dclassic.addCommand('ScanlineRender', "nukescripts.createNodeLocal(\"ScanlineRender\")",
                          icon='Render.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)
    m3Dclassic.addCommand('RayRender', "nukescripts.createNodeLocal(\"RayRender\")",
                          icon='Render.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)

    if not assist:
        n = m3Dclassic.addMenu('RenderMan', 'Toolbar3D.png')
        n.addCommand('PrmanRender', 'with nuke.lastHitGroup():\n  nukescripts.createPrmanRender()',
                     icon='Render.png', tag=MenuItemTag.Classic, tagTarget=MenuItemTagTargetFlag.TabMenu)

    # particles menu
    m = toolbar.addMenu('Particles', 'ToolbarParticles.png')
    m.addCommand('ParticleEmitter', "nukescripts.createNodeLocal('ParticleEmitter')")

    m.addCommand('ParticleBounce', "nukescripts.createNodeLocal('ParticleBounce')")
    m.addCommand('ParticleCache', "nukescripts.createNodeLocal('ParticleCache')",
                 icon='ParticleCache.png')
    m.addCommand('ParticleCurve', "nukescripts.createNodeLocal('ParticleCurve')")
    m.addCommand('ParticleDirectionalForce',
                 "nukescripts.createNodeLocal('ParticleDirectionalForce')")
    m.addCommand('ParticleDrag', "nukescripts.createNodeLocal('ParticleDrag2')",
                 icon='ParticleDrag.png')
    m.addCommand('ParticleExpression', "nukescripts.createNodeLocal('ParticleExpression')")
    m.addCommand('ParticleMerge', "nukescripts.createNodeLocal('ParticleMerge')")
    m.addCommand('ParticleMotionAlign', "nukescripts.createNodeLocal('ParticleMotionAlign')")
    m.addCommand('ParticleGravity', "nukescripts.createNodeLocal('ParticleGravity')")

    # Disable ParticleLineForce for now as it is not ready for being included in the bundle - Bug 30000
    # m.addCommand("ParticleLineForce")

    m.addCommand('ParticleLookAt', "nukescripts.createNodeLocal('ParticleLookAt')")
    m.addCommand('ParticlePointForce', "nukescripts.createNodeLocal('ParticlePointForce')")
    m.addCommand('ParticleSpeedLimit', "nukescripts.createNodeLocal('ParticleSpeedLimit')")
    m.addCommand('ParticleSpawn', "nukescripts.createNodeLocal('ParticleSpawn')")
    m.addCommand('ParticleTurbulence', "nukescripts.createNodeLocal('ParticleTurbulence')")
    m.addCommand('ParticleVortex', "nukescripts.createNodeLocal('ParticleVortex')")
    m.addCommand('ParticleWind', "nukescripts.createNodeLocal('ParticleWind')")
    m.addCommand('ParticleSettings', "nukescripts.createNodeLocal('ParticleSettings')",
                 icon='particle_settings.png')
    m.addCommand('ParticleToGeo', "nukescripts.createNodeLocal('ParticleToGeo')")
    m.addCommand('ParticleBlinkScript', "nukescripts.createNodeLocal('ParticleBlinkScript')",
                 icon='ParticleBlinkScript.png')

    n = m.addMenu('ParticleBlinkScript Gizmos', 'ParticleBlinkScript.png')
    n.addCommand('ParticleColorByAge', "nukescripts.createNodeLocal('ParticleColorByAge')",
                 icon='ParticleBlinkScript.png')
    n.addCommand('ParticleKill', "nukescripts.createNodeLocal('ParticleKill')",
                 icon='ParticleBlinkScript.png')
    n.addCommand('ParticleProjectDisplace',
                 "nukescripts.createNodeLocal('ParticleProjectDisplace')", icon='ParticleBlinkScript.png')
    n.addCommand('ParticleProjectImage',
                 "nukescripts.createNodeLocal('ParticleProjectImage')", icon='ParticleBlinkScript.png')
    n.addCommand('ParticleGrid', "nukescripts.createNodeLocal('ParticleGrid')",
                 icon='ParticleBlinkScript.png')
    n.addCommand('ParticleDirection', "nukescripts.createNodeLocal('ParticleDirection')",
                 icon='ParticleBlinkScript.png')
    n.addCommand('ParticleFuse', "nukescripts.createNodeLocal('ParticleFuse')",
                 icon='ParticleBlinkScript.png')
    n.addCommand('ParticleDistributeSphere',
                 "nukescripts.createNodeLocal('ParticleDistributeSphere')", icon='ParticleBlinkScript.png')
    n.addCommand('ParticleCylinderFlow',
                 "nukescripts.createNodeLocal('ParticleCylinderFlow')", icon='ParticleBlinkScript.png')
    n.addCommand('ParticleConstrainToSphere',
                 "nukescripts.createNodeLocal('ParticleConstrainToSphere')", icon='ParticleBlinkScript.png')
    n.addCommand('ParticleFlock', "nukescripts.createNodeLocal('ParticleFlock')",
                 icon='ParticleBlinkScript.png')
    n.addCommand('ParticleAttractToSphere',
                 "nukescripts.createNodeLocal('ParticleAttractToSphere')", icon='ParticleBlinkScript.png')
    n.addCommand('ParticleHelixFlow', "nukescripts.createNodeLocal('ParticleHelixFlow')",
                 icon='ParticleBlinkScript.png')
    n.addCommand('ParticleShockWave', "nukescripts.createNodeLocal('ParticleShockWave')",
                 icon='ParticleBlinkScript.png')

    m.addCommand('ParticleInfo', "nukescripts.createNodeLocal('ParticleInfo')",
                 icon='ParticleInfo.png')

    # deep menu
    m = toolbar.addMenu('Deep', 'ToolbarDeep.png')
    m.addCommand('DeepColorCorrect', "nukescripts.createNodeLocal('DeepColorCorrect2')")
    m.addCommand('DeepCrop', "nukescripts.createNodeLocal('DeepCrop')")
    m.addCommand('DeepExpression', "nukescripts.createNodeLocal('DeepExpression')")
    m.addCommand('DeepFromFrames', "nukescripts.createNodeLocal('DeepFromFrames')")
    m.addCommand('DeepFromImage', "nukescripts.createNodeLocal('DeepFromImage')")
    m.addCommand('DeepMerge', "nukescripts.createNodeLocal('DeepMerge2')")
    if not assist:
        m.addCommand('DeepRead', '''with nuke.lastHitGroup():\n  nukescripts.create_read("DeepRead")''')
    m.addCommand('DeepRecolor', "nukescripts.createNodeLocal('DeepRecolor')")
    m.addCommand('DeepReformat', "nukescripts.createNodeLocal('DeepReformat')")
    m.addCommand('DeepSample', "nukescripts.createNodeLocal('DeepSample')")
    m.addCommand('DeepToImage', "nukescripts.createNodeLocal('DeepToImage')")
    m.addCommand('DeepToImage', "nukescripts.createNodeLocal('DeepToImage2')")
    m.addCommand('DeepToPoints', "nukescripts.createNodeLocal('DeepToPoints')")
    m.addCommand('DeepTransform', "nukescripts.createNodeLocal('DeepTransform')")
    m.addCommand('DeepWrite', "nukescripts.createNodeLocal('DeepWrite')")

    # Views menu
    m = toolbar.addMenu('Views', 'ToolbarViews.png')
    n = m.addMenu('Stereo', 'ToolbarStereo.png')
    n.addCommand('Anaglyph', "nukescripts.createNodeLocal(\"Anaglyph\")", icon='Anaglyph.png')
    n.addCommand('MixViews', "nukescripts.createNodeLocal(\"MixViews\")", icon='MixViews.png')
    n.addCommand('SideBySide', "nukescripts.createNodeLocal(\"SideBySide\")", icon='SideBySide.png')
    n.addCommand('ReConverge', "nukescripts.createNodeLocal(\"ReConverge\")", icon='ReConverge.png')

    m.addCommand('JoinViews', "nukescripts.createNodeLocal(\"JoinViews\")", icon='JoinViews.png')
    m.addCommand('OneView', "nukescripts.createNodeLocal(\"OneView\")", icon='OneView.png')
    m.addCommand('ShuffleViews', "nukescripts.createNodeLocal(\"ShuffleViews\")",
                 icon='ShuffleViews.png')
    m.addCommand('Split and Join',
                 'with nuke.lastHitGroup():\n  nukescripts.create_viewsplitjoin()', icon='SplitAndJoin.png')

    m = toolbar.addMenu('MetaData', 'MetaData.png')
    m.addCommand('ViewMetaData', "nukescripts.createNodeLocal(\"ViewMetaData\")",
                 icon='ViewMetaData.png')
    m.addCommand('CompareMetaData', "nukescripts.createNodeLocal(\"CompareMetaData\")",
                 icon='CompareMetaData.png')
    m.addCommand('ModifyMetaData', "nukescripts.createNodeLocal(\"ModifyMetaData\")",
                 icon='ModifyMetaData.png')
    m.addCommand('CopyMetaData', "nukescripts.createNodeLocal(\"CopyMetaData\")",
                 icon='CopyMetaData.png')
    m.addCommand('AddTimeCode', "nukescripts.createNodeLocal(\"AddTimeCode\")",
                 icon='AddTimeCode.png')

    import nukescripts.toolsets
    nukescripts.toolsets.createToolsetsMenu(toolbar)
    nukescripts.createNodePresetsMenu()

    # The "Other" menu
    m = toolbar.addMenu('Other', 'ToolbarOther.png')
    m.addCommand('AudioRead', "nukescripts.createNodeLocal(\"AudioRead\")", icon='Read.png')
    m.addCommand('Assert', "nukescripts.createNodeLocal(\"Assert\")", icon='Assert.png')
    m.addCommand('Backdrop', 'with nuke.lastHitGroup():\n  nukescripts.autoBackdrop()',
                 icon='Backdrop.png')
    m.addCommand('BlinkScript', "nukescripts.createNodeLocal(\"BlinkScript\")",
                 icon='BlinkScript.png')
    m.addCommand('DiskCache', "nukescripts.createNodeLocal(\"DiskCache\")",
                 '.', icon='DiskCache.png', shortcutContext=dagContext)
    m.addCommand('Dot', "nukescripts.createNodeLocal(\"Dot\", inpanel=False)",
                 '.', icon='Dot.png', shortcutContext=dagContext)
    m.addCommand('Input', "nukescripts.createNodeLocal(\"Input\")", icon='Input.png')
    m.addCommand('Output', "nukescripts.createNodeLocal(\"Output\")", icon='Output.png')
    m.addCommand('NoOp', "nukescripts.createNodeLocal(\"NoOp\")", icon='NoOp.png')
    m.addCommand('PostageStamp', "nukescripts.createNodeLocal(\"PostageStamp\")",
                 icon='PostageStamp.png')
    m.addCommand('Group', 'with nuke.lastHitGroup():\n  nuke.collapseToGroup()', icon='Group.png')
    if not assist:
        m.addCommand('Precomp', 'with nuke.lastHitGroup():\n  nukescripts.precomp_selected()',
                     '^+p', icon='Precomp.png', shortcutContext=dagContext)
        m.addCommand(
            'LiveGroup', 'with nuke.lastHitGroup():\n  nuke.collapseToLiveGroup()', icon='Group.png')
        m.addCommand('LiveInput', 'with nuke.lastHitGroup():\n  nuke.createLiveInput()',
                     icon='Input.png')

    m.addCommand('StickyNote', 'with nuke.lastHitGroup():\n  nukescripts.toolbar_sticky_note()',
                 '#n', icon='StickyNote.png', shortcutContext=dagContext)
    n = m.addMenu('All plugins', 'AllPlugins.png')
    n.addCommand('Update', "nukescripts.update_plugin_menu(\"All plugins\")")

    # The OFX plugins menus
    nuke.ofxMenu('')

    # Have to remove some of the furnace core nodes that get added automatically in nuke.ofxMenu()
    m = toolbar.menu('FurnaceCore')
    if m:
        m.removeItem('F_DeGrain')
        m.removeItem('F_DeNoise')
        m.removeItem('F_Kronos')
        m.removeItem('F_MotionBlur')
        m.removeItem('F_VectorGenerator')
        m.removeItem('F_MatchGrade')

    # Denoise2 needs to be added after the OFX plugins menus
    m = toolbar.menu('Filter')
    if not m:
        # If the Filter menu is empty, eg no allowlisted filter plugins in Nuke Assist,
        # we must create the menu afresh, as it will not exist
        m = toolbar.addMenu('Filter', 'ToolbarFilter.png')
    if m:
        m.addCommand('Denoise', "nukescripts.createNodeLocal(\"Denoise2\")", icon='denoise.png')

    # OFlow needs to be added after the OFX plugins menus
    m = toolbar.menu('Time')
    if not m:
        # If the Filter menu is empty, eg no allowlisted filter plugins in Nuke Assist,
        # we must create the menu afresh, as it will not exist
        m = toolbar.addMenu('Time', 'ToolbarTime.png')
    if m:
        m.addCommand('OFlow', 'with nuke.lastHitGroup():\n  nukescripts.createOFlow()',
                     icon='Oflow.png')

    # AIR plugins menu
    m = toolbar.addMenu('AIR', 'ToolbarAIR.png')
    m.addCommand('CopyCat', "nukescripts.createNodeLocal(\"CopyCat\")", icon='CopyCat.png')
    m.addCommand('Inference', "nukescripts.createNodeLocal(\"Inference\")", icon='Inference.png')
    m.addCommand('Deblur', "nukescripts.createNodeLocal(\"Deblur\")", icon='Deblur.png')
    m.addCommand('Upscale', "nukescripts.createNodeLocal(\"Upscale\")", icon='Upscale.png')
    m.addCommand('CatFileCreator', "nukescripts.createNodeLocal(\"CatFileCreator\")",
                 icon='CatFileCreator.png')

    import nukescripts.cattery
    nukescripts.cattery.create_menu()  # create cattery menu

    m = None
    n = None


def createCurveTool():
    n = nuke.createNode('CurveTool')
    if n.input(0):
        n['resetROI'].execute()


def createKronos():
    n = nuke.createNode('Kronos')
    if n.input(0):
        n['resetInputRange'].execute()


def createOFlow():
    n = nuke.createNode('OFlow2')
    if n.input(0):
        n['resetInputRange'].execute()

# Some helper functions that we can call from the toolbar items.


def create_time_warp():
    t = nuke.createNode('TimeWarp')
    a = nuke.value(t.name()+'.first_frame')
    e = nuke.value(t.name()+'.last_frame')
    if float(e) <= float(a):
        a = nuke.value('root.first_frame')
        e = nuke.value('root.last_frame')
    cmd = '{curve C x'+a+' '+a+' x'+e+' '+e+'}'
    t.knob('lookup').fromScript(cmd)


def create_matrix():
    p = nuke.Panel('Enter desired matrix size:')
    p.addSingleLineInput('width', 3)
    p.addSingleLineInput('height', 3)
    ret = p.show()
    if ret == 1:
        wdt = p.value('width')
        hgt = p.value('height')
        a = ' { '+' 0 '*int(wdt)+' } '
        a = '{ ' + a*int(hgt) + ' }'
        nuke.createNode('Matrix', 'matrix '+a)


def toolbar_sticky_note():
    sticky = nuke.createNode('StickyNote')
    sticky.knob('label').setValue('type note here')
    sticky.knob('selected').setValue(False)


def createPrmanRender():
    try:
        nuke.createNode('PrmanRender')
    except:
        msg = "Could not create PrmanRender node.\n\nThis is usually because the library search path environment variable is not set correctly so Nuke can't link with the prman libraries.\n"
        if 'RMANTREE' not in os.environ:
            msg = msg + '\nAlso, the RMANTREE environment variable is not set.\n'

        if nuke.env['MACOS']:
            msg = msg + \
                '\nIf you are launching Nuke from an icon on Mac OSX you may need to add environment variable settings to your environment plist file (~/.MacOSX/environment.plist).\n'
        msg = msg + "\nCheck your Pixar Photorealistic Renderman documentation section \"RenderMan Pro Server > Administration > Installation\" for platform-specific installation instructions."

        nuke.message(msg)


def createUVTile():
    uvtile_node = nuke.createNode('UVTile2')
    n = uvtile_node.input(0)

    if n and n.Class() == 'Read':
        filename = n['file'].getValue()
        udim = nukescripts.parseUdimFile(filename)
        if udim != None:
            uvtile_node['udim_enable'].setValue(True)
            uvtile_node['udim'].setValue(udim)


def createPlanartracker():

    rotoNode = nuke.createNode('Roto', 'output {rgba.alpha none none mask_planartrack.a}', False)
    rotoLayerId = 1
    rotoLayerName = 'PlanarTrackLayer'+str(rotoLayerId)

    rotoTrackLayer = rotoNode.name() + '.' + str(rotoLayerId) + '.' + rotoLayerName

    rotoCurves = rotoNode['curves']
    rotoCurveRoot = rotoCurves.rootLayer
    planarLayer = nuke.rotopaint.Layer(rotoCurves)
    rotoCurveRoot.append(planarLayer)
    atr = planarLayer.getAttributes()
    planarLayer.name = rotoLayerName
    planarLayer.getAttributes().set(nuke.rotopaint.AnimAttributes.kPlanarTrackLayerAttribute, rotoLayerId)

    rotoNode.showControlPanel()
    planarLayer.setFlag(nuke.rotopaint.FlagType.eSelectedFlag, 1)
    rotoCurves.changed()
    rotoNode['toolbox'].setValue(4)
