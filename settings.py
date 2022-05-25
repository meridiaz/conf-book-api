"""
ConfBookGenerator settings.
"""
# Google Spreadsheet id
SPREADSHEET_ID = "1gODHlD5Qby3VHwXUntyvR4kQ2NEObT_jhqvOVRfmwvQ"#"1d7pYMrvO7WVfzTd06Xlx_ZH1TgmkK2vQXwwp1skCzVE"
#"1cWBAVb_pUqJlmlaxsXmajPK3601ZxToZWv6qP3wRj3g"

# Conference long name and short name (LaTeX special chars have to be escaped)
LONG_NAME = "Training to share knowledge and experiences in implementing AI at schools"
SHORT_NAME = "LTTA June 2022"

# Conference place and dates (LaTeX special chars have to be escaped)
PLACE = "Braga, Portugal"
DATES = "May 31\\textsuperscript{st} - June 3\\textsuperscript{rd}, 2022"

# Front Image of the ConfBook and logo of the conference (and sizes)
FRONT_IMAGE = "logoBraga.jpeg"
LOGO = "logoFAIaS.png"
FRONT_IMAGE_WIDTH = "14cm"
LOGO_HEIGHT = "1cm"
#'topics', 
# Google Spreadsheet column names
HEADER = ['date', 'name', 'position', 'affiliation', 'nationality', 'graduation', 'picture', 'topics', 'homepage', 'twitter', 'presentation', 'programming', 'hobbies', 'looking', 'hiring']
HEADER = ['date', 'name', 'affiliation', 'position', 'presentation', 'nationality', 'graduation', 'picture', 'homepage', 'twitter', 'looking', 'hiring', 'programming', 'hobbies']
HEADER = ['date', 'mail', 'name', 'affiliation', 'position', 'presentation', 'nationality', 'picture', 'homepage', 'twitter']#, 'looking', 'hiring', 'programming', 'hobbies']

# If generates Graphics and which (column names)
GENERATE_GRAPHICS = False#True
GRAPHICS_TO_GENERATE = ['hiring', 'looking']

# If generates Lists and which (column names + answer)
GENERATE_LISTS = False#True
LISTS_TO_GENERATE = [['hiring', 'Yes'], ['looking', 'Yes'], ['nationality', 'Spain']]
