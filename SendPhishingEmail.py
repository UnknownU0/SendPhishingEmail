import telnetlib


def SendPhishingEmail(MXServer, MailFrom, MailTo, Subject, Text):
    TelnetConnect = telnetlib.Telnet()
    TelnetConnect.open(MXServer, 25)
    TelnetConnect.write(b"EHLO UnknownSecurity\r\n")
    time.sleep(0.1)
    Mail_From = "MAIL FROM:<" + str(MailFrom) + ">"
    TelnetConnect.write(Mail_From.encode() + b'\r\n')
    time.sleep(0.1)
    Mail_To = "RCPT TO:<" + str(MailTo) + ">"
    TelnetConnect.write(Mail_To.encode() + b'\r\n')
    time.sleep(0.1)
    TelnetConnect.write(b'DATA\r\n')
    time.sleep(0.1)
    Mail_Data = "TO:<" + str(MailTo) + ">\r\nFROM:<" + str(MailFrom) + ">\r\nSUBJECT:" + str(Subject) + "\r\n\r\n" + str(Text) + "\r\n.\r\n"
    TelnetConnect.write(Mail_Data.encode())
    time.sleep(0.1)
    TelnetConnect.write(b'QUIT\r\n')
    time.sleep(0.1)
    TelnetConnect.close()


SendPhishingEmail("Your MXServer to Send", "UnknwonSecurity@UnknownSecurity.UnknownSecurity", "Mail to address", "Miss You Mybro!","Now, I Miss You So Much!!!")
