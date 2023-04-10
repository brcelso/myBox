from autoreplyer import AutoReplyer

class YourAutoReplyer(AutoReplyer):
        
        imap_server = 'imap.gmail.com'
        imap_port = 993  # Custom port, only use if the default one doesn’t work.
        imap_user = 'celsosilvajunior90@gmail.com'
        imap_password = 'eyoqlfiiurvoicub'
        smtp_server = 'smtp.gmail.com'
        smtp_port = 465  # Custom port, only use if the default one doesn’t work.
        smtp_user = 'celsosilvajunior90@gmail.com'
        smtp_password = 'eyoqlfiiurvoicub'
        from_address = 'Celso da Silva Junior <celsosilvajunior90@gmail.com>'
        body = '''
        Hello,
        I’m on vacation until a date I should mention here.
        You’ll have an answer when I’m back.
        Call Django in case of emergency.
        Have a nice day,
        You
        '''
        body_html = '''
        <p>Hello</p>,
        <p>
            I’m on vacation until a date I should mention here.<br />
            You’ll have an answer when I’m back.<br />
            Call <a href="tel:+1234567890">Django</a> in case of emergency.
        </p>
        <p>
            Have a nice day,<br />
            You
        </p>
        '''
YourAutoReplyer().run()
