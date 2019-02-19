from os.path import join as os_path_join
from django.conf import settings
from django import forms

class UploadFileForm(forms.Form):
    _SAVE_PATH = settings.FORM_ROOT
    title = forms.CharField(max_length=50)
    file = forms.FileField()

    # how to use above two fields?
    """
    form = UploadFile
    """

    def save(self):
        saved_file = os_path_join(self._SAVE_PATH, self['title'].data)
        with open(saved_file, "wb") as f:
            f.write(self['file'].data.read())