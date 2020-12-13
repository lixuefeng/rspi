# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
import smtplib
import os

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

def sendMail(text,
             subject='转发服务',
             from_addr='xfunl@qq.com',
             password='bgivsulgvsfmbgfj',
             to_addr='xfunl@qq.com',
             smtp_server='smtp.qq.com'):

    msg = MIMEText(text, 'plain', 'utf-8')
    msg['From'] = _format_addr(u'树莓派手机<%s>' % from_addr)
    msg['To'] = _format_addr(u'我的手机<%s>' % to_addr)
    msg['Subject'] = Header(subject, 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(3)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
def sendMultipartMail(text,
             imgs=[],
             subject='转发服务',
             from_addr='xfunl@qq.com',
             password='bgivsulgvsfmbgfj',
             to_addr='xfunl@qq.com',
             smtp_server='smtp.qq.com'):
    # 邮件对象:
    msg = MIMEMultipart()
    msg['From'] = _format_addr(u'树莓派手机<%s>' % from_addr)
    msg['To'] = _format_addr(u'我的手机<%s>' % to_addr)
    msg['Subject'] = Header(subject, 'utf-8').encode()

    # 邮件正文是MIMEText:
    msg.attach(MIMEText(text, 'plain', 'utf-8'))

    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    for img in imgs:
        if not os.path.isfile(img):
            log = logging.getLogger('gsmmodem.modem.GsmModem')
            self.log.warn('image not exists %s', img)
            continue
        with open(img, 'rb') as f:
            # 设置附件的MIME和文件名，这里是png类型:
            file_name = os.path.basename(img)
            mime = MIMEBase('image', 'png', filename=file_name)
            # 加上必要的头信息:
            mime.add_header('Content-Disposition', 'attachment', filename=file_name)
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            # 把附件的内容读进来:
            mime.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(mime)
            # 添加到MIMEMultipart:
            msg.attach(mime)
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(0)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
