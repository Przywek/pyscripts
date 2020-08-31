import imapclient, pyzmail
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('xxxx@gmail.com', 'xx@x')
imapObj.select_folder('INBOX', readonly=True)
# imap search keys for more search keys
UIDs = imapObj.search(['FROM', 'karol.przywarty@gmail.com'])
rawMessages = imapObj.fetch([5717], ['BODY[]', 'FLAGS'])
message = pyzmail.PyzMessage.factory(rawMessages[5717][b'BODY[]'])
message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('cc')
message.get_addresses('bcc')
message.text_part != None
message.text_part.get_payload().decode(message.text_part.charset)
message.html_part != None
message.html_part.get_payload().decode(message.html_part.charset)
imapObj.select_folder('INBOX', readonly=False)
IDs = imapObj.search(['ON', '09-Jul-2015'])
imapObj.delete_messages(UIDs)
imapObj.expunge()
imapObj.logout()
