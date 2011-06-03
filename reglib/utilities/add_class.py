import fetch_html
import parse_html
from login import login

def add_class(crn, crn2, schedule):
    login_number = 2
    for i in range(login_number):
        html = fetch_html.setup_ad_page()
        title = parse_html.get_page_title(html)
        form_data = ''
        if title != 'Login':
            if title == 'Select Term ':
                schedule.current_term = parse_html.get_current_term(html)
                form_data = fetch_html.current_term_form(schedule.current_term)
        else:
            login()
            continue
        
        html = fetch_html.add_drop_page(form_data)
        # Get a dictionary of values to post as the form
        values = parse_html.add_class(html, crn, crn2)
        html = fetch_html.add_class(values)
        
        # See if there were any errors when posting the form
        return parse_html.add_class_has_errors(html) 