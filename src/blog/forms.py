from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60, 
        widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Your Name"
        
        })
        
    )

    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    
    )

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your full name"
            }
        )
    )

    email_address = forms.EmailField(
        max_length=60,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your email address"
            }
        )
    )

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your message"
            }
        )
    )