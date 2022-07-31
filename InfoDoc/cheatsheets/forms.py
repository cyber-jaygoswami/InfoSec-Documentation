from .models import PdfFile
from django.forms import ModelForm

class UploadFile(ModelForm):
    class Meta:
        model = PdfFile
        fields = '__all__'
        labels = {
            'pdf_file':'File'
        }
    
    def __init__(self,*args,**kwargs):
        super(UploadFile,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            if not name == 'pdf_file':
                field.widget.attrs.update({'class':'form-control form-control-lg'})
            else:
                 field.widget.attrs.update({'accept':'.pdf'})

            