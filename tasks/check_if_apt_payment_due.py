## Checks if my apartment payment is due.
from tasks.browser_task import BrowserTask

HUMAN_STR = "Your rent is %s."

def run(browser):
    url = "https://milestonecorporate.residentportal.com/resident_portal/"
    print("Navigating.")
    browser.get(url)
    
    email, password = get_cred(url)
    print("Setting email.")
    set_value(browser, '#email', email)
    print("Setting password.")
    set_value(browser, '#password', password)
    
    print("Submitting form.")
    browser.find_element_by_id('authentication').submit()
    
    print("Waiting...")
    wait_for_class(browser, 'modulePay')
    
    print("Getting value.")
    browser.execute_script("$('strong > span').attr('id', 'tar')")
    text = get_text_from_id(browser, 'tar')
    return (text, "green" if float(text.replace("$", "").replace(",", "")) <= 0.0 else "red")  
    print("Amount due: " + text)
    
task = BrowserTask(run_func = run, humanized_template = HUMAN_STR)
task.run()
task.commit_result()
