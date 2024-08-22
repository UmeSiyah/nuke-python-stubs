import FnCyclone
import hiero.core.log

from . import FnEdlImporter, FnOTIOImporter

hiero.core.log.info('Loading Python hiero.importers package')


# Register importers

FnCyclone.registerImporter(importer=FnOTIOImporter.OtioImporter())
if not 'otio_imports_only' in hiero.core.env['Features']:
    FnCyclone.registerImporter(importer=FnEdlImporter.EdlImporter())
