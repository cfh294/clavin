import smtplib
from typing import Optional
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Mail(object):
    def __init__(self, text="", html="", subtype="alternative", subject="", from_address=None, to_list=[], cc_list=[], bcc_list=[]):
        super().__init__(subtype)

        self.__subtype = subtype
        self.text = text
        self.html = html
        self.subject = subject
        self.from_address = from_address
        self.to_list = to_list 
        self.cc_list = cc_list
        self.bcc_list = bcc_list

    @property
    def message(self):
        base = MIMEMultipart(self.__subtype)
        base["To"] = ",".join(self.to_list)
        base["From"] = self.from_address
        
        if self.subject:
            base["Subject"] = self.subject
        if self.cc_list:
            base["Cc"] = self.cc_list
        if self.bcc_list:
            base["Bcc"] = self.bcc_list
        if self.text:
            base.attach(self.text)
        if self.html:
            base.attach(self.html)
        return base


    @property 
    def recipient_list(self):
        return self.to_list + self.cc_list + self.bcc_list

    @property
    def to_list(self):
        return self._to_list
    
    @to_list.setter
    def to_list(self, value):
        if not isinstance(value, list):
            raise ValueError("Email to-list must be a list.")
        self._to_list = value

    @property
    def cc_list(self):
        return self._cc_list
    
    @cc_list.setter
    def cc_list(self, value):
        if not isinstance(value, list):
            raise ValueError("Email cc-list must be a list.")
        self._cc_list = value

    @property
    def bcc_list(self):
        return self._bcc_list
    
    @bcc_list.setter
    def cc_list(self, value):
        if not isinstance(value, list):
            raise ValueError("Email bcc-list must be a list.")
        self._bcc_list = value

    @property
    def subject(self):
        return self._subject
    
    @subject.setter
    def subject(self, value):
        if not isinstance(value, str):
            raise ValueError("Email subject must be a string.")
        elif value:
            self._subject = MIMEText(value, "plain")
        else:
            self._subject = None

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, value):
        if not isinstance(value, str):
            raise ValueError("Email text must be a string.")
        elif value:
            self._text = MIMEText(value, "plain")
        else:
            self._text = None

    @property
    def html(self):
        return self._html
    
    @html.setter
    def html(self, value):
        # TODO html files/templates
        if not isinstance(value, str):
            raise ValueError("Email HTML must be a string.")
        elif value:
            self._html = MIMEText(value, "html")
        else:
            self._html = None

    @property
    def from_address(self):
        return self._from_address
    
    @from_address.setter
    def from_address(self, value):
        if not value:
            raise ValueError("From-address required.")
        elif not isinstance(value, str):
            raise ValueError("From-address must be a string.")
        else:
            self._from_address = value


class MailMan(smtplib.SMTP):
    def __init__(*args, **kwargs):
        super().__init__(*args, **kwargs)

    def deliver(self, mail_object: Optional[Mail]=None, **kwargs):
        if not mail_object:
            mail_object = Mail(**kwargs)
        self.sendmail(
            mail_object.from_address,
            mail_object.recipient_list,
            mail_object.message.as_string()
        )
