import re
import magic

document_mime_types = [
    'text/plain',
    'text/rtf',
    # .docx, .docm
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    # .doc
    'application/msword',
    # .pdf
    'application/pdf',
]

image_mime_pattern = '^image\/[\w+-]+$'

def validate_mime(file_path):
    """
    Given the path to a file on disk, ensure its mime type is an allowed
    document mime type OR matches the allowed image mime pattern.
    """
    file_mime = magic.from_file(file_path, mime=True)
    is_valid = (file_mime in document_mime_types) or bool(re.match(image_mime_pattern, file_mime))

    print("[mime] %s for file %s validation result %r" % (file_mime, file_path, is_valid))

    return is_valid
