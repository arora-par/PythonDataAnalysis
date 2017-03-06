import enronutil
from email.parser import Parser
import glob
import os
import datetime
from collections import Counter
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

start_tracking_date = datetime.date(1998, 1, 1)
resignation_date = datetime.date(2001, 8, 14)
bankruptcy_date = datetime.date(2001, 12, 2)
# Identified in previous analysis
linked_members_stage_1 = ['rob.bradley@enron.com', 'joe.hillings@enron.com',
                  'jeffrey.garten@yale.edu', 'mark.lay@enron.com','sally.keepers@enron.com',
                    'sherri.sera@enron.com','kevinscott@onlinemailbox.net',
                    'eharris@insightpartners.com','joannie.williamson@enron.com',
                    'jeffrey.shankman@enron.com']

linked_members_stage_2 = ['enron_update@concureworkplace.com', 'l..wells@enron.com,'
                          ,'svarga@kudlow.com', 'nshaw@usenergyservices.com',
                          'j..kean@enron.com', 'john@pgsenergy.com',
                          'hema@izhuta.com','bpaddock@ghcf.org', 'news@real-net.net',
                          '_corolla@response.etracks.com']

linked_members_stage_3 = ['svarga@kudlow.com', 'mailings@cnn.com', 'lynda.l.phinney@williams.com', 'enron_update@concureworkplace.com','jharwood@mindspring.com']

def reset_stages(imp_emails_stage1, imp_emails_stage2, imp_emails_stage3, unread_files):
    del imp_emails_stage1[:]
    del imp_emails_stage2[:]
    del imp_emails_stage3[:]
    del unread_files[:]
def readRecursively(dirname, imp_emails_stage1, imp_emails_stage2, imp_emails_stage3, unread_files, action):
    for item in glob.glob(dirname + '/*'):
        if os.path.isfile(item):
            try:
                with open(item) as email_file:
                    email_item = Parser().parsestr(email_file.read())
                    if (email_item):
                        apply_action_for_stages(email_item, imp_emails_stage1, imp_emails_stage2, imp_emails_stage3, action)

            except UnicodeDecodeError:
                unread_files.append(item)
        else:
            readRecursively(item, imp_emails_stage1, imp_emails_stage2, imp_emails_stage3, unread_files, action)

def apply_action_for_stages(email_item, imp_emails_stage1, imp_emails_stage2, imp_emails_stage3, action):

    email_from = email_item['from']
    email_recipients = []
    email_to = email_item['to']
    if email_to:
        email_recipients = email_recipients + email_to.split()
    email_cc = email_item['cc']
    if email_cc:
        email_recipients = email_recipients + email_cc.split()
    email_bcc = email_item['bcc']
    if email_bcc:
        email_recipients = email_recipients + email_bcc.split()

    email_date = email_item['date']
    parsed_date = datetime.datetime.strptime(email_date[:-6], "%a, %d %b %Y %H:%M:%S %z")
    parsed_date = parsed_date.date()
    email_body = email_item.get_payload()

    # check dates to figure out stage number
    if parsed_date > start_tracking_date and parsed_date <= resignation_date:
        # invoke action on corresponding stage
        imp_emails_stage1.extend(action(email_from, email_recipients, email_body, imp_emails_stage1, linked_members_stage_1))
    elif parsed_date > resignation_date and parsed_date < bankruptcy_date:
        imp_emails_stage2.extend(action(email_from, email_recipients, email_body, imp_emails_stage2, linked_members_stage_2))
    elif parsed_date > bankruptcy_date:
        imp_emails_stage3.extend(action(email_from, email_recipients, email_body, imp_emails_stage3, linked_members_stage_3))
