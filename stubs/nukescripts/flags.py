# Copyright (c) 2009 The Foundry Visionmongers Ltd.  All Rights Reserved.

import nuke_internal as nuke


def get_fully_qualified_name(node):
    if node.Class() == 'Root':
        return ''
    parent_name = get_fully_qualified_name(node.parent())
    if parent_name == '':
        return node.name()
    return parent_name + '.' + node.name()


def toggle(knob):
    """ "Inverts" some flags on the selected nodes.

    What this really does is set all of them to the same value, by finding the
    majority value and using the inverse of that."""

    value = 0
    n = nuke.selectedNodes(recursive=True)
    for i in n:
        try:
            val = i.knob(knob).value()
            if val:
                value += 1
            else:
                value -= 1
        except:
            pass

    status = value < 0
    for i in n:
        knobbie_str = get_fully_qualified_name(i) + '.' + knob
        if not nuke.exists(knobbie_str):
            continue
        knobbie = i.knob(knob)
        size = nuke.animation(knobbie_str, 'size')
        if size is not None and int(size) > 0:
            knobbie.setKeyAt(nuke.frame())
            knobbie.setValue(status)
        else:
            knobbie.setValue(status)
        nuke.modified(True)
