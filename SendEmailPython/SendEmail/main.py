from autoreplyer import AutoReplyer

class YourAutoReplyer(AutoReplyer):
        
        imap_server = 'imap.gmail.com'
        imap_port = 993  # Custom port, only use if the default one doesn’t work.
        imap_user = 'gillthebot@gmail.com'
        imap_password = 'xuigobopavjgqaql'
        smtp_server = 'smtp.gmail.com'
        smtp_port = 465  # Custom port, only use if the default one doesn’t work.
        smtp_user = 'gillthebot@gmail.com'
        smtp_password = 'xuigobopavjgqaql'
        from_address = 'Gill The Bot <gillthebot@gmail.com>'
        body = '''
        Hello,
        I’m Gill The Bot.
        Have a nice day,
        Gill
        '''
        body_html = '''
        <p>Hello</p>,
        <p>
            I’m Gill The Bot.<br />
            Call <a href="tel:+1234567890">Django</a> in case of emergency.
        </p>
        <p>
            Have a nice day,<br />
            Gill
        </p>
        '''
YourAutoReplyer().run()
