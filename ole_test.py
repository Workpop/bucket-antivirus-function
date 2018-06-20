import ole

def test_clean_docx():
    assert ole.has_macros('test/clean_with_image.docx') == False
    assert ole.has_macros('test/clean.docx') == False

def test_clean_doc():
    assert ole.has_macros('test/clean.doc') == False

def test_macro_doc():
    assert ole.has_macros('test/macro.doc') == True

def test_macro_docx():
    assert ole.has_macros('test/macro.docx') == True

def test_macro_docm():
    assert ole.has_macros('test/macro.docm') == True

def test_non_word_files():
    # we only need to test allowed mime type files since the check occurs
    # after the mime check
    assert ole.has_macros('test/clean.jpg') == False
    assert ole.has_macros('test/clean.gif') == False
    assert ole.has_macros('test/clean.pdf') == False
    assert ole.has_macros('test/clean.tiff') == False
