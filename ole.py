from common import *
from oletools.olevba import VBA_Parser, FileOpenError

def scan_file(path):
    """
    Given path to a file on disk, scan the file for the existence of VBA macros
    if its a supported Office document. Documents other than supported Office
    documents are considered clean.
    """
    print("[olevba] Starting OLE Macro scan of %s" % path)

    # attempt to create a VBA_parser for the file, consider
    # clean if the file is not a suppored OLE format object
    try:
        vba_parser = VBA_Parser(path)
    except FileOpenError:
        print("[olevba] file %s NOT a supported OLE format" % path)
        return AV_STATUS_CLEAN

    # consider any file that contains macros to be INFECTED
    if vba_parser.detect_vba_macros():
        result = AV_STATUS_INFECTED
    else:
        result = AV_STATUS_CLEAN

    vba_parser.close()
    return result
