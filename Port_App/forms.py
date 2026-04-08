from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'w-full px-4 py-3 rounded-lg contact-input focus:outline-none',
        'placeholder': 'Your Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'w-full px-4 py-3 rounded-lg contact-input focus:outline-none',
        'placeholder': 'Your Email'
    }))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'w-full px-4 py-3 rounded-lg contact-input focus:outline-none',
        'placeholder': 'Subject'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'w-full px-4 py-3 rounded-lg contact-input focus:outline-none',
        'rows': 5,
        'placeholder': 'Message'
    }))
