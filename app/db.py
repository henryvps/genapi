from baserowapi import Baserow, Filter

# Initialize the Baserow client
baserow = Baserow(url='https://baserow.warren.io', token='4QcrBjvLJXT10aO2eCc2xBPLRXauRMfp')

table = baserow.get_table(547) # Articles table

schema = {
    'URL': '',
    'Original Content': '',
    'Generated Content': '',
    'Published': False,
    'Linkedin Post': '',
    'Tweet': ''
}


### DONE
def check_duplicates(rows, url):                  
    for row in rows:
        if row['URL'] == url and row['URL'] != "":
            return True
        else:
            return False
        

### DONE
def save_article(id, url, original_content):
    row = table.get_row(id)
    row['URL'] = url
    row['Original Content'] = original_content
    row.update()



### DONE
def add_new_row():
    new_row = table.add_row({})
    return new_row


### TODO
def get_unpublished():                      
    rows_unpublish = table.get_rows(filters=[Filter("URL", "")])
    for row in rows_empty_original_url:
        updated_row = single_row.update({'Published': False})
        print(row.update())



### TEST                                           
#print(save_article(3, 'https://test.ee'))
#add_new_row()
#print(check_duplicates("https://test.ee"))


