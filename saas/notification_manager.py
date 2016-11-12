import os
MY_OWN_SENDGRID_API_KEY = os.getenv('MY_OWN_SENDGRID_API_KEY', '')
from django.template import Context, Template
import sendgrid

def send_test_letter():
    email_html = unicode(("Hello!!!!!").encode('ascii', 'xmlcharrefreplace'))
    subject = unicode("firs email")
    context = Context({})
    html = (Template(email_html)).render(context)

    sg = sendgrid.SendGridAPIClient(apikey=MY_OWN_SENDGRID_API_KEY)
    data = {
        "categories": ['test_letter', ],
        "content": [{"type": "text/html", "value": html}],
        "from": {"email": unicode('muro@mur.com')},
        "personalizations": [{"subject": subject, "to": [{"email": unicode('muroslav2909@gmail.com')}]}],
        "tracking_settings": {"click_tracking": {"enable": True, "enable_text": True},
                              "open_tracking": {"enable": True, "substitution_tag": "%opentrack"},}
    }
    response = sg.client.mail.send.post(request_body=data)
    return response



def send_letter(template, subject, category, to, context):
    email_html = unicode((template).encode('ascii', 'xmlcharrefreplace'))
    subject = unicode(subject)

    html = (Template(email_html)).render(context)

    sg = sendgrid.SendGridAPIClient(apikey=MY_OWN_SENDGRID_API_KEY)
    data = {
        "categories": [category, ],
        "content": [{"type": "text/html", "value": html}],
        "from": {"email": unicode('SchoolSaas@saas.com'), "name": "School Saas"},
        "personalizations": [{"subject": subject, "to": [{"email": unicode(to)}]}],
        "tracking_settings": {"click_tracking": {"enable": True, "enable_text": True},
                              "open_tracking": {"enable": True, "substitution_tag": "%opentrack"},}
    }
    response = sg.client.mail.send.post(request_body=data)
    print response.status_code
    return response