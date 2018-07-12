import mime

def test_plaintext():
    assert mime.validate_mime('test/plain.txt') == True
    assert mime.validate_mime('test/eicar.pdf') == True

def test_rtf():
    assert mime.validate_mime('test/richtext.rtf') == True

def test_doc():
    assert mime.validate_mime('test/clean.doc') == True
    assert mime.validate_mime('test/macro.doc') == True
    assert mime.validate_mime('test/clean_doc_renamed.txt') == True

def test_docx():
    assert mime.validate_mime('test/clean.docx') == True
    assert mime.validate_mime('test/clean_with_image.docx') == True
    assert mime.validate_mime('test/macro.docx') == True

def test_docm():
    assert mime.validate_mime('test/macro.docm') == True

def test_jpg():
    assert mime.validate_mime('test/clean.jpg') == True

def test_gif():
    assert mime.validate_mime('test/clean.gif') == True

def test_tif():
    assert mime.validate_mime('test/clean.tiff') == True

def test_png():
    assert mime.validate_mime('test/clean.png') == True

def test_svg():
    assert mime.validate_mime('test/clean.svg') == True

def test_pdf():
    assert mime.validate_mime('test/clean.pdf') == True

def test_pptx():
    assert mime.validate_mime('test/clean.pptx') == False

def test_jsp():
    assert mime.validate_mime('test/page.jsp') == False

def test_perl():
    assert mime.validate_mime('test/script.pl') == False

def test_php():
    assert mime.validate_mime('test/hello.php') == False
    assert mime.validate_mime('test/hellophp.txt') == False

def test_java():
    assert mime.validate_mime('test/HelloWorld.java') == False
    assert mime.validate_mime('test/HelloWorld.class') == False

def test_bash():
    assert mime.validate_mime('test/script.sh') == False

def test_xlsb():
    assert mime.validate_mime('test/sheet.xlsb') == False

def test_xlsm():
    assert mime.validate_mime('test/sheet.xlsm') == False

def test_xlsx():
    assert mime.validate_mime('test/sheet.xlsx') == False
    assert mime.validate_mime('test/sheet2.xlsx') == False

def test_zip():
    assert mime.validate_mime('test/test.zip') == False
